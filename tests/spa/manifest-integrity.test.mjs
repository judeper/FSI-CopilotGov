// H2: Expanded manifest / solutions-lock integrity tests.
import { describe, it, expect } from "vitest";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const REPO = join(here, "..", "..");
const MANIFEST_PATH = join(REPO, "assessment", "manifest", "controls.json");
const LOCK_PATH = join(REPO, "assessment", "data", "solutions-lock.json");

describe("manifest + solutions-lock integrity (H2)", () => {
  const manifest = JSON.parse(readFileSync(MANIFEST_PATH, "utf8"));
  const lock = JSON.parse(readFileSync(LOCK_PATH, "utf8"));

  it("all 58 controls have the required core fields", () => {
    expect(manifest.length).toBe(58);
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
      "bank", "broker-dealer", "credit-union", "holding-company",
      "insurance-carrier", "insurance-wholesale", "investment-adviser", "other",
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

  it("every control id is unique and matches the documented pillar.index pattern", () => {
    const ids = manifest.map((c) => c.id);
    expect(new Set(ids).size).toBe(ids.length);
    for (const id of ids) {
      expect(id).toMatch(/^[1-4]\.\d+$/);
    }
  });
});
