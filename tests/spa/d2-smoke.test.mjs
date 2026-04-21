// D2 smoke test — validates collector evidence import: the CSV parser
// helper produces a correctly-shaped map, the applier pre-fills answers
// while recording prior values, the drawer renders a Collector evidence
// section for affected controls, and the Clear action reverts pre-fills
// without touching manual answers.

import { describe, it, expect } from "vitest";
import { JSDOM } from "jsdom";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const REPO = join(here, "..", "..");
const SPA_PATH = join(REPO, "docs", "javascripts", "assessment-app.js");
const MANIFEST_PATH = join(REPO, "assessment", "manifest", "controls.json");
const LOCK_PATH = join(REPO, "assessment", "data", "solutions-lock.json");
const DATA_PATH = join(REPO, "docs", "javascripts", "assessment-data.json");

function bootstrap() {
  const dom = new JSDOM(
    '<!DOCTYPE html><html><body><div id="assessment-app" class="assessment-container"></div></body></html>',
    { url: "http://localhost/" },
  );
  const { window } = dom;
  window.fetch = async (url) => {
    const u = String(url);
    let file;
    if (u.endsWith("assessment-data.json")) file = DATA_PATH;
    else if (u.endsWith("controls.json")) file = MANIFEST_PATH;
    else if (u.endsWith("solutions-lock.json")) file = LOCK_PATH;
    if (!file) return { ok: false, status: 404, json: async () => null };
    const body = readFileSync(file, "utf8");
    return { ok: true, status: 200, json: async () => JSON.parse(body) };
  };
  const src = readFileSync(SPA_PATH, "utf8");
  const mod = { exports: {} };
  const fn = new window.Function(
    "module", "exports", "window", "document", "localStorage", "fetch", "URL", "navigator", "console",
    src,
  );
  fn(
    mod, mod.exports,
    window, window.document, window.localStorage,
    window.fetch, window.URL, window.navigator, window.console,
  );
  return { window, document: window.document, mod };
}

async function initApp() {
  const { window, document, mod } = bootstrap();
  const container = document.getElementById("assessment-app");
  const { AssessmentApp } = mod.exports;
  const app = new AssessmentApp(container);
  await app.loadData();
  const manifest = JSON.parse(readFileSync(MANIFEST_PATH, "utf8"));
  app.manifest = manifest;
  app.manifestById = {};
  manifest.forEach((row) => { if (row && row.id) app.manifestById[row.id] = row; });
  const lock = JSON.parse(readFileSync(LOCK_PATH, "utf8"));
  app.solutionsLock = lock;
  app.solutionsLockById = {};
  (lock.solutions || []).forEach((s) => { if (s && s.id) app.solutionsLockById[s.id] = s; });
  app.state = {
    schemaVersion: 2,
    assessmentId: "test-d2",
    scoping: { zones: [1, 2, 3], targetLevel: "recommended" },
    selectedSector: "bank",
    responses: {},
    completedSteps: [],
  };
  app.step = "phase1";
  app.render();
  return { app, window, document, exports: mod.exports };
}

const THREE_ROW_CSV = [
  "control_id,evidence_key,status,raw_value,collected_at",
  "1.2,purview.dlp.policies,pass,12 policies active,2026-04-21T09:00:00Z",
  "2.1,entra.conditional_access,partial,\"3 of 5 scopes covered\",2026-04-21T09:05:00Z",
  "3.1,defender.communication_compliance,fail,no policy configured,2026-04-21T09:10:00Z",
].join("\n");

