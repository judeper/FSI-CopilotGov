// D1 smoke test — validates the four sub-features (drawer, facilitator
// mode, sector-calibration yes-bars, and solution recommendation cards)
// render both on authored controls (1.2, 1.3, 2.1, 3.1, 4.1) and on
// TODO-field controls (the remaining 53), and that graceful-degradation
// placeholders appear instead of "undefined" or empty markup.

import { describe, it, expect, beforeEach } from "vitest";
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
  // Stub fetch to serve local files.
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

async function initApp({ facilitator = false } = {}) {
  const { window, document, mod } = bootstrap();
  if (facilitator) window.localStorage.setItem("fsi-copilotgov:facilitator-mode", "1");
  const container = document.getElementById("assessment-app");
  const { AssessmentApp } = mod.exports;
  const app = new AssessmentApp(container);
  await app.loadData();
  // The real loader derives its base URL from the <script> tag, which is
  // absent in jsdom, so the manifest and solutions-lock fetches short-
  // circuit. Populate them directly so drawer/facilitator/solution
  // rendering exercises the real lookup paths.
  const manifest = JSON.parse(readFileSync(MANIFEST_PATH, "utf8"));
  app.manifest = manifest;
  app.manifestById = {};
  manifest.forEach((row) => { if (row && row.id) app.manifestById[row.id] = row; });
  const lock = JSON.parse(readFileSync(LOCK_PATH, "utf8"));
  app.solutionsLock = lock;
  app.solutionsLockById = {};
  (lock.solutions || []).forEach((s) => { if (s && s.id) app.solutionsLockById[s.id] = s; });
  // Recompute facilitator mode now that we've stubbed localStorage.
  app.facilitatorMode = window.localStorage.getItem("fsi-copilotgov:facilitator-mode") === "1";
  // Seed minimal state and jump to phase1 so renderPhase1 runs.
  app.state = {
    schemaVersion: 2,
    assessmentId: "test",
    scoping: { zones: [1, 2, 3], targetLevel: "recommended", sector: "bank" },
    selectedSector: "bank",
    responses: {},
    completedSteps: [],
    overrides: {},
  };
  app.step = "phase1";
  app.render();
  return { app, window, document, exports: mod.exports };
}

