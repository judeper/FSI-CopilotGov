// H2: Edge-case tests for the evidence drawer.
import { describe, it, expect } from "vitest";
import { initApp } from "./_bootstrap.mjs";

describe("drawer edge cases", () => {
  it("closes on Escape keydown inside the drawer", async () => {
    const { app, window, document } = await initApp();
    const ctrl = app.data.controls.find((c) => c.id === "1.2");
    app.openDrawer(ctrl);
    expect(document.querySelector(".control-drawer.open")).not.toBeNull();
    const drawer = document.querySelector(".control-drawer");
    const evt = new window.KeyboardEvent("keydown", { key: "Escape", bubbles: true });
    drawer.dispatchEvent(evt);
    expect(document.querySelector(".control-drawer.open")).toBeNull();
  });

  it("persists notes under fsi-copilotgov:notes:<id> and getDrawerNotes returns them", async () => {
    const { app, window } = await initApp();
    app.setDrawerNotes("2.1", "line one\nline two\n  indented");
    expect(window.localStorage.getItem("fsi-copilotgov:notes:2.1"))
      .toBe("line one\nline two\n  indented");
    expect(app.getDrawerNotes("2.1")).toBe("line one\nline two\n  indented");
  });

  it("notes survive a simulated page reload (new AssessmentApp instance)", async () => {
    const { app, window, exports } = await initApp();
    app.setDrawerNotes("3.1", "survives reload");
    // Same localStorage survives; new AssessmentApp constructed in same jsdom
    // realm should read the same key.
    const { AssessmentApp } = exports;
    const app2 = new AssessmentApp(window.document.getElementById("assessment-app"));
    expect(app2.getDrawerNotes("3.1")).toBe("survives reload");
  });

  it("preserves multi-line note content verbatim through a render cycle", async () => {
    const { app, document } = await initApp();
    const ctrl = app.data.controls.find((c) => c.id === "1.2");
    const blob = "Row 1: DLP enabled\nRow 2: 12 policies\n\nFinal row.";
    app.setDrawerNotes(ctrl.id, blob);
    app.openDrawer(ctrl);
    const textarea = document.getElementById("control-drawer-notes-1.2");
    expect(textarea).not.toBeNull();
    expect(textarea.value).toBe(blob);
  });

  it("rapid open/close/open does not leak drawer DOM nodes", async () => {
    const { app, document } = await initApp();
    const a = app.data.controls.find((c) => c.id === "1.2");
    const b = app.data.controls.find((c) => c.id === "2.1");
    for (let i = 0; i < 5; i++) {
      app.openDrawer(a);
      app.closeDrawer();
      app.openDrawer(b);
      app.closeDrawer();
    }
    // Exactly one drawer root + one backdrop must exist (singleton).
    expect(document.querySelectorAll(".control-drawer").length).toBe(1);
    expect(document.querySelectorAll(".control-drawer-backdrop").length).toBe(1);
    expect(document.querySelector(".control-drawer.open")).toBeNull();
  });

  it("TODO-field control opens drawer with pending placeholder, no undefined leaks", async () => {
    const { app, document } = await initApp();
    // 1.1 is a TODO-evidence control (authored sample tested in D1).
    const todoIds = ["1.1", "2.2", "3.2", "4.2"];
    for (const id of todoIds) {
      const ctrl = app.data.controls.find((c) => c.id === id);
      expect(ctrl, `control ${id}`).toBeTruthy();
      app.openDrawer(ctrl);
      const drawer = document.querySelector(".control-drawer.open");
      expect(drawer, `drawer open for ${id}`).not.toBeNull();
      const lower = drawer.textContent.toLowerCase();
      expect(lower, `no 'undefined' leak in ${id}`).not.toContain("undefined");
      expect(drawer.textContent, `no raw TODO leak in ${id}`).not.toMatch(/^\s*TODO:/m);
      app.closeDrawer();
    }
  });

  it("notes textarea has the documented per-control id attribute", async () => {
    const { app, document } = await initApp();
    const ctrl = app.data.controls.find((c) => c.id === "4.1");
    app.openDrawer(ctrl);
    const textarea = document.getElementById("control-drawer-notes-4.1");
    expect(textarea).not.toBeNull();
    expect(textarea.getAttribute("aria-label")).toContain("4.1");
  });
});
