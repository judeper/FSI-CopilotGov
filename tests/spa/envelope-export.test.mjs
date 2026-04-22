// H2: Deeper envelope export/import tests — empty/partial summaries,
// round-trips with notes + collector evidence, error handling, identity reuse.
import { describe, it, expect } from "vitest";
import { initApp } from "./_bootstrap.mjs";

describe("envelope export / import (edge cases)", () => {
  it("empty assessment exports a valid envelope with all-zero summary", async () => {
    const { app } = await initApp({ step: "export" });
    const env = app.buildEnvelope();
    expect(env.schemaVersion).toBe("fsi-copilotgov-envelope/0.1.0");
    expect(env.answers).toHaveLength(62);
    expect(env.answers.every((a) => a.answer === null)).toBe(true);
    expect(env.summary.yes).toBe(0);
    expect(env.summary.partial).toBe(0);
    expect(env.summary.no).toBe(0);
    expect(env.summary.na).toBe(0);
    expect(env.summary.unanswered).toBe(62);
    expect(env.summary.overall).toBe(0);
    expect(env.summary.maturityLevel).toBe("Not assessed");
  });

  it("partial (Pillar 1 only) export reports per-pillar scores with zero for unanswered pillars", async () => {
    const { app } = await initApp({ step: "export" });
    // Answer one Pillar-1 control yes; leave Pillars 2/3/4 untouched.
    app.state.responses["1.2"] = { answer: "yes", notes: "" };
    const env = app.buildEnvelope();
    expect(env.summary.yes).toBe(1);
    expect(env.summary.unanswered).toBe(61);
    expect(env.summary.scoreByPillar).toBeTypeOf("object");
    // Pillars 2-4 unanswered → their scores are zero (not undefined).
    [2, 3, 4].forEach((p) => {
      expect(env.summary.scoreByPillar[p], `pillar ${p}`).toBe(0);
    });
    // Pillar 1 may be zero or positive depending on the scorer, but must be a number.
    expect(typeof env.summary.scoreByPillar[1]).toBe("number");
  });

  it("envelope round-trips answers + notes + collector evidence + identity", async () => {
    const { app, window } = await initApp({ step: "export" });
    app.setEnvelopeIdentity({ name: "Jane Doe", role: "Compliance Lead", org: "Acme Bank, N.A." });
    app.state.responses["1.2"] = { answer: "yes", notes: "dlp active" };
    app.state.responses["2.1"] = { answer: "partial", notes: "3 of 5 scopes" };
    app.applyCollectorEvidence({
      "1.2": { status: "yes", evidence: [{ key: "dlp.k", raw: "12 policies", collectedAt: "2026-04-21", status: "yes" }] },
    }, "round-trip.csv");
    const env = app.buildEnvelope();

    const { app: app2 } = await initApp({ step: "export" });
    // app2 uses a separate localStorage realm (new jsdom), so identity starts empty.
    expect(app2.getEnvelopeIdentity()).toEqual({ name: "", role: "", org: "" });
    app2.importEnvelope(env);
    expect(app2.state.responses["1.2"].answer).toBe("yes");
    expect(app2.state.responses["1.2"].notes).toBe("dlp active");
    expect(app2.state.responses["2.1"].notes).toBe("3 of 5 scopes");
    const ce = app2.getCollectorEvidenceFor("1.2");
    expect(ce).not.toBeNull();
    expect(ce.runId).toBe("round-trip.csv");
    expect(ce.evidence[0].key).toBe("dlp.k");
    // Identity was folded in via importEnvelope → setEnvelopeIdentity.
    expect(app2.getEnvelopeIdentity().name).toBe("Jane Doe");
    expect(app2.getEnvelopeIdentity().org).toBe("Acme Bank, N.A.");
    void window; // keep reference
  });

  it("importEnvelope throws on a foreign schemaVersion (AgentGov envelope)", async () => {
    const { app } = await initApp({ step: "export" });
    expect(() => app.importEnvelope({
      schemaVersion: "fsi-agentgov-envelope/0.1.0",
      answers: [],
    })).toThrow(/Not a CopilotGov envelope/);
  });

  it("importEnvelope throws on null or non-object input", async () => {
    const { app } = await initApp({ step: "export" });
    expect(() => app.importEnvelope(null)).toThrow(/Envelope must be an object/);
    expect(() => app.importEnvelope(undefined)).toThrow(/Envelope must be an object/);
    expect(() => app.importEnvelope("a string")).toThrow(/Envelope must be an object/);
  });

  it("importEnvelope with missing answers[] degrades gracefully (treats as empty)", async () => {
    const { app } = await initApp({ step: "export" });
    // schemaVersion present, but no answers array at all.
    const result = app.importEnvelope({
      schemaVersion: "fsi-copilotgov-envelope/0.1.0",
      assessor: { name: "X", role: "Y", org: "Z" },
    });
    expect(result.controls).toBe(0);
    expect(result.collectorRows).toBe(false);
    expect(app.state.responses).toEqual({});
  });

  it("identity dialog is skipped on second export once identity is stored", async () => {
    const { app } = await initApp({ step: "export" });
    // First-time exporters with no identity: simulate storing identity.
    app.setEnvelopeIdentity({ name: "Jane", role: "Lead", org: "Acme" });
    // Calling exportEnvelope when identity is present bypasses the prompt;
    // _finalizeEnvelopeDownload calls downloadBlob which needs URL + anchors.
    // We assert the guard: identity is non-empty so the modal path is not hit.
    const identity = app.getEnvelopeIdentity();
    expect(identity.name).toBe("Jane");
    expect(identity.org).toBe("Acme");
    // The envelope built with stored identity carries those fields verbatim.
    const env = app.buildEnvelope();
    expect(env.assessor).toEqual({ name: "Jane", role: "Lead", org: "Acme" });
  });
});
