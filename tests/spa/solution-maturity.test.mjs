// Issue #257: per-control solution cards must disclose solution maturity, so a
// documentation-first scaffold is not mistaken for shipped tooling.
import { describe, it, expect } from "vitest";
import { initApp } from "./_bootstrap.mjs";

describe("solution maturity disclosure on control cards", () => {
  it("renders a maturity chip on every mapped per-control solution card", async () => {
    const { app } = await initApp();
    const mapped = app.manifest.find(
      (m) => Array.isArray(m.solutions) && m.solutions.length,
    );
    expect(mapped).toBeTruthy();

    const wrap = app.renderSolutionCards({ id: mapped.id });
    const cards = wrap.querySelectorAll(".solution-card");
    expect(cards.length).toBe(mapped.solutions.length);

    cards.forEach((card) => {
      const id = card.getAttribute("data-solution-id");
      const entry = app.solutionsLockById[id];
      if (!entry || typeof entry.maturity !== "string") return;
      const chip = card.querySelector(".solution-maturity");
      expect(chip, `no maturity chip for ${id}`).not.toBeNull();
      expect(chip.getAttribute("data-maturity")).toBe(entry.maturity);
      expect(chip.textContent).toBe(entry.maturity.replace(/-/g, " "));
    });
  });

  it("omits the chip when the locked entry carries no maturity", async () => {
    const { app } = await initApp();
    const mapped = app.manifest.find(
      (m) => Array.isArray(m.solutions) && m.solutions.length,
    );
    const id = mapped.solutions[0].id || mapped.solutions[0];
    const original = app.solutionsLockById[id];
    app.solutionsLockById[id] = Object.assign({}, original);
    delete app.solutionsLockById[id].maturity;

    const wrap = app.renderSolutionCards({ id: mapped.id });
    const card = wrap.querySelector(`.solution-card[data-solution-id="${id}"]`);
    expect(card.querySelector(".solution-maturity")).toBeNull();

    app.solutionsLockById[id] = original;
  });

  it("keeps every locked solution honest about being documentation-first", async () => {
    const { app } = await initApp();
    const allowed = ["documentation-first-scaffold", "preview", "live"];
    app.solutionsLock.solutions.forEach((s) => {
      expect(allowed).toContain(s.maturity);
    });
  });
});
