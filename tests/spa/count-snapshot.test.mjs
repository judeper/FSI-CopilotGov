// Phase E3: count snapshot — keep manifest, content-graph, and SPA data file
// in lock-step. Catches drift the moment any one of them is regenerated
// without the others.
import { describe, it, expect } from "vitest";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const REPO = join(here, "..", "..");

const MANIFEST = JSON.parse(
  readFileSync(join(REPO, "assessment", "manifest", "controls.json"), "utf8")
);
const GRAPH = JSON.parse(
  readFileSync(join(REPO, "assessment", "manifest", "content-graph.json"), "utf8")
);
const DATA = JSON.parse(
  readFileSync(join(REPO, "docs", "javascripts", "assessment-data.json"), "utf8")
);

describe("count snapshot — manifest / content-graph / SPA data agree", () => {
  it("manifest length equals content-graph counts.controls", () => {
    expect(MANIFEST.length).toBe(GRAPH.counts.controls);
  });

  it("SPA data file controls.length equals manifest length", () => {
    expect(DATA.controls.length).toBe(MANIFEST.length);
  });

  it("SPA data totalControls equals controls array length", () => {
    expect(DATA.totalControls).toBe(DATA.controls.length);
  });

  it("content-graph reports exactly 4 pillars", () => {
    expect(GRAPH.counts.pillars).toBe(4);
  });

  it("playbooks_total equals control + cross-cutting subtotals", () => {
    const c = GRAPH.counts;
    expect(c.playbooks_total).toBe(c.playbooks_control + c.playbooks_cross_cutting);
  });

  it("every manifest pillar value is in {1,2,3,4}", () => {
    for (const ctrl of MANIFEST) {
      expect([1, 2, 3, 4]).toContain(ctrl.pillar);
    }
  });

  it("per-pillar control counts match expected distribution (16/17/15/14)", () => {
    const byPillar = MANIFEST.reduce((acc, c) => {
      acc[c.pillar] = (acc[c.pillar] || 0) + 1;
      return acc;
    }, {});
    expect(byPillar[1]).toBe(16);
    expect(byPillar[2]).toBe(17);
    expect(byPillar[3]).toBe(15);
    expect(byPillar[4]).toBe(14);
  });
});
