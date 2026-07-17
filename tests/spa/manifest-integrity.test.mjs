// H2: Expanded manifest / solutions-lock integrity tests.
import { describe, it, expect } from "vitest";
import { readFileSync, existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const REPO = join(here, "..", "..");
const MANIFEST_PATH = join(REPO, "assessment", "manifest", "controls.json");
const LOCK_PATH = join(REPO, "assessment", "data", "solutions-lock.json");
const GRAPH_PATH = join(REPO, "assessment", "manifest", "content-graph.json");

describe("manifest + solutions-lock integrity (H2)", () => {
  const manifest = JSON.parse(readFileSync(MANIFEST_PATH, "utf8"));
  const lock = JSON.parse(readFileSync(LOCK_PATH, "utf8"));
  const graph = JSON.parse(readFileSync(GRAPH_PATH, "utf8"));

  it("manifest control count matches content-graph and every control has core fields", () => {
    expect(manifest.length).toBe(graph.counts.controls);
    const required = ["id", "title", "pillar", "zonesApplicable", "automation", "solutions"];
    for (const c of manifest) {
      for (const field of required) {
        expect(c, `control ${c && c.id} missing ${field}`).toHaveProperty(field);
      }
      expect(c.title.length).toBeGreaterThan(0);
      expect([1, 2, 3, 4]).toContain(c.pillar);
      expect(Array.isArray(c.solutions)).toBe(true);
      expect(Array.isArray(c.zonesApplicable)).toBe(true);
    }
  });

  it("every solutions[] id resolves to an entry in solutions-lock.json", () => {
    const lockIds = new Set((lock.solutions || []).map((s) => s.id));
    expect(lockIds.size).toBeGreaterThan(0);
    for (const c of manifest) {
      for (const s of c.solutions) {
        const sid = typeof s === "string" ? s : s && s.id;
        expect(sid, `missing id on solution entry in ${c.id}`).toBeTruthy();
        expect(lockIds.has(sid), `${c.id} references unknown solution '${sid}'`).toBe(true);
      }
    }
  });

  it("no control has duplicate solution ids in its solutions[] array", () => {
    for (const c of manifest) {
      const ids = c.solutions.map((s) => (typeof s === "string" ? s : s && s.id)).filter(Boolean);
      const dupes = ids.filter((id, i) => ids.indexOf(id) !== i);
      expect(dupes, `duplicate solution ids in ${c.id}: ${dupes.join(", ")}`).toEqual([]);
    }
  });

  it("every sectorYesBar (when authored) is a map keyed by FSI sector", () => {
    const allowedSectors = new Set([
      "bank", "broker-dealer", "credit-union",
      "insurance-carrier", "investment-adviser", "other",
    ]);
    for (const c of manifest) {
      if (!c.sectorYesBar) continue;
      expect(typeof c.sectorYesBar, `${c.id} sectorYesBar type`).toBe("object");
      const keys = Object.keys(c.sectorYesBar);
      expect(keys.length, `${c.id} sectorYesBar empty`).toBeGreaterThan(0);
      for (const k of keys) {
        expect(allowedSectors.has(k), `${c.id} unknown sector '${k}'`).toBe(true);
        // Value is a string (TODO token allowed; language-rules script gates).
        expect(typeof c.sectorYesBar[k]).toBe("string");
      }
    }
  });

  it("solutions-lock has unique ids and every solution has tier ∈ {1,2,3}", () => {
    const solutions = lock.solutions || [];
    const ids = solutions.map((s) => s.id);
    expect(new Set(ids).size).toBe(ids.length);
    for (const s of solutions) {
      expect([1, 2, 3], `tier for ${s.id}`).toContain(s.tier);
      expect(typeof s.name).toBe("string");
      expect(s.name.length).toBeGreaterThan(0);
    }
  });

  it("solutions-lock source metadata ships a ref and a 40-char commit", () => {
    expect(lock.source).toBeTruthy();
    expect(typeof lock.source.ref).toBe("string");
    expect(lock.source.ref.length).toBeGreaterThan(0);
    expect(typeof lock.source.commit).toBe("string");
    expect(lock.source.commit).toMatch(/^[0-9a-f]{40}$/);
  });

  it("every portalPlaybookUrl resolves to an existing portal-walkthrough on disk (no broken route)", () => {
    // Regression guard for controls/3.8a: its manifest route pointed at a
    // nonexistent /3.8a/portal-walkthrough/ playbook. Every control's playbook
    // route must map to a real docs/playbooks/.../portal-walkthrough.md file.
    const routeRe =
      /^\/playbooks\/control-implementations\/([^/]+)\/portal-walkthrough\/?$/;
    for (const c of manifest) {
      const url = c.portalPlaybookUrl;
      const m = typeof url === "string" ? url.match(routeRe) : null;
      expect(
        m,
        `${c.id} portalPlaybookUrl '${url}' is not a control-implementations portal-walkthrough route`,
      ).toBeTruthy();
      const file = join(
        REPO,
        "docs",
        "playbooks",
        "control-implementations",
        m[1],
        "portal-walkthrough.md",
      );
      expect(existsSync(file), `${c.id} portalPlaybookUrl points to missing file ${file}`).toBe(true);
    }
  });

  it("co-dependent controls 3.8 and 3.8a carry concrete accountable roles (no TODO placeholder)", () => {
    // Reconciliation guard: 3.8a shipped with a ["TODO: assign per ROLE_CONTROLS"]
    // placeholder. Both halves of the co-dependent MRM pair must name real roles.
    for (const id of ["3.8", "3.8a"]) {
      const c = manifest.find((x) => x.id === id);
      expect(c, `control ${id} missing from manifest`).toBeTruthy();
      expect(Array.isArray(c.roles) && c.roles.length > 0, `${id} roles must be non-empty`).toBe(true);
      for (const r of c.roles) {
        expect(typeof r).toBe("string");
        expect(
          r.toLowerCase().startsWith("todo"),
          `${id} still carries a TODO role placeholder: '${r}'`,
        ).toBe(false);
      }
    }
  });

  it("every control id is unique and matches the documented pillar.index pattern", () => {
    const ids = manifest.map((c) => c.id);
    expect(new Set(ids).size).toBe(ids.length);
    for (const id of ids) {
      expect(id).toMatch(/^[1-4]\.\d+[a-z]?$/);
    }
  });
});
