// Phase C3 smoke test — SPA Solutions catalog view.
// - Renders 20 solution cards (from solutions-lock.json — sister catalog
//   currently lists both 19-* slug variants; tracked as a follow-up).
// - Click a card → detail panel with control reverse-lookup
// - Reverse lookup accurate: solution 01-copilot-readiness-scanner covers ≥ 2 controls
// - Tier filter narrows the visible list

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
    assessmentId: "test-c3",
    scoping: { zones: [1, 2, 3], targetLevel: "recommended" },
    responses: {},
    completedSteps: [],
  };
  app.step = "solutions";
  app.render();
  return { app, window, document, exports: mod.exports };
}

describe("Phase C3 SPA solutions catalog", () => {
  it("renders the 🧩 Solutions side-nav button", async () => {
    const { document } = await initApp();
    const btn = document.getElementById("solutions-nav-btn");
    expect(btn).not.toBeNull();
    expect(btn.textContent).toContain("Solutions");
  });

  it("solutions view renders 20 catalog cards", async () => {
    const { document } = await initApp();
    const cards = document.querySelectorAll(".solution-catalog-card");
    expect(cards.length).toBe(20);
  });

  it("reverse-lookup: 01-copilot-readiness-scanner covers ≥ 2 controls", async () => {
    const { app } = await initApp();
    const controls = app.getControlsForSolution("01-copilot-readiness-scanner");
    expect(controls.length).toBeGreaterThanOrEqual(2);
    controls.forEach((c) => expect(c.id).toMatch(/^[1-4]\.\d+$/));
  });

  it("clicking a solution card opens the detail panel with control list", async () => {
    const { app, document } = await initApp();
    const card = document.querySelector('.solution-catalog-card[data-solution-id="01-copilot-readiness-scanner"]');
    expect(card).not.toBeNull();
    card.click();
    const panel = document.querySelector(".solution-detail-panel");
    expect(panel).not.toBeNull();
    const links = panel.querySelectorAll(".solution-detail-control-link");
    expect(links.length).toBeGreaterThanOrEqual(2);
    // Each link should include a control id token like "1.1 — ...".
    const firstText = links[0].textContent;
    expect(firstText).toMatch(/^[1-4]\.\d+ /);
    // Clicking again should deselect (toggle behavior).
    card.click();
    expect(document.querySelector(".solution-detail-panel")).toBeNull();
    void app;
  });

  it("tier filter narrows the visible list", async () => {
    const { document } = await initApp();
    const allCards = document.querySelectorAll(".solution-catalog-card");
    expect(allCards.length).toBe(20);
    const tier1Btn = document.querySelector('.solutions-filter-chip[data-filter-tier="1"]');
    expect(tier1Btn).not.toBeNull();
    tier1Btn.click();
    const tier1Cards = document.querySelectorAll(".solution-catalog-card");
    expect(tier1Cards.length).toBeLessThan(allCards.length);
    expect(tier1Cards.length).toBeGreaterThan(0);
    // Every visible card should be a tier-1 card.
    tier1Cards.forEach((c) => {
      expect(c.querySelector(".tier-1")).not.toBeNull();
    });
    // Reset to All.
    document.querySelector('.solutions-filter-chip[data-filter-tier="all"]').click();
    expect(document.querySelectorAll(".solution-catalog-card").length).toBe(20);
  });

  it("coverage badge reflects reverse-lookup count", async () => {
    const { document, app } = await initApp();
    const card = document.querySelector('.solution-catalog-card[data-solution-id="01-copilot-readiness-scanner"]');
    const badge = card.querySelector(".solution-catalog-coverage");
    expect(badge).not.toBeNull();
    const actual = app.getControlsForSolution("01-copilot-readiness-scanner").length;
    expect(badge.getAttribute("data-coverage-count")).toBe(String(actual));
    expect(badge.textContent).toMatch(/Covers \d+ of 58/);
  });
});
