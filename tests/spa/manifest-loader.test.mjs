import { describe, it, expect } from "vitest";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const MANIFEST_PATH = join(here, "..", "..", "assessment", "manifest", "controls.json");

// FSI-CopilotGov ships 62 controls (16/17/15/14 across pillars 1-4).
const EXPECTED_CONTROL_COUNT = 62;
const EXPECTED_PER_PILLAR = { 1: 16, 2: 17, 3: 15, 4: 14 };

describe("manifest/controls.json", () => {
  const manifest = JSON.parse(readFileSync(MANIFEST_PATH, "utf8"));

  it(`contains exactly ${EXPECTED_CONTROL_COUNT} controls`, () => {
    expect(Array.isArray(manifest)).toBe(true);
    expect(manifest.length).toBe(EXPECTED_CONTROL_COUNT);
  });

  it("matches the expected per-pillar distribution", () => {
    const counts = { 1: 0, 2: 0, 3: 0, 4: 0 };
    for (const c of manifest) counts[c.pillar] = (counts[c.pillar] || 0) + 1;
    expect(counts).toEqual(EXPECTED_PER_PILLAR);
  });

  it("every control has id, title, pillar, and a solutions array", () => {
    for (const c of manifest) {
      expect(typeof c.id, `id for ${JSON.stringify(c).slice(0, 80)}`).toBe("string");
      expect(c.id).toMatch(/^[1-4]\.\d+[a-z]?$/);
      expect(typeof c.title, `title for ${c.id}`).toBe("string");
      expect(c.title.length).toBeGreaterThan(0);
      expect([1, 2, 3, 4]).toContain(c.pillar);
      // Solutions array must exist (Phase C will populate values).
      expect(Array.isArray(c.solutions), `solutions for ${c.id}`).toBe(true);
    }
  });

  it("every solutions[] entry (when present) is a kebab-case slug or {id, tier, role} object", () => {
    const slug = /^[a-z0-9][a-z0-9-]*$/;
    for (const c of manifest) {
      for (const s of c.solutions) {
        if (typeof s === "string") {
          expect(s, `solution slug in ${c.id}`).toMatch(slug);
        } else {
          expect(typeof s, `solution entry in ${c.id}`).toBe("object");
          expect(typeof s.id, `solution.id in ${c.id}`).toBe("string");
          expect(s.id, `solution.id slug in ${c.id}`).toMatch(slug);
          if (s.tier !== undefined) {
            expect([1, 2, 3], `solution.tier in ${c.id}`).toContain(s.tier);
          }
          if (s.role !== undefined) {
            expect(["primary", "supporting"], `solution.role in ${c.id}`).toContain(s.role);
          }
        }
      }
    }
  });

  it("every control has zonesApplicable as a non-empty subset of [1,2,3]", () => {
    for (const c of manifest) {
      expect(Array.isArray(c.zonesApplicable), `zonesApplicable for ${c.id}`).toBe(true);
      expect(c.zonesApplicable.length).toBeGreaterThan(0);
      for (const z of c.zonesApplicable) {
        expect([1, 2, 3]).toContain(z);
      }
      expect(new Set(c.zonesApplicable).size).toBe(c.zonesApplicable.length);
    }
  });

  it("every control has automation in {full, partial, manual}", () => {
    const allowed = new Set(["full", "partial", "manual"]);
    for (const c of manifest) {
      expect(allowed.has(c.automation), `automation for ${c.id}`).toBe(true);
    }
  });

  it("control IDs are unique", () => {
    const ids = manifest.map((c) => c.id);
    expect(new Set(ids).size).toBe(ids.length);
  });
});