describe("D1 SPA smoke", () => {
  it("exports D1 helpers on the test seam", () => {
    const { exports } = bootstrap().mod;
    // loadSpa happens synchronously via fn() above, so exports are populated.
    // Actually bootstrap() returns { mod } with mod.exports populated.
    const s = bootstrap().mod.exports;
    expect(typeof s.AssessmentApp).toBe("function");
    expect(typeof s.isAuthored).toBe("function");
    expect(typeof s.isTodoString).toBe("function");
    expect(typeof s.authoredOr).toBe("function");
    expect(s.DRAWER_NOTES_PREFIX).toBe("fsi-copilotgov:notes:");
    expect(s.FACILITATOR_MODE_KEY).toBe("fsi-copilotgov:facilitator-mode");
  });

  it("isAuthored handles TODO strings, empty arrays, and nested objects", () => {
    const { mod } = bootstrap();
    const { isAuthored } = mod.exports;
    expect(isAuthored("TODO: pending")).toBe(false);
    expect(isAuthored("[TODO: describe]")).toBe(false);
    expect(isAuthored("")).toBe(false);
    expect(isAuthored(null)).toBe(false);
    expect(isAuthored(undefined)).toBe(false);
    expect(isAuthored("Real content")).toBe(true);
    expect(isAuthored([])).toBe(false);
    expect(isAuthored(["TODO: foo"])).toBe(false);
    expect(isAuthored(["TODO: foo", "real item"])).toBe(true);
    expect(isAuthored({})).toBe(false);
    expect(isAuthored({ a: "TODO: x" })).toBe(false);
    expect(isAuthored({ a: "TODO: x", b: "real" })).toBe(true);
  });

  it("renders 62 control rows with drawer trigger + yes-bar badges when authored", async () => {
    const { document } = await initApp();
    const rows = document.querySelectorAll(".control-row");
    expect(rows.length).toBe(62);
    // Drawer trigger on every row
    const triggers = document.querySelectorAll(".control-drawer-trigger");
    expect(triggers.length).toBe(62);
    // Facilitator toggle exists in Phase 1
    const facBtn = document.getElementById("facilitator-toggle");
    expect(facBtn).not.toBeNull();
    expect(facBtn.getAttribute("aria-pressed")).toBe("false");
    // Yes-bar badges: present on authored controls (1.2, 1.3, 2.1, 3.1, 4.1).
    const authoredIds = ["1.2", "1.3", "2.1", "3.1", "4.1"];
    authoredIds.forEach((id) => {
      const row = document.querySelector(`.control-row[data-control-id="${id}"]`);
      expect(row, `row ${id}`).not.toBeNull();
      const yesBar = row.querySelector(".yes-bar-badge");
      expect(yesBar, `yes-bar on ${id}`).not.toBeNull();
    });
  });

  it("opens the evidence drawer on click and graceful-degrades on TODO fields", async () => {
    const { app, document } = await initApp();
    // TODO control (1.1 has yesBar = TODO)
    const row11 = document.querySelector('.control-row[data-control-id="1.1"]');
    const ctrl11 = app.data.controls.find((c) => c.id === "1.1");
    app.openDrawer(ctrl11);
    const drawer = document.querySelector(".control-drawer.open");
    expect(drawer).not.toBeNull();
    // Pending placeholder should appear for TODO evidence.
    const pending = drawer.querySelector(".control-drawer-pending");
    expect(pending).not.toBeNull();
    // Solution-empty text should appear when solutions is empty OR a solution-card
    // exists when populated. Control 1.1 has 1 authored solution.
    const card = drawer.querySelector(".solution-card");
    expect(card).not.toBeNull();
    // "undefined" literal should never leak into drawer text.
    expect(drawer.textContent.toLowerCase()).not.toContain("undefined");
    // TODO-tokens should not leak into drawer text.
    expect(drawer.textContent).not.toMatch(/^\s*TODO:/m);
    app.closeDrawer();
    expect(document.querySelector(".control-drawer.open")).toBeNull();
  });

  it("drawer shows solution recommendation cards for authored control 1.2", async () => {
    const { app, document } = await initApp();
    const ctrl = app.data.controls.find((c) => c.id === "1.2");
    app.openDrawer(ctrl);
    const drawer = document.querySelector(".control-drawer");
    const cards = drawer.querySelectorAll(".solution-card");
    // FSI-CopilotGov: Control 1.2 maps to multiple solutions in the manifest (count derived from solutions-lock.json).
    expect(cards.length).toBeGreaterThanOrEqual(1);
    const first = cards[0];
    expect(first.getAttribute("href")).toMatch(/^https:\/\/github\.com/);
    // Card should contain a name, tier badge, and role pill.
    expect(first.querySelector(".solution-card-name")).not.toBeNull();
    expect(first.querySelector(".solution-card-tier")).not.toBeNull();
    expect(first.querySelector(".solution-card-role")).not.toBeNull();
  });

  it("facilitator mode toggle adds expanded panels on authored controls", async () => {
    const { app, document } = await initApp({ facilitator: true });
    expect(app.facilitatorMode).toBe(true);
    const wrap = document.querySelector(".phase1-wrap.facilitator-mode");
    expect(wrap).not.toBeNull();
    // Authored control 1.2 has facilitatorNotes.ask populated.
    const row12 = document.querySelector('.control-row[data-control-id="1.2"]');
    expect(row12.querySelector(".facilitator-panel")).not.toBeNull();
    expect(row12.querySelector(".facilitator-next")).not.toBeNull();
    // TODO control 1.1 must NOT render a facilitator panel (graceful degrade).
    const row11 = document.querySelector('.control-row[data-control-id="1.1"]');
    expect(row11.querySelector(".facilitator-panel")).toBeNull();
  });

  it("drawer notes persist to localStorage under the documented key", async () => {
    const { app, window } = await initApp();
    const ctrl = app.data.controls.find((c) => c.id === "1.2");
    app.setDrawerNotes(ctrl.id, "my workshop jot");
    expect(window.localStorage.getItem("fsi-copilotgov:notes:1.2")).toBe("my workshop jot");
    expect(app.getDrawerNotes(ctrl.id)).toBe("my workshop jot");
    app.setDrawerNotes(ctrl.id, "");
    expect(window.localStorage.getItem("fsi-copilotgov:notes:1.2")).toBeNull();
  });
});
