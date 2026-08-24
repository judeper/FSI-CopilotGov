import { describe, it, expect } from "vitest";
import { readFileSync } from "node:fs";
import { bootstrap, LOCK_PATH } from "./_bootstrap.mjs";

const VALID_URLS = [
  "https://github.com/judeper/FSI-CopilotGov-Solutions",
  "https://github.com/judeper/FSI-CopilotGov-Solutions/",
  "https://github.com/judeper/FSI-CopilotGov-Solutions/tree/main/solutions/01",
  "https://github.com/judeper/FSI-CopilotGov-Solutions?tab=readme-ov-file#readme",
];

const INVALID_URLS = [
  "http://github.com/judeper/FSI-CopilotGov-Solutions",
  "https://user@github.com/judeper/FSI-CopilotGov-Solutions",
  "https://user:pass@github.com/judeper/FSI-CopilotGov-Solutions",
  "https://github.com:443/judeper/FSI-CopilotGov-Solutions",
  "https://github.com:444/judeper/FSI-CopilotGov-Solutions",
  "https://github.com.evil/judeper/FSI-CopilotGov-Solutions",
  "https://github.com./judeper/FSI-CopilotGov-Solutions",
  "https://GitHub.com/judeper/FSI-CopilotGov-Solutions",
  "https://github.com/judeper/a-different-repository",
  "https://github.com/judeper/FSI-CopilotGov-Solutions.evil",
  "https://github.com/judeper/FSI-CopilotGov-Solutions/../../attacker/repo",
  "https://github.com/judeper/FSI-CopilotGov-Solutions/%2e%2e/%2e%2e/attacker/repo",
  "https://github.com/judeper/FSI-CopilotGov-Solutions/%2F..%2Fattacker",
  "https://github.com/judeper/FSI-CopilotGov-Solutions/%5c..%5cattacker",
  "https://github.com/judeper/FSI-CopilotGov-Solutions\\..\\attacker",
  "https://github.com/judeper/FSI-CopilotGov-Solutions//tree/main",
  "https://github.com/judeper/FSI-CopilotGov-Solutions/тест",
  " https://github.com/judeper/FSI-CopilotGov-Solutions",
  "https://github.com/judeper/FSI-CopilotGov-Solutions ",
  "https://github.com/judeper/FSI-CopilotGov-Solutions\n.evil",
  "javascript:alert(1)",
  "data:text/html,<script>alert(1)</script>",
];

describe("solution URL security", () => {
  it("accepts only canonical URLs inside the expected GitHub repository", () => {
    const { canonicalSolutionUrl } = bootstrap().mod.exports;

    VALID_URLS.forEach((url) => {
      expect(canonicalSolutionUrl(url), url).toBe(url);
    });
    INVALID_URLS.forEach((url) => {
      expect(canonicalSolutionUrl(url), url).toBeNull();
    });
  });

  it("validates every committed solutions-lock URL", () => {
    const { document, mod } = bootstrap();
    const { AssessmentApp, canonicalSolutionUrl } = mod.exports;
    const lock = JSON.parse(readFileSync(LOCK_PATH, "utf8"));
    const app = new AssessmentApp(document.getElementById("assessment-app"));

    expect(lock.solutions.length).toBeGreaterThan(0);
    lock.solutions.forEach((entry) => {
      expect(canonicalSolutionUrl(entry.url), entry.id).toBe(entry.url);
    });
    app.setSolutionsLock(lock);
    expect(app.solutionsLock.solutions).toHaveLength(lock.solutions.length);
    app.solutionsLock.solutions.forEach((entry, index) => {
      expect(entry.url, entry.id).toBe(lock.solutions[index].url);
    });
  });

  it("sanitizes loaded URLs and revalidates both rendering sinks", () => {
    const { document, mod } = bootstrap();
    const { AssessmentApp, canonicalSolutionUrl, SOLUTIONS_BASE_URL } = mod.exports;
    const app = new AssessmentApp(document.getElementById("assessment-app"));
    const id = "01-copilot-readiness-scanner";
    const malicious =
      "https://github.com/judeper/FSI-CopilotGov-Solutions/../../attacker/repo";
    const entry = {
      id,
      name: "Readiness Scanner",
      url: malicious,
      summary: "test",
    };

    app.setSolutionsLock({ solutions: [entry] });
    expect(app.solutionsLock.solutions[0].url).toBeNull();
    expect(app.solutionsLockById[id].url).toBeNull();

    app.manifest = [{
      id: "1.1",
      solutions: [{ id, tier: 1, role: "primary" }],
    }];
    app.manifestById = { "1.1": app.manifest[0] };
    app.data = { controls: [] };

    // Bypass load-time sanitization to prove each href sink revalidates.
    app.solutionsLockById[id].url = malicious;
    const cards = app.renderSolutionCards({ id: "1.1" });
    const card = cards.querySelector(".solution-card");
    expect(card.getAttribute("href")).toBe(SOLUTIONS_BASE_URL + id);
    expect(canonicalSolutionUrl(card.getAttribute("href"))).not.toBeNull();

    const panel = app._renderSolutionDetailPanel(
      Object.assign({}, entry, { url: malicious }),
    );
    const detailLink = panel.querySelector(".solution-detail-link");
    expect(detailLink.getAttribute("href")).toBe(SOLUTIONS_BASE_URL + id);
    expect(canonicalSolutionUrl(detailLink.getAttribute("href"))).not.toBeNull();
  });

  it("renders no link when neither the URL nor solution id is safe", () => {
    const { document, mod } = bootstrap();
    const { AssessmentApp } = mod.exports;
    const app = new AssessmentApp(document.getElementById("assessment-app"));
    const id = "../attacker";

    app.setSolutionsLock({
      solutions: [{ id, name: "Unsafe", url: "javascript:alert(1)" }],
    });
    app.manifest = [{ id: "1.1", solutions: [{ id, tier: 1, role: "primary" }] }];
    app.manifestById = { "1.1": app.manifest[0] };

    const cards = app.renderSolutionCards({ id: "1.1" });
    const card = cards.querySelector(".solution-card");
    expect(card.tagName).toBe("DIV");
    expect(card.hasAttribute("href")).toBe(false);
    expect(card.getAttribute("aria-disabled")).toBe("true");
  });
});
