// Regression guard for control 2.15: Azure Private Link must never be
// represented as a private route to the M365 Copilot SaaS service. It applies
// only to adjacent Azure resources an internal Copilot Studio agent calls.
// See issue: "Clarify Azure Private Link scope in control 2.15".
import { describe, it, expect } from "vitest";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const REPO = join(here, "..", "..");

const CONTROL_DOC = join(
  REPO, "docs", "controls", "pillar-2-security", "2.15-network-security.md",
);
const PLAYBOOK_DIR = join(
  REPO, "docs", "playbooks", "control-implementations", "2.15",
);
const PLAYBOOKS = [
  "portal-walkthrough.md",
  "powershell-setup.md",
  "verification-testing.md",
  "troubleshooting.md",
].map((f) => join(PLAYBOOK_DIR, f));
const HOMEWORK = [
  join(REPO, "docs", "getting-started", "homework-recommended.md"),
  join(REPO, "docs", "getting-started", "homework-regulated.md"),
];
const MANIFEST_PATH = join(REPO, "assessment", "manifest", "controls.json");

// Affirmative claims that (falsely) treat Private Link as a route to M365 /
// Copilot SaaS. These are phrased so they never match the corrective wording
// (e.g. "Private Link applies only to adjacent Azure resources").
const FORBIDDEN = [
  /Private Endpoints for SharePoint Online/i,
  /Azure Private Link for SharePoint/i,
  /Private network path for M365/i,
  /Test Copilot functionality (over|through) the (private|Private Link)/i,
  /GroupIds\s*-match\s*["']sharePoint\|exchange["']/i,
  /Private Link is optional but recommended/i,
  /\(Private Link, VPN/i,
];

describe("control 2.15 — Azure Private Link scope guard", () => {
  const scanned = [CONTROL_DOC, ...PLAYBOOKS, ...HOMEWORK].map((p) => ({
    path: p,
    text: readFileSync(p, "utf8"),
  }));

  it("no 2.15 doc/playbook/homework asserts Private Link is a route to M365 Copilot SaaS", () => {
    for (const { path, text } of scanned) {
      for (const re of FORBIDDEN) {
        expect(
          re.test(text),
          `${path} contains a forbidden Private-Link-for-M365 claim matching ${re}`,
        ).toBe(false);
      }
    }
  });

  it("control 2.15 keeps the note that Private Link is not available for M365 Copilot SaaS", () => {
    const text = readFileSync(CONTROL_DOC, "utf8");
    expect(
      text.includes(
        "Azure Private Link is not available for Microsoft 365 Copilot SaaS surfaces",
      ),
      "control 2.15 lost its Private Link scope clarification note",
    ).toBe(true);
    expect(
      /adjacent Azure resource/i.test(text),
      "control 2.15 should scope Private Link to adjacent Azure resources",
    ).toBe(true);
  });

  it("manifest control 2.15 does not list Private Link as a plain Copilot network control", () => {
    const manifest = JSON.parse(readFileSync(MANIFEST_PATH, "utf8"));
    const c = manifest.find((x) => x.id === "2.15");
    expect(c, "control 2.15 missing from manifest").toBeTruthy();
    for (const re of FORBIDDEN) {
      expect(
        re.test(JSON.stringify(c)),
        `manifest 2.15 contains a forbidden Private-Link-for-M365 claim matching ${re}`,
      ).toBe(false);
    }
  });
});
