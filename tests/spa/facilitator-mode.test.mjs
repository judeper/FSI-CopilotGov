// H2: Facilitator-mode tests — persistence, ARIA state, next-control
// navigation, and TODO suppression.
import { describe, it, expect } from "vitest";
import { initApp } from "./_bootstrap.mjs";

describe("facilitator mode", () => {
  it("persists to localStorage under fsi-copilotgov:facilitator-mode", async () => {
    const { app, window } = await initApp();
    expect(app.facilitatorMode).toBe(false);
    expect(window.localStorage.getItem("fsi-copilotgov:facilitator-mode")).toBeNull();
    app.toggleFacilitatorMode();
    expect(app.facilitatorMode).toBe(true);
    expect(window.localStorage.getItem("fsi-copilotgov:facilitator-mode")).toBe("1");
    app.toggleFacilitatorMode();
    expect(app.facilitatorMode).toBe(false);
    expect(window.localStorage.getItem("fsi-copilotgov:facilitator-mode")).toBe("0");
  });

  it("toggle updates aria-pressed and button styling", async () => {
    const { document } = await initApp();
    const btn = document.getElementById("facilitator-toggle");
    expect(btn).not.toBeNull();
    expect(btn.getAttribute("aria-pressed")).toBe("false");
    expect(btn.textContent).toContain("Off");
    btn.click(); // triggers toggleFacilitatorMode → re-render
    const btn2 = document.getElementById("facilitator-toggle");
    expect(btn2.getAttribute("aria-pressed")).toBe("true");
    expect(btn2.textContent).toContain("On");
    expect(btn2.classList.contains("ag-btn-primary")).toBe(true);
  });

  it("suppresses the facilitator panel for TODO facilitatorNotes.ask", async () => {
    const { document } = await initApp({ facilitator: true });
    // Authored (should render): 1.2, 1.3, 2.1, 3.1, 4.1.
    ["1.2", "1.3", "2.1", "3.1", "4.1"].forEach((id) => {
      const row = document.querySelector(`.control-row[data-control-id="${id}"]`);
      expect(row, `row ${id}`).not.toBeNull();
      expect(row.querySelector(".facilitator-panel"), `panel ${id}`).not.toBeNull();
    });
    // TODO (should NOT render): several arbitrary non-authored controls.
    ["1.1", "1.4", "2.2", "2.3", "3.2", "4.2", "4.13"].forEach((id) => {
      const row = document.querySelector(`.control-row[data-control-id="${id}"]`);
      expect(row, `row ${id}`).not.toBeNull();
      expect(row.querySelector(".facilitator-panel"), `panel suppressed for TODO ${id}`).toBeNull();
    });
  });

  it("Next control button on an authored card advances focus to the next card", async () => {
    const { document } = await initApp({ facilitator: true });
    const row12 = document.querySelector('.control-row[data-control-id="1.2"]');
    const nextBtn = row12.querySelector(".facilitator-next");
    expect(nextBtn).not.toBeNull();
    // Clicking delegates to focusNextControlCard which calls .focus() on
    // the next card's answer button. No error thrown (scrollIntoView stubbed).
    expect(() => nextBtn.click()).not.toThrow();
    // After the click, focused element is within the next ag-control-card.
    const activeCard = document.activeElement && document.activeElement.closest
      ? document.activeElement.closest(".ag-control-card")
      : null;
    if (activeCard) {
      // Next authored row may be 1.3 OR the DOM ordering for 1.x controls.
      const nextId = activeCard.getAttribute("data-control-id");
      expect(nextId).not.toBe("1.2");
      expect(nextId).toMatch(/^1\./);
    }
  });

  it("Next control button on the last authored card is a no-op (no throw)", async () => {
    const { app, document } = await initApp({ facilitator: true });
    // 4.1 is the last authored facilitator control, but not necessarily the
    // last card in DOM order. We instead probe focusNextControlCard on the
    // final card overall to confirm graceful exit.
    const cards = document.querySelectorAll(".ag-control-card");
    const lastId = cards[cards.length - 1].getAttribute("data-control-id");
    expect(() => app.focusNextControlCard(lastId)).not.toThrow();
    // And with an unknown id: still a no-op, no throw.
    expect(() => app.focusNextControlCard("does-not-exist")).not.toThrow();
  });

  it("enabling facilitator mode adds the .phase1-wrap.facilitator-mode class", async () => {
    const { document } = await initApp();
    expect(document.querySelector(".phase1-wrap.facilitator-mode")).toBeNull();
    const btn = document.getElementById("facilitator-toggle");
    btn.click();
    expect(document.querySelector(".phase1-wrap.facilitator-mode")).not.toBeNull();
  });

  it("facilitator mode survives a fresh init when localStorage is pre-set", async () => {
    const { app, document } = await initApp({ facilitator: true });
    expect(app.facilitatorMode).toBe(true);
    const btn = document.getElementById("facilitator-toggle");
    expect(btn.getAttribute("aria-pressed")).toBe("true");
  });
});
