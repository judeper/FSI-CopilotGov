// Shared bootstrap helper for H2 SPA tests. Boots the assessment SPA inside
// a jsdom realm, stubs fetch against on-disk manifests, and returns a ready-
// to-use `{ app, window, document, exports }` tuple.
import { JSDOM } from "jsdom";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const REPO = join(here, "..", "..");
export const SPA_PATH = join(REPO, "docs", "javascripts", "assessment-app.js");
export const MANIFEST_PATH = join(REPO, "assessment", "manifest", "controls.json");
export const LOCK_PATH = join(REPO, "assessment", "data", "solutions-lock.json");
export const DATA_PATH = join(REPO, "docs", "javascripts", "assessment-data.json");

export function bootstrap() {
  const dom = new JSDOM(
    '<!DOCTYPE html><html><body><div id="assessment-app" class="assessment-container"></div></body></html>',
    { url: "http://localhost/" },
  );
  const { window } = dom;
  // jsdom lacks scrollIntoView — stub as a no-op so facilitator "next control"
  // navigation does not throw inside tests.
  window.HTMLElement.prototype.scrollIntoView = function () {};
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

export async function initApp({ step = "phase1", sector = "bank", facilitator = false } = {}) {
  const { window, document, mod } = bootstrap();
  if (facilitator) window.localStorage.setItem("fsi-copilotgov:facilitator-mode", "1");
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
  app.facilitatorMode = window.localStorage.getItem("fsi-copilotgov:facilitator-mode") === "1";
  app.state = {
    schemaVersion: 2,
    assessmentId: "test-h2",
    scoping: { zones: [1, 2, 3], targetLevel: "recommended", sector },
    selectedSector: sector,
    responses: {},
    completedSteps: [],
    overrides: {},
  };
  app.step = step;
  app.render();
  return { app, window, document, exports: mod.exports };
}