describe("D2 collector evidence import", () => {
  it("exports parseCollectorCsv / parseCollectorJson / constants on the test seam", () => {
    const { mod } = bootstrap();
    const s = mod.exports;
    expect(typeof s.parseCollectorCsv).toBe("function");
    expect(typeof s.parseCollectorJson).toBe("function");
    expect(s.COLLECTOR_EVIDENCE_KEY_PREFIX).toBe("fsi-copilotgov:collector-evidence:");
    expect(s.COLLECTOR_STATUS_MAP).toEqual({ pass: "yes", partial: "partial", fail: "no" });
  });

  it("parses a 3-row CSV into a map with correct status mapping", () => {
    const { mod } = bootstrap();
    const { parseCollectorCsv } = mod.exports;
    const map = parseCollectorCsv(THREE_ROW_CSV);
    expect(Object.keys(map)).toHaveLength(3);
    expect(map["1.2"].status).toBe("yes");
    expect(map["2.1"].status).toBe("partial");
    expect(map["3.1"].status).toBe("no");
    expect(map["1.2"].evidence[0].key).toBe("purview.dlp.policies");
    expect(map["2.1"].evidence[0].raw).toBe("3 of 5 scopes covered"); // quoted cell preserved
    expect(map["3.1"].evidence[0].collectedAt).toBe("2026-04-21T09:10:00Z");
  });

  it("warns on unknown status values but still records the evidence row", () => {
    const { mod } = bootstrap();
    const { parseCollectorCsv } = mod.exports;
    const warnings = [];
    const prev = console.warn;
    console.warn = (...args) => warnings.push(args.join(" "));
    try {
      const map = parseCollectorCsv(
        "control_id,evidence_key,status,raw_value,collected_at\n1.1,foo,maybe,bar,now"
      );
      expect(map["1.1"].status).toBeNull();
      expect(map["1.1"].evidence).toHaveLength(1);
      expect(warnings.some((w) => w.includes("unknown status 'maybe'"))).toBe(true);
    } finally {
      console.warn = prev;
    }
  });

  it("applyCollectorEvidence pre-fills answers and clearCollectorEvidence reverts them", async () => {
    const { app } = await initApp();
    const { parseCollectorCsv } = (await import("node:fs")); // unused, suppress lint
    void parseCollectorCsv;
    // Seed a manual answer on 1.2 to ensure it is preserved in prior-answers.
    app.state.responses["1.2"] = { answer: "partial", notes: "manual jot" };
    const map = {
      "1.2": { status: "yes", evidence: [{ key: "k", raw: "r", collectedAt: "t", status: "yes" }] },
      "2.1": { status: "partial", evidence: [{ key: "k2", raw: "r2", collectedAt: "t2", status: "partial" }] },
      "3.1": { status: "no", evidence: [{ key: "k3", raw: "r3", collectedAt: "t3", status: "no" }] },
    };
    const result = app.applyCollectorEvidence(map, "test-run.csv");
    expect(result.prefillCount).toBe(3);
    expect(app.state.responses["1.2"].answer).toBe("yes");
    expect(app.state.responses["1.2"].notes).toBe("manual jot");
    expect(app.state.responses["2.1"].answer).toBe("partial");
    expect(app.state.responses["3.1"].answer).toBe("no");
    expect(app.state.collectorPriorAnswers["1.2"]).toBe("partial");
    expect(app.state.collectorPriorAnswers["2.1"]).toBeNull();

    app.clearCollectorEvidence();
    expect(app.state.responses["1.2"].answer).toBe("partial"); // reverted
    expect(app.state.responses["1.2"].notes).toBe("manual jot"); // preserved
    expect(app.state.responses["2.1"]).toBeUndefined(); // removed (no prior + no notes)
    expect(app.state.collectorEvidence).toBeUndefined();
    expect(app.state.collectorRunId).toBeUndefined();
  });

  it("drawer renders a Collector evidence section for affected controls", async () => {
    const { app, document } = await initApp();
    app.applyCollectorEvidence({
      "1.2": {
        status: "yes",
        evidence: [
          { key: "purview.dlp.policies", raw: "12 policies active", collectedAt: "2026-04-21T09:00Z", status: "yes" },
          { key: "purview.dlp.alerts", raw: "0 high-severity", collectedAt: "2026-04-21T09:00Z", status: "yes" },
        ],
      },
    }, "smoke-run.csv");
    app.render();
    const ctrl = app.data.controls.find((c) => c.id === "1.2");
    app.openDrawer(ctrl);
    const drawer = document.querySelector(".control-drawer.open");
    expect(drawer).not.toBeNull();
    const ceSec = drawer.querySelector(".collector-evidence-section");
    expect(ceSec).not.toBeNull();
    expect(ceSec.textContent).toContain("purview.dlp.policies");
    expect(ceSec.textContent).toContain("12 policies active");
    expect(ceSec.textContent).toContain("smoke-run.csv");
    // Drawer for a control not in the import should NOT have the section.
    app.closeDrawer();
    const other = app.data.controls.find((c) => c.id === "4.1");
    app.openDrawer(other);
    const drawer2 = document.querySelector(".control-drawer.open");
    expect(drawer2.querySelector(".collector-evidence-section")).toBeNull();
  });

  it("persists imported evidence to localStorage under the run-id key", async () => {
    const { app, window } = await initApp();
    app.applyCollectorEvidence({
      "1.2": { status: "yes", evidence: [{ key: "k", raw: "r", collectedAt: "t", status: "yes" }] },
    }, "persist-test.csv");
    const raw = window.localStorage.getItem("fsi-copilotgov:collector-evidence:persist-test.csv");
    expect(raw).not.toBeNull();
    const parsed = JSON.parse(raw);
    expect(parsed.runId).toBe("persist-test.csv");
    expect(parsed.evidence["1.2"].status).toBe("yes");
    app.clearCollectorEvidence();
    expect(window.localStorage.getItem("fsi-copilotgov:collector-evidence:persist-test.csv")).toBeNull();
  });

  it("import button and file input are rendered in Phase 1", async () => {
    const { document } = await initApp();
    expect(document.getElementById("collector-import-btn")).not.toBeNull();
    expect(document.getElementById("collector-import-input")).not.toBeNull();
  });
});
