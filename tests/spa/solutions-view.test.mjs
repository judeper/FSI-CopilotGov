// H2: Deeper tests for the Solutions catalog view (C3).
import { describe, it, expect } from "vitest";
import { initApp } from "./_bootstrap.mjs";

async function init() { return initApp({ step: "solutions" }); }

describe("solutions catalog view (edge cases)", () => {
  it("renders all 20 solutions as catalog cards with a coverage badge each", async () => {
    const { document } = await init();
    const cards = document.querySelectorAll(".solution-catalog-card");
    expect(cards.length).toBe(20);
    cards.forEach((c) => {
      expect(c.querySelector(".solution-catalog-coverage")).not.toBeNull();
      expect(c.getAttribute("data-solution-id")).toBeTruthy();
    });
  });

  it("tier chips narrow to exactly the tier's solutions and empty-search shows all 20", async () => {
    const { document } = await init();
    const t1 = document.querySelector('.solutions-filter-chip[data-filter-tier="1"]');
    t1.click();
    const tier1Cards = document.querySelectorAll(".solution-catalog-card");
    expect(tier1Cards.length).toBeGreaterThan(0);
    expect(tier1Cards.length).toBeLessThan(20);
    tier1Cards.forEach((c) => {
      expect(c.querySelector(".tier-1")).not.toBeNull();
    });
    // Reset.
    document.querySelector('.solutions-filter-chip[data-filter-tier="all"]').click();
    expect(document.querySelectorAll(".solution-catalog-card").length).toBe(20);
  });

  it("tier + domain filters compose (intersection)", async () => {
    const { app, document } = await init();
    const tier1 = document.querySelector('.solutions-filter-chip[data-filter-tier="1"]');
    tier1.click();
    const tier1Count = document.querySelectorAll(".solution-catalog-card").length;
    // Pick a domain that has at least one tier-1 solution for a non-empty intersection.
    const lock = app.solutionsLock;
    const anyTier1 = lock.solutions.find((s) => s.tier === 1);
    expect(anyTier1).toBeTruthy();
    const dom = anyTier1.domain;
    const domBtn = document.querySelector(`.solutions-filter-chip[data-filter-domain="${dom}"]`);
    expect(domBtn).not.toBeNull();
    domBtn.click();
    const both = document.querySelectorAll(".solution-catalog-card");
    expect(both.length).toBeGreaterThan(0);
    expect(both.length).toBeLessThanOrEqual(tier1Count);
    // Every visible card must belong to the chosen tier AND domain.
    both.forEach((card) => {
      const sid = card.getAttribute("data-solution-id");
      const s = lock.solutions.find((x) => x.id === sid);
      expect(s.tier).toBe(1);
      expect(s.domain).toBe(dom);
    });
  });

  it("search filters by id, name, and summary (case-insensitive substring)", async () => {
    const { app } = await init();
    // Drive filtering through the internal filter object + render to avoid
    // the debounced input handler.
    const f = app._getSolutionsFilter();
    // Search by known slug fragment.
    f.search = "READINESS";
    app.render();
    let cards = app.el.querySelectorAll(".solution-catalog-card");
    expect(cards.length).toBeGreaterThanOrEqual(1);
    const ids = Array.from(cards).map((c) => c.getAttribute("data-solution-id"));
    expect(ids.some((id) => id.includes("readiness"))).toBe(true);
    // Search by a term that should hit nothing.
    f.search = "zzz-no-match-xyz";
    app.render();
    cards = app.el.querySelectorAll(".solution-catalog-card");
    expect(cards.length).toBe(0);
    // Reset.
    f.search = "";
    app.render();
    cards = app.el.querySelectorAll(".solution-catalog-card");
    expect(cards.length).toBe(20);
  });

  it("reverse-lookup for 01-copilot-readiness-scanner returns ≥ 1 controls with well-formed ids", async () => {
    const { app } = await init();
    const controls = app.getControlsForSolution("01-copilot-readiness-scanner");
    expect(controls.length).toBeGreaterThanOrEqual(1);
    controls.forEach((c) => {
      expect(c.id).toMatch(/^[1-4]\.\d+$/);
      expect([1, 2, 3, 4]).toContain(c.pillar);
    });
  });

  it("coverage badge count matches getControlsForSolution length for every card", async () => {
    const { app, document } = await init();
    const cards = document.querySelectorAll(".solution-catalog-card");
    cards.forEach((card) => {
      const sid = card.getAttribute("data-solution-id");
      const badge = card.querySelector(".solution-catalog-coverage");
      const expected = String(app.getControlsForSolution(sid).length);
      expect(badge.getAttribute("data-coverage-count"), `coverage ${sid}`).toBe(expected);
      expect(badge.textContent).toMatch(/Covers \d+ of 58/);
    });
  });

  it("unknown solution id returns an empty control list (no throw)", async () => {
    const { app } = await init();
    expect(app.getControlsForSolution("does-not-exist")).toEqual([]);
    expect(app.getControlsForSolution("")).toEqual([]);
    expect(app.getControlsForSolution(null)).toEqual([]);
  });
});
