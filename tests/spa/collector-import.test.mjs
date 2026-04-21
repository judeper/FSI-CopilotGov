// H2: Deeper collector-import tests — malformed CSV, unknown statuses,
// clear-preserves-manual-answers, multi-import accumulation, empty file.
import { describe, it, expect } from "vitest";
import { bootstrap, initApp } from "./_bootstrap.mjs";

function captureWarnings(fn) {
  const warnings = [];
  const prev = console.warn;
  console.warn = (...args) => warnings.push(args.join(" "));
  try { const r = fn(); return { result: r, warnings }; }
  finally { console.warn = prev; }
}

describe("collector import (edge cases)", () => {
  it("CSV with malformed row (missing columns) skips the bad row but applies valid rows", () => {
    const { mod } = bootstrap();
    const { parseCollectorCsv } = mod.exports;
    const csv = [
      "control_id,evidence_key,status,raw_value,collected_at",
      "1.2,purview.dlp,pass,12 policies,2026-04-21",
      ",,,,", // blank — dropped by trim()
      "2.1,entra.ca,partial,3 of 5,2026-04-21",
    ].join("\n");
    const map = parseCollectorCsv(csv);
    expect(Object.keys(map).sort()).toEqual(["1.2", "2.1"]);
    expect(map["1.2"].status).toBe("yes");
    expect(map["2.1"].status).toBe("partial");
  });

  it("CSV with unknown status warns and leaves the mapped status as null", () => {
    const { mod } = bootstrap();
    const { parseCollectorCsv } = mod.exports;
    const { result: map, warnings } = captureWarnings(() => parseCollectorCsv(
      "control_id,evidence_key,status,raw_value,collected_at\n" +
      "1.2,key,banana,raw,2026-04-21\n" +
      "2.1,key,pass,raw,2026-04-21"
    ));
    expect(map["1.2"].status).toBeNull();
    expect(map["1.2"].evidence).toHaveLength(1);
    expect(map["2.1"].status).toBe("yes");
    expect(warnings.some((w) => w.includes("unknown status 'banana'"))).toBe(true);
  });

  it("CSV missing the control_id header yields an empty map and a warning", () => {
    const { mod } = bootstrap();
    const { parseCollectorCsv } = mod.exports;
    const { result: map, warnings } = captureWarnings(() => parseCollectorCsv(
      "evidence_key,status,raw_value\nk,pass,r"
    ));
    expect(map).toEqual({});
    expect(warnings.some((w) => w.includes("missing required control_id"))).toBe(true);
  });

  it("empty file (header only, no data rows) produces a no-op, no error", () => {
    const { mod } = bootstrap();
    const { parseCollectorCsv } = mod.exports;
    expect(parseCollectorCsv("")).toEqual({});
    expect(parseCollectorCsv("control_id,evidence_key,status,raw_value,collected_at")).toEqual({});
    // Whitespace-only / comment-only input is also a no-op.
    expect(parseCollectorCsv("\n\n# comment\n  \n")).toEqual({});
  });

  it("JSON array import produces the same map shape as CSV import", () => {
    const { mod } = bootstrap();
    const { parseCollectorCsv, parseCollectorJson } = mod.exports;
    const csvMap = parseCollectorCsv(
      "control_id,evidence_key,status,raw_value,collected_at\n" +
      "1.2,k,pass,r,2026-04-21"
    );
    const jsonMap = parseCollectorJson(JSON.stringify([
      { control_id: "1.2", evidence_key: "k", status: "pass", raw_value: "r", collected_at: "2026-04-21" },
    ]));
    expect(jsonMap["1.2"].status).toBe(csvMap["1.2"].status);
    expect(jsonMap["1.2"].evidence[0].key).toBe(csvMap["1.2"].evidence[0].key);
    expect(jsonMap["1.2"].evidence[0].raw).toBe(csvMap["1.2"].evidence[0].raw);
  });

  it("clearCollectorEvidence preserves manual notes on untouched controls", async () => {
    const { app } = await initApp();
    // Manual answer/notes on 4.1 that is NOT part of the import.
    app.state.responses["4.1"] = { answer: "yes", notes: "manual-only row" };
    app.applyCollectorEvidence({
      "1.2": { status: "yes", evidence: [{ key: "k", raw: "r", collectedAt: "t", status: "yes" }] },
    }, "run-preserve.csv");
    expect(app.state.responses["1.2"].answer).toBe("yes");
    app.clearCollectorEvidence();
    // 4.1 untouched by import; its manual answer and notes must survive.
    expect(app.state.responses["4.1"].answer).toBe("yes");
    expect(app.state.responses["4.1"].notes).toBe("manual-only row");
  });

  it("multiple sequential imports with different run-ids both persist in localStorage", async () => {
    const { app, window } = await initApp();
    app.applyCollectorEvidence({
      "1.2": { status: "yes", evidence: [{ key: "a", raw: "r", collectedAt: "t", status: "yes" }] },
    }, "run-A.csv");
    app.applyCollectorEvidence({
      "2.1": { status: "partial", evidence: [{ key: "b", raw: "r", collectedAt: "t", status: "partial" }] },
    }, "run-B.csv");
    expect(window.localStorage.getItem("fsi-copilotgov:collector-evidence:run-A.csv")).not.toBeNull();
    expect(window.localStorage.getItem("fsi-copilotgov:collector-evidence:run-B.csv")).not.toBeNull();
    // Current runId is the most recent.
    expect(app.state.collectorRunId).toBe("run-B.csv");
    // Both controls' evidence is present in state.
    expect(app.state.collectorEvidence["1.2"]).toBeDefined();
    expect(app.state.collectorEvidence["2.1"]).toBeDefined();
  });

  it("re-import overwrites same control's prior evidence without losing others", async () => {
    const { app } = await initApp();
    app.applyCollectorEvidence({
      "1.2": { status: "yes", evidence: [{ key: "old", raw: "r1", collectedAt: "t1", status: "yes" }] },
    }, "first.csv");
    app.applyCollectorEvidence({
      "1.2": { status: "partial", evidence: [{ key: "new", raw: "r2", collectedAt: "t2", status: "partial" }] },
      "3.1": { status: "no", evidence: [{ key: "x", raw: "r3", collectedAt: "t3", status: "no" }] },
    }, "second.csv");
    expect(app.state.collectorEvidence["1.2"].evidence).toHaveLength(1);
    expect(app.state.collectorEvidence["1.2"].evidence[0].key).toBe("new");
    expect(app.state.collectorEvidence["1.2"].status).toBe("partial");
    expect(app.state.collectorEvidence["3.1"].status).toBe("no");
    expect(app.state.responses["1.2"].answer).toBe("partial");
    expect(app.state.responses["3.1"].answer).toBe("no");
  });
});
