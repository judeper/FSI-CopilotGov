// Phase E smoke test — portal envelope export / import round-trip.
// Populates 3 mock answers, calls buildEnvelope, asserts the schema
// top-level keys, then re-imports the envelope into a fresh app and
// verifies the answers round-trip verbatim.

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
  const lock = JSON.parse(readFileSync(LOCK_PATH, "utf8"));
  app.solutionsLock = lock;
  app.solutionsLockById = {};
  (lock.solutions || []).forEach((s) => { if (s && s.id) app.solutionsLockById[s.id] = s; });
  app.state = {
    schemaVersion: 2,
    assessmentId: "test-e",
    scoping: {
      zones: [1, 2, 3],
      targetLevel: "recommended",
      organizationName: "Acme Bank, N.A.",
      assessorName: "Jane Doe",
      assessorRole: "Compliance Lead",
    },
    responses: {},
    completedSteps: [],
  };
  app.step = "export";
  return { app, window, document, exports: mod.exports };
}

describe("Phase E portal export envelope", () => {
  it("exposes ENVELOPE_SCHEMA_VERSION and identity storage key", () => {
    const { mod } = bootstrap();
    const s = mod.exports;
    expect(s.ENVELOPE_SCHEMA_VERSION).toBe("fsi-copilotgov-envelope/0.1.0");
    expect(s.ENVELOPE_IDENTITY_KEY).toBe("fsi-copilotgov:envelope-identity");
  });

  it("buildEnvelope returns a schema-valid envelope with top-level keys", async () => {
    const { app } = await initApp();
    app.state.responses["1.2"] = { answer: "yes", notes: "dlp active" };
    app.state.responses["2.1"] = { answer: "partial", notes: "partial CA coverage" };
    app.state.responses["3.1"] = { answer: "no", notes: "" };
    const env = app.buildEnvelope();
    // Top-level keys
    [
      "schemaVersion", "generatedAt", "assessor", "scope", "manifest",
      "solutionsLock", "answers", "summary", "signatures",
    ].forEach((k) => expect(env).toHaveProperty(k));
    expect(env.schemaVersion).toBe("fsi-copilotgov-envelope/0.1.0");
    expect(env.scope.pillars).toEqual([1, 2, 3, 4]);
    expect(env.scope.tier).toBe("recommended");
    expect(env.manifest.controlCount).toBe(58);
    // ref is whatever generate_solutions_lock.PINNED_REF currently emits;
    // assert against the on-disk lock to stay version-agnostic.
    const lockRef = JSON.parse(readFileSync(LOCK_PATH, "utf8")).source.ref;
    expect(env.solutionsLock.ref).toBe(lockRef);
    expect(env.solutionsLock.commit).toMatch(/^[0-9a-f]{40}$/);
    expect(Array.isArray(env.answers)).toBe(true);
    expect(env.answers).toHaveLength(58);
    expect(env.summary.yes).toBe(1);
    expect(env.summary.partial).toBe(1);
    expect(env.summary.no).toBe(1);
    expect(env.summary.unanswered).toBe(55);
    expect(env.signatures).toEqual({ assessorSignedAt: null, facilitatorSignedAt: null });
    // Identity folded from scoping when envelope-identity-store is empty.
    expect(env.assessor.name).toBe("Jane Doe");
    expect(env.assessor.org).toBe("Acme Bank, N.A.");
    // generatedAt must be ISO.
    expect(env.generatedAt).toMatch(/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}/);
  });

  it("envelope embeds collector evidence for affected controls", async () => {
    const { app } = await initApp();
    app.state.responses["1.2"] = { answer: "yes", notes: "" };
    app.applyCollectorEvidence({
      "1.2": {
        status: "yes",
        evidence: [{ key: "k", raw: "r", collectedAt: "t", status: "yes" }],
      },
    }, "ct.csv");
    const env = app.buildEnvelope();
    const row = env.answers.find((a) => a.controlId === "1.2");
    expect(row.answer).toBe("yes");
    expect(row.collectorEvidence).not.toBeNull();
    expect(row.collectorEvidence.runId).toBe("ct.csv");
    expect(row.collectorEvidence.evidence).toHaveLength(1);
  });

  it("importEnvelope round-trips 3 mock answers", async () => {
    const { app } = await initApp();
    app.state.responses["1.2"] = { answer: "yes", notes: "dlp active" };
    app.state.responses["2.1"] = { answer: "partial", notes: "3 of 5 scopes" };
    app.state.responses["3.1"] = { answer: "no", notes: "no policy" };
    const env = app.buildEnvelope();

    // Fresh app for import target.
    const { app: app2 } = await initApp();
    // Verify the fresh app has no answers.
    expect(Object.keys(app2.state.responses)).toHaveLength(0);
    const result = app2.importEnvelope(env);
    expect(result.controls).toBe(58);

    expect(app2.state.responses["1.2"].answer).toBe("yes");
    expect(app2.state.responses["1.2"].notes).toBe("dlp active");
    expect(app2.state.responses["2.1"].answer).toBe("partial");
    expect(app2.state.responses["2.1"].notes).toBe("3 of 5 scopes");
    expect(app2.state.responses["3.1"].answer).toBe("no");
    expect(app2.state.responses["3.1"].notes).toBe("no policy");
    // Scoping tier round-trips.
    expect(app2.state.scoping.targetLevel).toBe("recommended");
    expect(app2.state.scoping.organizationName).toBe("Acme Bank, N.A.");
  });

  it("importEnvelope rejects a non-CopilotGov schema", async () => {
    const { app } = await initApp();
    expect(() => app.importEnvelope({ schemaVersion: "fsi-agentgov-envelope/0.1.0", answers: [] }))
      .toThrow(/Not a CopilotGov envelope/);
    expect(() => app.importEnvelope(null)).toThrow(/Envelope must be an object/);
  });

  it("collector evidence round-trips through export/import", async () => {
    const { app } = await initApp();
    app.state.responses["1.2"] = { answer: "yes", notes: "" };
    app.applyCollectorEvidence({
      "1.2": {
        status: "yes",
        evidence: [{ key: "purview.dlp", raw: "12 policies", collectedAt: "2026-04-21", status: "yes" }],
      },
    }, "ct-round.csv");
    const env = app.buildEnvelope();

    const { app: app2 } = await initApp();
    app2.importEnvelope(env);
    const ce = app2.getCollectorEvidenceFor("1.2");
    expect(ce).not.toBeNull();
    expect(ce.runId).toBe("ct-round.csv");
    expect(ce.evidence[0].key).toBe("purview.dlp");
    expect(app2.state.collectorRunId).toBe("ct-round.csv");
  });

  it("export view renders envelope and load-envelope buttons", async () => {
    const { app, document } = await initApp();
    app.render();
    // The "Export envelope (.json)" card appears in the export grid.
    const exportCards = document.querySelectorAll(".ag-export-card");
    const envelopeCard = Array.from(exportCards).find((c) => c.textContent.includes("Export envelope"));
    expect(envelopeCard).toBeTruthy();
    expect(document.getElementById("envelope-import-btn")).not.toBeNull();
  });
});
