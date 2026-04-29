/**
 * FSI-CopilotGov Governance Scorecard
 *
 * Client-side SPA that walks users through a scoped assessment of the
 * 54-control governance framework and produces scorecards, gap analysis,
 * and remediation roadmaps.
 *
 * @version 1.0.0
 */
(function () {
  "use strict";

  /* ================================================================
     CONSTANTS
     ================================================================ */
  var STORAGE_KEY = "fsi-copilotgov-assessment";
  var STATE_SCHEMA_VERSION = 2;
  var LEVELS = ["baseline", "recommended", "regulated"];
  // D1: SPA enhancement storage keys (per-control drawer notes + facilitator toggle).
  var DRAWER_NOTES_PREFIX = "fsi-copilotgov:notes:";
  var FACILITATOR_MODE_KEY = "fsi-copilotgov:facilitator-mode";
  var SOLUTIONS_BASE_URL = "https://github.com/judeper/FSI-CopilotGov-Solutions/tree/main/solutions/";
  // D2: Collector evidence import storage + status-mapping constants.
  var COLLECTOR_EVIDENCE_KEY_PREFIX = "fsi-copilotgov:collector-evidence:";
  var COLLECTOR_STATUS_MAP = { pass: "yes", partial: "partial", fail: "no" };
  // Severity ranking used when multiple evidence rows disagree on status.
  var COLLECTOR_STATUS_PRIORITY = { no: 3, partial: 2, yes: 1 };
  // E: Envelope export schema + identity storage keys.
  var ENVELOPE_SCHEMA_VERSION = "fsi-copilotgov-envelope/0.1.0";
  var ENVELOPE_IDENTITY_KEY = "fsi-copilotgov:envelope-identity";
  var STEPS = [
    { id: "welcome", label: "Welcome", num: 1 },
    { id: "scoping", label: "Scope", num: 2 },
    { id: "phase1", label: "Assess Controls", num: 3 },
    { id: "phase2", label: "Drill-Down", num: 4 },
    { id: "results", label: "Results", num: 5 },
    { id: "export", label: "Export", num: 6 },
  ];
  var ANSWERS = [
    { value: "yes", label: "Yes", cls: "selected" },
    { value: "partial", label: "Partial", cls: "selected-partial" },
    { value: "no", label: "No", cls: "selected-no" },
    { value: "na", label: "N/A", cls: "selected" },
  ];

  /* ================================================================
     UTILITY HELPERS
     ================================================================ */
  function h(tag, attrs, children) {
    var el = document.createElement(tag);
    if (attrs) {
      Object.keys(attrs).forEach(function (k) {
        var v = attrs[k];
        if (v === null || v === undefined) return; // Skip null/undefined
        if (k === "className") el.className = v;
        else if (k.indexOf("on") === 0)
          el.addEventListener(k.slice(2).toLowerCase(), v);
        else if (k === "htmlFor") el.setAttribute("for", v);
        else el.setAttribute(k, v);
      });
    }
    if (children !== undefined && children !== null) {
      if (Array.isArray(children)) {
        children.forEach(function (c) {
          if (c == null) return;
          el.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
        });
      } else if (typeof children === "string") {
        el.textContent = children;
      } else {
        el.appendChild(children);
      }
    }
    return el;
  }

  function uuid() {
    return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function (c) {
      var r = (Math.random() * 16) | 0;
      return (c === "x" ? r : (r & 0x3) | 0x8).toString(16);
    });
  }

  function fmtDate(iso) {
    if (!iso) return "—";
    var d = new Date(iso);
    return d.toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" });
  }

  function ragClass(pct) {
    if (pct >= 80) return "green";
    if (pct >= 50) return "amber";
    return "red";
  }

  function clamp(v, lo, hi) { return Math.max(lo, Math.min(hi, v)); }

  function debounce(fn, ms) {
    var timer;
    return function () {
      var ctx = this, args = arguments;
      clearTimeout(timer);
      timer = setTimeout(function () { fn.apply(ctx, args); }, ms);
    };
  }

  /** Sanitize a string for CSV/Excel to prevent formula injection. */
  function sanitizeCell(val) {
    if (typeof val !== "string") return val;
    // Prefix dangerous leading characters that trigger formula execution
    if (/^[=+\-@\t\r]/.test(val)) return "'" + val;
    return val;
  }

  function downloadBlob(blob, filename) {
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    setTimeout(function () {
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }, 100);
  }

  function getBasePath() {
    // Calculate base path for playbook links relative to site root
    var path = window.location.pathname;
    // If we're at /FSI-CopilotGov/assessment/ then base is /FSI-CopilotGov/
    var match = path.match(/^(\/[^/]*\/)/);
    return match ? match[1] : "/";
  }

  function getStorageStateKey(id) {
    return STORAGE_KEY + "-state-" + id;
  }

  /* ================================================================
     D1: AUTHORED-CONTENT HELPERS
     Centralize TODO-placeholder detection so drawer / facilitator /
     yes-bar / solution rendering can gracefully degrade on the 53
     controls whose manifest fields are still TODO markers.
     ================================================================ */
  function isTodoString(value) {
    if (typeof value !== "string") return false;
    var s = value.trim();
    if (!s) return true;
    return /^todo\b/i.test(s) || /^\[todo\b/i.test(s);
  }

  /**
   * Return true when `value` is present, non-empty, and not a TODO placeholder.
   *
   * - Strings: non-empty and not starting with "TODO".
   * - Arrays: non-empty and at least one item passes isAuthored.
   * - Objects: at least one own value passes isAuthored.
   * - Null / undefined / 0-length: false.
   */
  function isAuthored(value) {
    if (value === null || value === undefined) return false;
    if (typeof value === "string") return !isTodoString(value);
    if (Array.isArray(value)) {
      if (!value.length) return false;
      for (var i = 0; i < value.length; i++) {
        if (isAuthored(value[i])) return true;
      }
      return false;
    }
    if (typeof value === "object") {
      var keys = Object.keys(value);
      if (!keys.length) return false;
      for (var k = 0; k < keys.length; k++) {
        if (isAuthored(value[keys[k]])) return true;
      }
      return false;
    }
    return true;
  }

  /** Return `fallback` when the manifest field is missing or a TODO marker. */
  function authoredOr(value, fallback) {
    return isAuthored(value) ? value : fallback;
  }

  /* ================================================================
     D2: COLLECTOR EVIDENCE PARSER
     Transforms a CSV or JSON produced by Collect-Graph / Collect-Purview
     etc. into an in-memory map the SPA can apply to state.
     ================================================================ */

  /** Parse a single CSV row respecting double-quoted cells with escaped quotes. */
  function parseCsvLine(line) {
    var out = [];
    var cur = "";
    var inQ = false;
    for (var i = 0; i < line.length; i++) {
      var c = line.charAt(i);
      if (inQ) {
        if (c === '"' && line.charAt(i + 1) === '"') { cur += '"'; i++; }
        else if (c === '"') { inQ = false; }
        else { cur += c; }
      } else {
        if (c === '"') inQ = true;
        else if (c === ',') { out.push(cur); cur = ""; }
        else cur += c;
      }
    }
    out.push(cur);
    return out.map(function (x) { return x.trim(); });
  }

  /**
   * Parse a collector CSV (schema: control_id,evidence_key,status,raw_value,collected_at)
   * into a map of { controlId: { status: "yes"|"partial"|"no"|null, evidence: [...] } }.
   *
   * - Status is mapped: pass→yes, partial→partial, fail→no. Unknown values are
   *   skipped (the row still contributes evidence) and emit a console warning.
   * - When multiple rows map a single control to different statuses, the worst
   *   severity wins (no > partial > yes) — this matches operator expectations
   *   that any failing signal should downgrade the aggregate answer.
   */
  function parseCollectorCsv(text) {
    var map = {};
    if (typeof text !== "string") return map;
    var body = text.replace(/\r\n/g, "\n").replace(/\r/g, "\n");
    var lines = body.split("\n");
    // Drop blank and comment lines.
    var rows = [];
    for (var i = 0; i < lines.length; i++) {
      var ln = lines[i];
      if (!ln || !ln.trim() || /^#/.test(ln.trim())) continue;
      rows.push(ln);
    }
    if (!rows.length) return map;

    var header = parseCsvLine(rows[0]).map(function (h) { return h.toLowerCase(); });
    var iCtrl = header.indexOf("control_id");
    var iKey = header.indexOf("evidence_key");
    var iStatus = header.indexOf("status");
    var iRaw = header.indexOf("raw_value");
    var iAt = header.indexOf("collected_at");
    if (iCtrl < 0) {
      if (typeof console !== "undefined" && console.warn) {
        console.warn("[collector] CSV missing required control_id column");
      }
      return map;
    }

    for (var r = 1; r < rows.length; r++) {
      var cols = parseCsvLine(rows[r]);
      var ctrl = cols[iCtrl];
      if (!ctrl) continue;
      var statusRaw = iStatus >= 0 ? (cols[iStatus] || "").toLowerCase() : "";
      var mapped = COLLECTOR_STATUS_MAP[statusRaw] || null;
      if (statusRaw && !mapped) {
        if (typeof console !== "undefined" && console.warn) {
          console.warn("[collector] unknown status '" + statusRaw + "' for " + ctrl + " — row status ignored");
        }
      }
      var entry = map[ctrl] || { status: null, evidence: [] };
      if (mapped) {
        var prev = entry.status;
        if (!prev || (COLLECTOR_STATUS_PRIORITY[mapped] > COLLECTOR_STATUS_PRIORITY[prev])) {
          entry.status = mapped;
        }
      }
      entry.evidence.push({
        key: iKey >= 0 ? cols[iKey] || "" : "",
        raw: iRaw >= 0 ? cols[iRaw] || "" : "",
        collectedAt: iAt >= 0 ? cols[iAt] || "" : "",
        status: mapped || statusRaw || "",
      });
      map[ctrl] = entry;
    }
    return map;
  }

  /**
   * Parse a collector JSON payload. Accepts either:
   *   { "<controlId>": { status, evidence: [...] }, ... }
   * or a flat array of rows [{ control_id, evidence_key, status, raw_value, collected_at }, ...].
   */
  function parseCollectorJson(text) {
    var parsed;
    try { parsed = typeof text === "string" ? JSON.parse(text) : text; }
    catch (_e) { return {}; }
    if (!parsed || typeof parsed !== "object") return {};
    if (Array.isArray(parsed)) {
      // Convert array of rows to CSV-style map.
      var map = {};
      parsed.forEach(function (row) {
        if (!row || typeof row !== "object") return;
        var ctrl = row.control_id || row.controlId;
        if (!ctrl) return;
        var statusRaw = String(row.status || "").toLowerCase();
        var mapped = COLLECTOR_STATUS_MAP[statusRaw] || null;
        if (statusRaw && !mapped && typeof console !== "undefined" && console.warn) {
          console.warn("[collector] unknown status '" + statusRaw + "' for " + ctrl);
        }
        var entry = map[ctrl] || { status: null, evidence: [] };
        if (mapped) {
          var prev = entry.status;
          if (!prev || COLLECTOR_STATUS_PRIORITY[mapped] > COLLECTOR_STATUS_PRIORITY[prev]) {
            entry.status = mapped;
          }
        }
        entry.evidence.push({
          key: String(row.evidence_key || row.evidenceKey || ""),
          raw: String(row.raw_value || row.rawValue || ""),
          collectedAt: String(row.collected_at || row.collectedAt || ""),
          status: mapped || statusRaw || "",
        });
        map[ctrl] = entry;
      });
      return map;
    }
    // Object-shaped already.
    var out = {};
    Object.keys(parsed).forEach(function (ctrl) {
      var v = parsed[ctrl];
      if (!v || typeof v !== "object") return;
      var statusRaw = v.status ? String(v.status).toLowerCase() : "";
      var mapped = COLLECTOR_STATUS_MAP[statusRaw] || (statusRaw && ["yes", "partial", "no"].indexOf(statusRaw) >= 0 ? statusRaw : null);
      out[ctrl] = {
        status: mapped,
        evidence: Array.isArray(v.evidence) ? v.evidence.map(function (e) {
          return {
            key: String((e && (e.key || e.evidence_key)) || ""),
            raw: String((e && (e.raw || e.raw_value)) || ""),
            collectedAt: String((e && (e.collectedAt || e.collected_at)) || ""),
            status: String((e && e.status) || ""),
          };
        }) : [],
      };
    });
    return out;
  }

  function findStep(stepId) {
    for (var i = 0; i < STEPS.length; i++) {
      if (STEPS[i].id === stepId) return STEPS[i];
    }
    return null;
  }

  function normalizeLevel(level) {
    return LEVELS.indexOf(level) >= 0 ? level : "recommended";
  }

  function isFocusable(el) {
    if (!el || typeof el.matches !== "function") return false;
    if (el.disabled) return false;
    if (el.getAttribute("aria-hidden") === "true") return false;
    if (el.tabIndex < 0) return false;
    return el.matches('a[href], button, textarea, input, select, [tabindex]');
  }

  function getFocusableElements(root) {
    return Array.prototype.slice.call(
      root.querySelectorAll('a[href], button:not([disabled]), textarea:not([disabled]), input:not([disabled]), select:not([disabled]), [tabindex]:not([tabindex="-1"])')
    ).filter(isFocusable);
  }

  /* ================================================================
     AssessmentApp CLASS
     ================================================================ */
  function AssessmentApp(container) {
    this.el = container;
    this.data = null;           // assessment-data.json contents (legacy primary)
    this.manifest = null;       // controls.json — engine-facing manifest (v1.4)
    this.manifestById = {};     // D1: O(1) lookup of manifest rows by control id
    this.solutionsLock = null;  // D1: solutions-lock.json contents
    this.solutionsLockById = {};// D1: O(1) lookup of solution entries by slug
    this.state = null;          // current assessment state
    this.charts = [];           // Chart.js instances to destroy on cleanup
    this.step = "welcome";
    this.message = null;
    this.pendingDeleteId = null;
    this._observers = [];
    this._drawerCtrlId = null;  // D1: id of control currently shown in drawer
    this._drawerRoot = null;    // D1: persistent drawer DOM node (survives re-render)
    this._drawerBackdrop = null;
    this._drawerPrevFocus = null;
    this.facilitatorMode = false; // D1: toggled via header button, persisted
    try {
      this.facilitatorMode = localStorage.getItem(FACILITATOR_MODE_KEY) === "1";
    } catch (_e) { /* private mode / disabled storage */ }
    this._debouncedSave = debounce(this.saveToStorage.bind(this), 500);
  }

  AssessmentApp.prototype.init = function () {
    var self = this;
    this.loadData().then(function () {
      self.render();
    });
  };

  AssessmentApp.prototype.destroy = function () {
    this.charts.forEach(function (c) { try { c.destroy(); } catch (e) { /* */ } });
    this.charts = [];
    this._observers.forEach(function (o) { try { o.disconnect(); } catch (e) { /* */ } });
    this._observers = [];
  };

  AssessmentApp.prototype.loadData = function () {
    var self = this;
    var base = "";
    var scripts = document.querySelectorAll('script[src*="assessment-loader"]');
    if (scripts.length) {
      var src = scripts[scripts.length - 1].src;
      base = src.substring(0, src.lastIndexOf("/") + 1);
    }

    // Manifest URL is anchored at site-root (../../assessment/data/...) and
    // is loaded best-effort — A1 keeps assessment-data.json as the primary
    // data source. A2/D1 will move SPA rendering onto the manifest.
    var manifestUrl;
    try {
      manifestUrl = new URL("../../assessment/data/controls.json", base).toString();
    } catch (_e) {
      manifestUrl = null;
    }

    var manifestPromise = manifestUrl
      ? fetch(manifestUrl)
          .then(function (r) { return r.ok ? r.json() : null; })
          .then(function (m) {
            if (Array.isArray(m) && m.length) {
              self.manifest = m;
              self.manifestById = {};
              m.forEach(function (row) {
                if (row && row.id) self.manifestById[row.id] = row;
              });
              if (window.console && console.debug) {
                console.debug("[assessment] manifest loaded: " + m.length + " controls");
              }
            }
          })
          .catch(function () { /* manifest is optional in A1 */ })
      : Promise.resolve();

    // D1: solutions-lock.json ships alongside the manifest via the
    // copy_assessment_data mkdocs hook. Best-effort load — if it fails
    // the drawer falls back to a "no mappings yet" placeholder.
    var solutionsLockUrl;
    try {
      solutionsLockUrl = new URL("../../assessment/data/solutions-lock.json", base).toString();
    } catch (_e) {
      solutionsLockUrl = null;
    }
    var solutionsLockPromise = solutionsLockUrl
      ? fetch(solutionsLockUrl)
          .then(function (r) { return r.ok ? r.json() : null; })
          .then(function (lock) {
            if (!lock || typeof lock !== "object") return;
            self.solutionsLock = lock;
            self.solutionsLockById = {};
            var entries = Array.isArray(lock.solutions) ? lock.solutions : [];
            entries.forEach(function (entry) {
              if (entry && entry.id) self.solutionsLockById[entry.id] = entry;
            });
            if (window.console && console.debug) {
              console.debug("[assessment] solutions-lock loaded: " + entries.length + " solutions");
            }
          })
          .catch(function () { /* optional */ })
      : Promise.resolve();

    var dataPromise = fetch(base + "assessment-data.json")
      .then(function (r) {
        if (!r.ok) throw new Error("Failed to load assessment data: " + r.status);
        return r.json();
      })
      .then(function (d) { self.data = d; })
      .catch(function (err) {
        console.error(err);
        self.el.innerHTML =
          '<div class="admonition failure"><p class="admonition-title">Error</p>' +
          "<p>Could not load assessment data. Run <code>python scripts/extract_assessment_data.py</code> first.</p></div>";
        throw err;
      });

    return Promise.all([manifestPromise, solutionsLockPromise, dataPromise]).then(function () { /* */ });
  };

  AssessmentApp.prototype.setMessage = function (type, title, text, details) {
    this.message = {
      type: type || "info",
      title: title || "",
      text: text || "",
      details: Array.isArray(details) ? details : [],
    };
    this.refreshMessageRegion();
  };

  AssessmentApp.prototype.clearMessage = function () {
    this.message = null;
    this.refreshMessageRegion();
  };

  AssessmentApp.prototype.renderMessageRegion = function () {
    var wrap = h("div", { id: "ag-message-region" });
    if (!this.message) return wrap;

    var msg = this.message;
    var banner = h("div", {
      className: "ag-message ag-message-" + msg.type,
      role: msg.type === "error" ? "alert" : "status",
      "aria-live": msg.type === "error" ? "assertive" : "polite",
      "aria-atomic": "true",
    });
    var main = h("div", { style: "flex:1" });
    if (msg.title) {
      main.appendChild(h("strong", { className: "ag-message-title" }, msg.title));
    }
    if (msg.text) {
      main.appendChild(h("p", { className: "ag-message-text" }, msg.text));
    }
    if (msg.details && msg.details.length > 0) {
      var list = h("ul", { className: "ag-message-list" });
      msg.details.forEach(function (detail) {
        list.appendChild(h("li", null, detail));
      });
      main.appendChild(list);
    }
    banner.appendChild(main);
    banner.appendChild(h("button", {
      className: "ag-message-dismiss",
      type: "button",
      "aria-label": "Dismiss message",
      onClick: this.clearMessage.bind(this),
    }, "Dismiss"));
    wrap.appendChild(banner);
    return wrap;
  };

  AssessmentApp.prototype.refreshMessageRegion = function () {
    var current = this.el.querySelector("#ag-message-region");
    if (!current || !current.parentNode) return;
    current.parentNode.replaceChild(this.renderMessageRegion(), current);
  };

  AssessmentApp.prototype.announce = function (message) {
    var live = this.el.querySelector("#ag-app-live");
    if (!live) return;
    live.textContent = "";
    setTimeout(function () { live.textContent = message; }, 10);
  };

  /* ================================================================
     STATE MANAGEMENT
     ================================================================ */
  AssessmentApp.prototype.newState = function () {
    return {
      assessmentId: uuid(),
      assessmentName: "",
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      schemaVersion: STATE_SCHEMA_VERSION,
      dataVersion: this.data && this.data.version ? String(this.data.version) : "",
      frameworkVersion: this.data && this.data.frameworkVersion ? String(this.data.frameworkVersion) : "",
      lastStep: "scoping",
      scoping: {
        organizationName: "",
        assessorName: "",
        assessorRole: "",
        institutionType: "",
        zones: [1, 2, 3],
        targetLevel: "recommended",
        adoptionPhase: 0,
        regulations: [],
        scope: "full",
      },
      responses: {},      // controlId → { answer, notes }
      drilldown: {},      // controlId → { subQuestionId → answer }
      completedSteps: [],
    };
  };

  AssessmentApp.prototype.getStepLabel = function (stepId) {
    var step = findStep(stepId);
    return step ? step.label : "Assessment";
  };

  AssessmentApp.prototype.getTargetLevel = function (state) {
    var source = state || this.state;
    return normalizeLevel(source && source.scoping ? source.scoping.targetLevel : "recommended");
  };

  AssessmentApp.prototype.getIncludedLevels = function (level) {
    var normalized = normalizeLevel(level || this.getTargetLevel());
    return LEVELS.slice(0, LEVELS.indexOf(normalized) + 1);
  };

  AssessmentApp.prototype.getDefaultAssessmentName = function (state) {
    var source = state || this.state;
    var orgName = source && source.scoping ? source.scoping.organizationName : "";
    if (!orgName) return "";
    return orgName + " — " + new Date().toISOString().slice(0, 10);
  };

  AssessmentApp.prototype.hasAnsweredControl = function (controlId, state) {
    var source = state || this.state;
    var resp = source && source.responses ? source.responses[controlId] : null;
    return !!(resp && resp.answer);
  };

  AssessmentApp.prototype.getAnsweredControlCount = function (state) {
    var source = state || this.state;
    var self = this;
    if (!source || !source.responses || !this.data) return 0;
    return this.data.controls.filter(function (ctrl) {
      return self.hasAnsweredControl(ctrl.id, source);
    }).length;
  };

  AssessmentApp.prototype.getUnansweredControls = function (state) {
    var source = state || this.state;
    var self = this;
    if (!this.data) return [];
    return this.data.controls.filter(function (ctrl) {
      return !self.hasAnsweredControl(ctrl.id, source);
    });
  };

  AssessmentApp.prototype.isScopingComplete = function (state) {
    var source = state || this.state;
    if (!source || !source.scoping) return false;
    return !!(source.scoping.organizationName && source.scoping.institutionType && source.scoping.targetLevel);
  };

  AssessmentApp.prototype.getCurrentStorageId = function () {
    try {
      return localStorage.getItem(STORAGE_KEY + "-current-id") || "";
    } catch (e) {
      return "";
    }
  };

  AssessmentApp.prototype.saveToStorage = function () {
    if (!this.state) return;
    var stateKey = getStorageStateKey(this.state.assessmentId);
    this.state.updatedAt = new Date().toISOString();
    this.state.lastStep = this.step;
    this.state.schemaVersion = STATE_SCHEMA_VERSION;
    this.state.dataVersion = this.data && this.data.version ? String(this.data.version) : this.state.dataVersion || "";
    this.state.frameworkVersion = this.data && this.data.frameworkVersion ? String(this.data.frameworkVersion) : this.state.frameworkVersion || "";
    try {
      localStorage.setItem(stateKey, JSON.stringify(this.state));
      localStorage.setItem(STORAGE_KEY + "-current-id", this.state.assessmentId);
      localStorage.setItem(STORAGE_KEY + "-current", JSON.stringify(this.state));
      var list = this.getSavedList();
      var idx = list.findIndex(function (s) { return s.id === this.state.assessmentId; }.bind(this));
      var entry = {
        id: this.state.assessmentId,
        name: this.state.assessmentName || this.state.scoping.organizationName || "Untitled",
        updatedAt: this.state.updatedAt,
        createdAt: this.state.createdAt,
        progress: this.getProgressPct(),
        step: this.state.lastStep,
      };
      if (idx >= 0) list[idx] = entry;
      else list.push(entry);
      localStorage.setItem(STORAGE_KEY + "-list", JSON.stringify(list));
    } catch (e) {
      console.error("Failed to save assessment draft:", e);
      this.setMessage(
        "warning",
        "Browser draft not saved",
        "Your latest changes could not be saved to browser storage. Use Save to File to keep a portable copy of this assessment."
      );
    }
  };

  AssessmentApp.prototype.getStoredStateBlob = function (id) {
    if (!id) return null;
    try {
      var perAssessment = localStorage.getItem(getStorageStateKey(id));
      if (perAssessment) return perAssessment;
      var legacy = localStorage.getItem(STORAGE_KEY + "-current");
      if (!legacy) return null;
      var parsed = JSON.parse(legacy);
      if (parsed && parsed.assessmentId === id) return legacy;
    } catch (e) {
      return null;
    }
    return null;
  };

  AssessmentApp.prototype.getSavedList = function () {
    try {
      var raw = JSON.parse(localStorage.getItem(STORAGE_KEY + "-list") || "[]");
      if (!Array.isArray(raw)) return [];
      var self = this;
      return raw.filter(function (item) {
        return item && typeof item === "object" && typeof item.id === "string" && !!self.getStoredStateBlob(item.id);
      });
    } catch (e) { return []; }
  };

  AssessmentApp.prototype.getDefaultResumeStep = function (state) {
    var source = state || this.state;
    if (!source) return "welcome";
    if (source.lastStep && findStep(source.lastStep)) return source.lastStep;
    if (source.completedSteps && source.completedSteps.indexOf("results") >= 0) return "results";
    if (source.completedSteps && source.completedSteps.indexOf("phase2") >= 0) return "results";
    if (source.completedSteps && source.completedSteps.indexOf("phase1") >= 0) return "results";
    if (this.isScopingComplete(source)) return "phase1";
    return "scoping";
  };

  AssessmentApp.prototype.loadFromStorage = function (id) {
    try {
      var targetId = id || this.getCurrentStorageId();
      var blob = targetId ? this.getStoredStateBlob(targetId) : localStorage.getItem(STORAGE_KEY + "-current");
      if (!blob) return false;
      var data = JSON.parse(blob);
      if (data && (!targetId || data.assessmentId === targetId) && this.validateState(data)) {
        this.state = this.buildCleanState(data);
        return true;
      }
    } catch (e) { /* */ }
    return false;
  };

  AssessmentApp.prototype.deleteSaved = function (id) {
    var list = this.getSavedList().filter(function (s) { return s.id !== id; });
    localStorage.setItem(STORAGE_KEY + "-list", JSON.stringify(list));
    try {
      localStorage.removeItem(getStorageStateKey(id));
      var currentId = this.getCurrentStorageId();
      if (currentId === id) {
        localStorage.removeItem(STORAGE_KEY + "-current-id");
        localStorage.removeItem(STORAGE_KEY + "-current");
      }
    } catch (e) { /* */ }
  };

  AssessmentApp.prototype.getProgressPct = function () {
    if (!this.state || !this.data) return 0;
    var total = this.data.controls.length;
    var answered = this.getAnsweredControlCount();
    return Math.round((answered / total) * 100);
  };

  AssessmentApp.prototype.validateState = function (parsed) {
    if (!parsed || typeof parsed !== "object" || Array.isArray(parsed)) return false;
    if (typeof parsed.assessmentId !== "string") return false;
    if (!parsed.scoping || typeof parsed.scoping !== "object") return false;
    if (!parsed.responses || typeof parsed.responses !== "object") return false;
    // Validate responses values
    var validAnswers = { yes: 1, partial: 1, no: 1, na: 1 };
    for (var k in parsed.responses) {
      if (!Object.prototype.hasOwnProperty.call(parsed.responses, k)) continue;
      var r = parsed.responses[k];
      if (r && r.answer && !validAnswers[r.answer]) return false;
    }
    return true;
  };

  AssessmentApp.prototype.buildCleanState = function (parsed) {
    var sc = parsed.scoping || {};
    var clean = {
      assessmentId: String(parsed.assessmentId),
      assessmentName: String(parsed.assessmentName || ""),
      createdAt: parsed.createdAt || new Date().toISOString(),
      updatedAt: parsed.updatedAt || new Date().toISOString(),
      schemaVersion: typeof parsed.schemaVersion === "number" ? parsed.schemaVersion : 1,
      dataVersion: String(parsed.dataVersion || ""),
      frameworkVersion: String(parsed.frameworkVersion || ""),
      lastStep: findStep(parsed.lastStep) ? parsed.lastStep : "",
      scoping: {
        organizationName: String(sc.organizationName || ""),
        assessorName: String(sc.assessorName || ""),
        assessorRole: String(sc.assessorRole || ""),
        institutionType: String(sc.institutionType || ""),
        zones: Array.isArray(sc.zones) ? sc.zones.filter(function (z) { return [1, 2, 3].indexOf(z) >= 0; }) : [1, 2, 3],
        targetLevel: normalizeLevel(sc.targetLevel || "recommended"),
        adoptionPhase: [0, 1, 2].indexOf(parseInt(sc.adoptionPhase, 10)) >= 0 ? parseInt(sc.adoptionPhase, 10) : 0,
        regulations: Array.isArray(sc.regulations) ? sc.regulations.map(String) : [],
        scope: String(sc.scope || "full"),
      },
      responses: {},
      drilldown: {},
      completedSteps: Array.isArray(parsed.completedSteps) ? parsed.completedSteps.filter(function (stepId) {
        return !!findStep(stepId);
      }) : [],
    };
    for (var k in parsed.responses) {
      if (!Object.prototype.hasOwnProperty.call(parsed.responses, k)) continue;
      clean.responses[k] = parsed.responses[k];
    }
    if (parsed.drilldown) {
      for (var d in parsed.drilldown) {
        if (!Object.prototype.hasOwnProperty.call(parsed.drilldown, d)) continue;
        clean.drilldown[d] = parsed.drilldown[d];
      }
    }
    clean.schemaVersion = STATE_SCHEMA_VERSION;
    clean.dataVersion = this.data && this.data.version ? String(this.data.version) : clean.dataVersion;
    clean.frameworkVersion = this.data && this.data.frameworkVersion ? String(this.data.frameworkVersion) : clean.frameworkVersion;
    clean.lastStep = this.getDefaultResumeStep(clean);
    return clean;
  };

  AssessmentApp.prototype.importState = function (json, mode) {
    try {
      var parsed = typeof json === "string" ? JSON.parse(json) : json;
      var importMode = mode || "assessment";

      if (parsed && parsed.sectionExport) {
        if (importMode !== "section") {
          this.setMessage(
            "warning",
            "Use full assessment files here",
            "Role-specific section files should be imported from Drill-Down after you start or resume the related assessment."
          );
          return null;
        }
        if (!this.state) {
          this.setMessage(
            "warning",
            "Start an assessment first",
            "Import a completed section after you start a new assessment or resume the related browser draft."
          );
          return null;
        }
        return this.importSection(parsed);
      }

      if (importMode === "section") {
        this.setMessage(
          "warning",
          "Import a section file instead",
          "The selected file is a full assessment export. Use Import Assessment File from the welcome step to resume it."
        );
        return null;
      }

      if (!this.validateState(parsed)) {
        throw new Error("Invalid assessment file structure");
      }
      if (parsed.schemaVersion && parsed.schemaVersion > STATE_SCHEMA_VERSION) {
        throw new Error("This assessment file was created by a newer scorecard version.");
      }

      var details = [];
      if (!parsed.dataVersion && !parsed.frameworkVersion) {
        details.push("This file was created before version metadata was added. Review the imported scoping and scores before relying on it.");
      } else {
        if (parsed.dataVersion && this.data && String(parsed.dataVersion) !== String(this.data.version)) {
          details.push("Assessment data version mismatch: imported file " + parsed.dataVersion + ", current site " + this.data.version + ".");
        }
        if (parsed.frameworkVersion && this.data && String(parsed.frameworkVersion) !== String(this.data.frameworkVersion)) {
          details.push("Framework version mismatch: imported file " + parsed.frameworkVersion + ", current site " + this.data.frameworkVersion + ".");
        }
      }

      this.state = this.buildCleanState(parsed);
      this.pendingDeleteId = null;
      this.saveToStorage();
      this.setMessage(
        details.length > 0 ? "warning" : "success",
        details.length > 0 ? "Assessment imported with warnings" : "Assessment imported",
        details.length > 0
          ? "The assessment file was imported. Review the notes below before continuing."
          : "The assessment file was imported successfully. You can continue where it left off.",
        details
      );
      return {
        ok: true,
        type: "assessment",
        step: this.getDefaultResumeStep(this.state),
      };
    } catch (e) {
      console.error("Assessment import failed:", e);
      this.setMessage("error", "Import failed", "The selected file could not be imported. " + e.message);
      return null;
    }
  };

  AssessmentApp.prototype.importSection = function (sectionData) {
    if (!sectionData || !sectionData.responses || typeof sectionData.responses !== "object") {
      this.setMessage("error", "Section import failed", "The selected section file does not contain any responses to import.");
      return null;
    }
    if (sectionData.assessmentId && sectionData.assessmentId !== this.state.assessmentId) {
      this.setMessage(
        "error",
        "Section import blocked",
        "This section file belongs to a different assessment. Export a section from this assessment before importing updates."
      );
      return null;
    }

    var validAnswers = { yes: 1, partial: 1, no: 1, na: 1 };
    var conflicts = [];
    var applied = 0;
    var imported = 0;
    var details = [];
    var self = this;

    if (sectionData.dataVersion && this.data && String(sectionData.dataVersion) !== String(this.data.version)) {
      details.push("Section file data version " + sectionData.dataVersion + " differs from the current site version " + this.data.version + ".");
    }

    Object.keys(sectionData.responses).forEach(function (cid) {
      if (!Object.prototype.hasOwnProperty.call(sectionData.responses, cid)) return;
      var raw = sectionData.responses[cid];
      if (!raw || typeof raw !== "object") return;
      imported++;

      var incoming = { answer: validAnswers[raw.answer] ? raw.answer : "", notes: String(raw.notes || "") };
      var existing = self.state.responses[cid] || {};
      if (existing.answer && incoming.answer && existing.answer !== incoming.answer) {
        conflicts.push(cid);
        return;
      }

      self.state.responses[cid] = {
        answer: incoming.answer || existing.answer || "",
        notes: incoming.notes || existing.notes || "",
      };
      applied++;
    });

    if (sectionData.drilldown && typeof sectionData.drilldown === "object") {
      Object.keys(sectionData.drilldown).forEach(function (cid) {
        if (!Object.prototype.hasOwnProperty.call(sectionData.drilldown, cid)) return;
        if (conflicts.indexOf(cid) >= 0) return;
        var dd = sectionData.drilldown[cid];
        if (!dd || typeof dd !== "object") return;
        var clean = {};
        Object.keys(dd).forEach(function (k) {
          if (Object.prototype.hasOwnProperty.call(dd, k) && (dd[k] === "yes" || dd[k] === "no")) {
            clean[k] = dd[k];
          }
        });
        if (Object.keys(clean).length > 0) {
          self.state.drilldown[cid] = clean;
        }
      });
    }

    this.saveToStorage();
    if (conflicts.length > 0) {
      details.unshift(conflicts.length + " conflicting response(s) were kept in the current assessment: " + conflicts.join(", "));
    }
    this.setMessage(
      conflicts.length > 0 ? "warning" : "success",
      "Section import complete",
      applied + " of " + imported + " response(s) were merged into the current assessment.",
      details
    );
    return {
      ok: true,
      type: "section",
      step: this.step,
    };
  };

  /* ================================================================
     SCORING
     ================================================================ */
  AssessmentApp.prototype.getControlById = function (controlId) {
    if (!this.data || !this.data.controls) return null;
    for (var i = 0; i < this.data.controls.length; i++) {
      if (this.data.controls[i].id === controlId) return this.data.controls[i];
    }
    return null;
  };

  AssessmentApp.prototype.getVerificationCriteria = function (control, level) {
    var allowedLevels = this.getIncludedLevels(level);
    return (control.verificationCriteria || []).slice(0, 12).map(function (criterion, idx) {
      var text = typeof criterion === "string" ? criterion : String(criterion && criterion.text || "");
      var criterionLevel = criterion && typeof criterion === "object" ? criterion.governanceLevel : null;
      return text ? {
        id: "q" + idx,
        text: text,
        governanceLevel: LEVELS.indexOf(criterionLevel) >= 0 ? criterionLevel : null,
      } : null;
    }).filter(function (criterion) {
      return criterion && (!criterion.governanceLevel || allowedLevels.indexOf(criterion.governanceLevel) >= 0);
    });
  };

  AssessmentApp.prototype.getHiddenCriteriaCount = function (control, level) {
    var total = (control.verificationCriteria || []).slice(0, 12).filter(function (criterion) {
      if (typeof criterion === "string") return !!criterion;
      return !!(criterion && criterion.text);
    }).length;
    return Math.max(total - this.getVerificationCriteria(control, level).length, 0);
  };

  AssessmentApp.prototype.getDrilldownStats = function (level, state) {
    var source = state || this.state;
    if (!source || !this.data) {
      return { totalQuestions: 0, answeredQuestions: 0, controlsWithQuestions: 0, pendingControls: 0 };
    }

    var self = this;
    var totalQuestions = 0;
    var answeredQuestions = 0;
    var controlsWithQuestions = 0;
    var pendingControls = 0;

    this.getGapControls(level, source).forEach(function (ctrl) {
      var questions = self.getVerificationCriteria(ctrl, level || self.getTargetLevel(source));
      if (questions.length === 0) return;

      var dd = source.drilldown && source.drilldown[ctrl.id] ? source.drilldown[ctrl.id] : {};
      var answeredForControl = 0;
      controlsWithQuestions++;
      totalQuestions += questions.length;

      questions.forEach(function (question) {
        if (dd[question.id] === "yes" || dd[question.id] === "no") {
          answeredQuestions++;
          answeredForControl++;
        }
      });

      if (answeredForControl < questions.length) {
        pendingControls++;
      }
    });

    return {
      totalQuestions: totalQuestions,
      answeredQuestions: answeredQuestions,
      controlsWithQuestions: controlsWithQuestions,
      pendingControls: pendingControls,
    };
  };

  AssessmentApp.prototype.getAssessmentCompletion = function (state) {
    var answered = this.getAnsweredControlCount(state);
    var total = this.data ? this.data.controls.length : 0;
    return {
      answered: answered,
      total: total,
      remaining: Math.max(total - answered, 0),
      complete: total > 0 && answered === total,
    };
  };

  AssessmentApp.prototype.getControlScoreFromState = function (state, controlId, level) {
    var source = state || this.state;
    var resp = source && source.responses ? source.responses[controlId] : null;
    if (!resp || !resp.answer) return null;
    if (resp.answer === "na") return null;
    if (resp.answer === "yes") return 1.0;

    var control = this.getControlById(controlId);
    var questions = control ? this.getVerificationCriteria(control, level || this.getTargetLevel(source)) : [];
    if (questions.length > 0) {
      var dd = source.drilldown && source.drilldown[controlId] ? source.drilldown[controlId] : {};
      var answeredAny = false;
      var yesCount = 0;
      questions.forEach(function (question) {
        if (dd[question.id] === "yes") {
          yesCount++;
          answeredAny = true;
        } else if (dd[question.id] === "no") {
          answeredAny = true;
        }
      });
      if (answeredAny) {
        return yesCount / questions.length;
      }
    }
    return resp.answer === "partial" ? 0.5 : 0.0;
  };

  AssessmentApp.prototype.getControlScore = function (controlId, level) {
    return this.getControlScoreFromState(this.state, controlId, level);
  };

  AssessmentApp.prototype.getAggregateScore = function (controlIds, level, state) {
    var self = this;
    var total = 0;
    var count = 0;
    controlIds.forEach(function (cid) {
      var score = self.getControlScoreFromState(state || self.state, cid, level);
      if (score !== null) {
        total += score;
        count++;
      }
    });
    return count > 0 ? Math.round((total / count) * 100) : null;
  };

  AssessmentApp.prototype.getPillarScore = function (pillarNum, level, state) {
    var ids = this.data.controls
      .filter(function (c) { return c.pillar === pillarNum; })
      .map(function (c) { return c.id; });
    return this.getAggregateScore(ids, level, state);
  };

  AssessmentApp.prototype.getOverallScore = function (level, state) {
    var ids = this.data.controls.map(function (c) { return c.id; });
    return this.getAggregateScore(ids, level, state);
  };

  AssessmentApp.prototype.getRegulationScore = function (regKey, level, state) {
    var mapping = this.data.regulatoryMappings[regKey];
    if (!mapping) return null;
    return this.getAggregateScore(mapping.controls, level, state);
  };

  AssessmentApp.prototype.getZoneScore = function (zoneNum) {
    var self = this;
    var total = 0;
    var count = 0;
    this.data.controls.forEach(function (c) {
      if (c.zones && c.zones.indexOf(zoneNum) < 0) return;
      var weight = (c.zoneWeights && c.zoneWeights[String(zoneNum)] !== undefined)
        ? c.zoneWeights[String(zoneNum)] : 1;
      if (weight === 0) return;
      var score = self.getControlScore(c.id);
      if (score !== null) {
        total += score;
        count++;
      }
    });
    return count > 0 ? Math.round((total / count) * 100) : null;
  };

  // CopilotGov: governance level scoring (cumulative target model)
  AssessmentApp.prototype.getLevelScore = function (level, state) {
    var normalized = normalizeLevel(level);
    return this.getAggregateScore(
      this.data.controls.map(function (c) { return c.id; }),
      normalized,
      state
    );
  };

  AssessmentApp.prototype.getRiskPriority = function (control) {
    var score = this.getControlScore(control.id);
    if (score === null || score === 1.0) return 0;
    var regWeight = control.regulations.length >= 4 ? 3 : control.regulations.length >= 2 ? 2 : 1;
    // CopilotGov: inverted level weights — baseline gaps are most urgent
    var targetLevel = this.state.scoping.targetLevel || "recommended";
    var levelWeight = targetLevel === "baseline" ? 3 : targetLevel === "recommended" ? 2 : 1;
    var currentPhase = this.state.scoping.adoptionPhase || 0;
    var phaseWeight = 1;
    if (control.adoptionPhase) {
      var cp = control.adoptionPhase.phase;
      if (cp === currentPhase) phaseWeight = 3;
      else if (cp === currentPhase + 1) phaseWeight = 2;
    }
    return (1 - score) * regWeight * levelWeight * phaseWeight;
  };

  AssessmentApp.prototype.getGapControls = function (level, state) {
    var self = this;
    var source = state || this.state;
    return this.data.controls.filter(function (c) {
      var score = self.getControlScoreFromState(source, c.id, level);
      return score !== null && score < 1.0;
    }).sort(function (a, b) {
      return self.getRiskPriority(b) - self.getRiskPriority(a);
    });
  };

  AssessmentApp.prototype.canAccessStep = function (stepId) {
    var completion = this.getAssessmentCompletion();
    var phase1Complete = !!(this.state && this.state.completedSteps && this.state.completedSteps.indexOf("phase1") >= 0) || completion.complete;
    var resultsComplete = !!(this.state && this.state.completedSteps && this.state.completedSteps.indexOf("results") >= 0);
    var hasGaps = this.state && this.data ? this.getGapControls().length > 0 : false;

    if (stepId === "welcome") return true;
    if (!this.state) return false;
    if (stepId === "scoping") return true;
    if (stepId === "phase1") return this.isScopingComplete();
    if (stepId === "phase2") return phase1Complete && hasGaps;
    if (stepId === "results") return phase1Complete;
    if (stepId === "export") return resultsComplete || this.step === "export";
    return false;
  };

  AssessmentApp.prototype.getStepAccessHint = function (stepId) {
    if (stepId === "phase1" && !this.isScopingComplete()) {
      return "Complete the required scoping fields first.";
    }
    var completion = this.getAssessmentCompletion();
    if (stepId === "phase2") {
      if (!completion.complete) return "Answer every control in Assess Controls first.";
      if (this.state && this.data && this.getGapControls().length === 0) return "No gap controls require drill-down.";
    }
    if (stepId === "results" && !completion.complete) {
      return "Answer every control in Assess Controls before viewing results.";
    }
    if (stepId === "export" && !(this.state && this.state.completedSteps && this.state.completedSteps.indexOf("results") >= 0)) {
      return "Open Results before using Export.";
    }
    return this.getStepLabel(stepId);
  };

  /* ================================================================
     RENDERING — MAIN ROUTER
     ================================================================ */
  AssessmentApp.prototype.render = function () {
    this.destroy(); // Clean up charts
    this.el.innerHTML = "";
    this.el.appendChild(this.renderSteps());
    this.el.appendChild(this.renderMessageRegion());
    this.el.appendChild(h("div", {
      className: "ag-sr-only",
      id: "ag-app-live",
      "aria-live": "polite",
      "aria-atomic": "true",
    }));
    var content = h("div", { className: "ag-content" });
    switch (this.step) {
      case "welcome": this.renderWelcome(content); break;
      case "scoping": this.renderScoping(content); break;
      case "phase1":  this.renderPhase1(content); break;
      case "phase2":  this.renderPhase2(content); break;
      case "results": this.renderResults(content); break;
      case "export":  this.renderExport(content); break;
      case "solutions": this.renderSolutionsView(content); break;
    }
    this.el.appendChild(content);
  };

  AssessmentApp.prototype.goToStep = function (step) {
    // "solutions" is a side-view reachable any time; bypass canAccessStep.
    if (step !== "solutions" && !this.canAccessStep(step) && step !== "welcome") return;
    this.step = step;
    this.render();
    this.el.scrollIntoView({ behavior: "smooth", block: "start" });
    var heading = this.el.querySelector("[data-step-heading]");
    if (heading) heading.focus();
    if (step === "solutions") {
      this.announce("Opened solutions catalog");
    } else {
      this.announce("Step " + (findStep(step) ? findStep(step).num : "?") + " of " + STEPS.length + ": " + this.getStepLabel(step));
    }
  };

  AssessmentApp.prototype.renderSteps = function () {
    var self = this;
    var nav = h("nav", { className: "ag-steps", role: "navigation", "aria-label": "Assessment steps" });
    STEPS.forEach(function (s) {
      var cls = "ag-step-indicator";
      var current = s.id === self.step;
      var isCompleted = self.state && self.state.completedSteps && self.state.completedSteps.indexOf(s.id) >= 0;
      var canAccess = self.canAccessStep(s.id);
      if (current) cls += " active";
      else if (isCompleted) cls += " completed";
      var prefix = isCompleted && !current ? "\u2713 " : s.num + ". ";
      var el = h("button", {
        className: cls,
        type: "button",
        title: isCompleted ? s.label + " (completed)" : self.getStepAccessHint(s.id),
        "aria-current": current ? "step" : null,
        "aria-disabled": canAccess ? null : "true",
        disabled: canAccess ? null : "disabled",
        onClick: function () { self.goToStep(s.id); }
      }, prefix + s.label);
      nav.appendChild(el);
    });
    // C3: Solutions catalog side-view — always accessible, not part of the wizard.
    var solsCurrent = self.step === "solutions";
    nav.appendChild(h("button", {
      className: "ag-step-indicator ag-step-solutions" + (solsCurrent ? " active" : ""),
      type: "button",
      id: "solutions-nav-btn",
      title: "Browse the solutions catalog",
      "aria-current": solsCurrent ? "page" : null,
      onClick: function () { self.goToStep("solutions"); }
    }, "🧩 Solutions"));
    return nav;
  };

  /* ================================================================
     MODAL
     ================================================================ */
  AssessmentApp.prototype.showModal = function (title, contentEl) {
    var backdrop = h("div", { className: "ag-modal-backdrop" });
    var previousFocus = document.activeElement;
    var titleId = "ag-modal-title-" + Date.now();
    var modal = h("div", {
      className: "ag-modal",
      role: "dialog",
      "aria-modal": "true",
      "aria-labelledby": titleId,
      tabindex: "-1",
    });
    var header = h("div", { className: "ag-modal-header" });
    header.appendChild(h("h3", { id: titleId }, title));
    var closeBtn = h("button", { className: "ag-modal-close", "aria-label": "Close" }, "\u00D7");
    header.appendChild(closeBtn);
    modal.appendChild(header);
    var body = h("div", { className: "ag-modal-body" });
    body.appendChild(contentEl);
    modal.appendChild(body);
    backdrop.appendChild(modal);

    var close = function () {
      if (backdrop.parentNode) backdrop.parentNode.removeChild(backdrop);
      if (previousFocus && typeof previousFocus.focus === "function") previousFocus.focus();
    };
    var trapFocus = function (e) {
      if (e.key === "Escape") {
        e.preventDefault();
        close();
        return;
      }
      if (e.key !== "Tab") return;
      var focusable = getFocusableElements(modal);
      if (focusable.length === 0) {
        e.preventDefault();
        modal.focus();
        return;
      }
      var first = focusable[0];
      var last = focusable[focusable.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    };
    closeBtn.addEventListener("click", close);
    backdrop.addEventListener("click", function (e) { if (e.target === backdrop) close(); });
    backdrop.addEventListener("keydown", trapFocus);

    document.body.appendChild(backdrop);
    closeBtn.focus();
  };

  AssessmentApp.prototype.showScoringModal = function () {
    var content = h("div");
    content.appendChild(h("p", null,
      "Each control is scored based on your self-reported implementation status."));

    var dl = document.createElement("dl");
    var items = [
      ["Yes = 1.0", "Fully implemented and verified."],
      ["Partial = 0.5", "Some aspects implemented. Refined by Phase 2 drill-down sub-questions."],
      ["No = 0.0", "Not yet implemented."],
      ["N/A = excluded", "Not applicable to your organization; excluded from scoring."],
    ];
    items.forEach(function (pair) {
      dl.appendChild(h("dt", null, pair[0]));
      dl.appendChild(h("dd", null, pair[1]));
    });
    content.appendChild(dl);

    content.appendChild(h("p", { style: "margin-top:1rem;font-weight:600" }, "Aggregate Score Formula"));
    content.appendChild(h("p", null,
      "score = sum(controlScores) / count(applicableControls) \u00D7 100"));

    content.appendChild(h("p", { style: "margin-top:1rem;font-weight:600" }, "RAG Thresholds"));
    var ragDl = document.createElement("dl");
    ragDl.appendChild(h("dt", { style: "color:var(--ag-green)" }, "Green (80%+)"));
    ragDl.appendChild(h("dd", null, "Strong implementation; minor refinements may be needed."));
    ragDl.appendChild(h("dt", { style: "color:var(--ag-amber)" }, "Amber (50\u201379%)"));
    ragDl.appendChild(h("dd", null, "Partial implementation; focused remediation recommended."));
    ragDl.appendChild(h("dt", { style: "color:var(--ag-red)" }, "Red (below 50%)"));
    ragDl.appendChild(h("dd", null, "Significant gaps; prioritized remediation required."));
    content.appendChild(ragDl);

    content.appendChild(h("p", { style: "margin-top:1rem;font-weight:600" }, "Risk Priority"));
    content.appendChild(h("p", null,
      "riskPriority = (1 \u2212 score) \u00D7 regulatoryWeight \u00D7 levelWeight \u00D7 phaseWeight"));
    var rpDl = document.createElement("dl");
    rpDl.appendChild(h("dt", null, "Regulatory weight"));
    rpDl.appendChild(h("dd", null, "3.0 (4+ regulations), 2.0 (2\u20133), 1.0 (0\u20131)"));
    rpDl.appendChild(h("dt", null, "Level weight (inverted \u2014 foundational gaps are most urgent)"));
    rpDl.appendChild(h("dd", null, "3.0 (Baseline gap), 2.0 (Recommended gap), 1.0 (Regulated gap)"));
    rpDl.appendChild(h("dt", null, "Phase weight"));
    rpDl.appendChild(h("dd", null, "3.0 (current phase), 2.0 (next phase), 1.0 (future)"));
    content.appendChild(rpDl);

    content.appendChild(h("p", { style: "margin-top:1rem;font-weight:600" }, "Governance Level Scoring"));
    content.appendChild(h("p", null,
      "All controls are assessed at your selected target governance level. " +
      "Governance levels are cumulative: Recommended includes all Baseline requirements, and Regulated includes all Recommended requirements."));

    this.showModal("How Scoring Works", content);
  };

  /* ================================================================
     STEP 1: WELCOME
     ================================================================ */
  AssessmentApp.prototype.renderWelcome = function (parent) {
    var self = this;
    var wrap = h("div", { className: "ag-welcome" });

    wrap.appendChild(h("h2", { "data-step-heading": "true", tabindex: "-1" }, "Governance Scorecard"));
    wrap.appendChild(h("p", null,
      "Assess your organization's readiness across the 54-control FSI Copilot Governance Framework. " +
      "This tool helps identify gaps and generates a personalized remediation roadmap."
    ));

    // Disclaimer
    wrap.appendChild(h("div", { className: "ag-disclaimer" },
      "This assessment helps support governance readiness. It does not constitute legal advice " +
      "and does not constitute a compliance certification."
    ));

    // Scoring summary
    var scoringSummary = h("div", { className: "ag-scoring-summary" });
    var scoringDl = document.createElement("dl");
    scoringDl.style.margin = "0";
    [["Yes", "1.0"], ["Partial", "0.5"], ["No", "0.0"], ["N/A", "excluded"]].forEach(function (pair) {
      scoringDl.appendChild(h("dt", null, pair[0] + " ="));
      scoringDl.appendChild(h("dd", null, pair[1]));
    });
    scoringSummary.appendChild(scoringDl);
    var ragLine = h("div", { style: "margin-top:0.5rem" });
    ragLine.appendChild(h("span", { style: "font-weight:600" }, "RAG: "));
    ragLine.appendChild(h("span", { style: "color:var(--ag-green);font-weight:600" }, "Green 80%+ "));
    ragLine.appendChild(h("span", { style: "color:var(--ag-amber);font-weight:600" }, "Amber 50\u201379% "));
    ragLine.appendChild(h("span", { style: "color:var(--ag-red);font-weight:600" }, "Red <50%"));
    scoringSummary.appendChild(ragLine);
    var privacyNote = h("div", { className: "ag-privacy-note" },
      "Data Privacy: All assessment data stays in your browser. No data is sent to any server. " +
      "Use Save to File (JSON export) to share or archive results.");
    scoringSummary.appendChild(privacyNote);
    wrap.appendChild(scoringSummary);

    var btns = h("div", { className: "ag-btn-group", style: "justify-content: center" });
    btns.appendChild(h("button", {
      className: "ag-btn ag-btn-primary",
      onClick: function () {
        self.pendingDeleteId = null;
        self.clearMessage();
        self.state = self.newState();
        self.saveToStorage();
        self.goToStep("scoping");
      }
    }, "Start New Assessment"));

    btns.appendChild(h("button", {
      className: "ag-btn ag-btn-secondary",
      onClick: function () { self.triggerImport("assessment"); }
    }, "Import Assessment File"));
    wrap.appendChild(btns);

    wrap.appendChild(h("p", { style: "font-size:0.78rem;color:var(--md-default-fg-color--light);max-width:600px;margin:0.5rem auto" },
      "Browser drafts are saved automatically after you start the assessment and stay on this device only. " +
      "Use Save to File (JSON export) as the primary artifact for sharing or archival. " +
      "Import completed role-specific sections during Drill-Down."));

    var saved = this.getSavedList();
    if (saved.length > 0) {
      wrap.appendChild(h("h3", { style: "margin-top:2rem;font-size:1rem" }, "Saved Browser Drafts"));
      var list = h("ul", { className: "ag-saved-list" });
      saved.sort(function (a, b) { return new Date(b.updatedAt) - new Date(a.updatedAt); });
      saved.forEach(function (s) {
        var item = h("li", { className: "ag-saved-item" });
        var info = h("div");
        var savedStep = s.step && findStep(s.step) ? s.step : "scoping";
        info.appendChild(h("strong", null, s.name || "Untitled"));
        info.appendChild(h("div", { className: "ag-saved-meta" },
          fmtDate(s.updatedAt) + " — " + self.getStepLabel(savedStep) + " — " + (s.progress || 0) + "% of controls answered"
        ));
        item.appendChild(info);
        var actions = h("div", { className: "ag-btn-group", style: "margin:0" });
        var savedName = s.name || "Untitled";
        var awaitingDelete = self.pendingDeleteId === s.id;
        actions.appendChild(h("button", {
          className: "ag-btn ag-btn-sm ag-btn-primary",
          type: "button",
          "aria-label": "Resume draft " + savedName,
          onClick: function (e) {
            e.stopPropagation();
            if (self.loadFromStorage(s.id)) {
              self.pendingDeleteId = null;
              self.setMessage("success", "Draft resumed", "Resumed the saved browser draft for " + savedName + ".");
              self.goToStep(self.getDefaultResumeStep(self.state));
            }
          }
        }, "Resume Draft"));
        if (awaitingDelete) {
          actions.appendChild(h("button", {
            className: "ag-btn ag-btn-sm ag-btn-danger",
            type: "button",
            "aria-label": "Confirm delete draft " + savedName,
            onClick: function (e) {
              e.stopPropagation();
              self.deleteSaved(s.id);
              self.pendingDeleteId = null;
              self.setMessage("success", "Draft deleted", "Deleted the saved browser draft for " + savedName + ".");
              self.render();
            }
          }, "Confirm Delete"));
          actions.appendChild(h("button", {
            className: "ag-btn ag-btn-sm ag-btn-secondary",
            type: "button",
            onClick: function (e) {
              e.stopPropagation();
              self.pendingDeleteId = null;
              self.render();
            }
          }, "Cancel"));
        } else {
          actions.appendChild(h("button", {
            className: "ag-btn ag-btn-sm ag-btn-danger",
            type: "button",
            "aria-label": "Delete draft " + savedName,
            onClick: function (e) {
              e.stopPropagation();
              self.pendingDeleteId = s.id;
              self.render();
            }
          }, "Delete Draft"));
        }
        item.appendChild(actions);
        list.appendChild(item);
      });
      wrap.appendChild(list);
    }

    parent.appendChild(wrap);
  };

  AssessmentApp.prototype.triggerImport = function (mode) {
    var self = this;
    var input = document.createElement("input");
    input.type = "file";
    input.accept = ".json";
    input.onchange = function () {
      var file = input.files[0];
      if (!file) return;
      var reader = new FileReader();
      reader.onload = function () {
        var result = self.importState(reader.result, mode || "assessment");
        if (result && result.ok && result.step) {
          self.goToStep(result.step);
        }
      };
      reader.readAsText(file);
    };
    input.click();
  };

  /* ================================================================
     STEP 2: SCOPING
     ================================================================ */
  AssessmentApp.prototype.renderScoping = function (parent) {
    var self = this;
    var sc = this.state.scoping;
    var wrap = h("div");

    wrap.appendChild(h("h2", { style: "font-size:1.3rem;margin-bottom:0.3rem", "data-step-heading": "true", tabindex: "-1" }, "Assessment Scoping"));
    wrap.appendChild(h("p", { className: "ag-card-subtitle" },
      "Configure the assessment scope for your organization. " +
      "All controls in the manifest will be assessed and prioritized based on your profile and target governance level."
    ));
    wrap.appendChild(h("div", { className: "ag-callout" },
      "Required fields are marked with an asterisk. Browser drafts are saved on this device while you work, but Save to File remains the primary artifact for sharing or archival."
    ));

    var form = h("div", { className: "ag-card" });

    // Organization name
    form.appendChild(this.field("Organization Name", "text", sc.organizationName, function (v) {
      sc.organizationName = v;
      self._debouncedSave();
    }, "Used to label saved drafts and exports.", { required: true }));

    // Assessor
    form.appendChild(this.field("Assessor Name", "text", sc.assessorName, function (v) {
      sc.assessorName = v;
      self._debouncedSave();
    }));
    form.appendChild(this.field("Assessor Role", "text", sc.assessorRole, function (v) {
      sc.assessorRole = v;
      self._debouncedSave();
    },
      "e.g., AI Governance Lead, Compliance Officer"));

    // Institution type
    var instOptions = [
      { value: "", label: "Select institution type..." },
      { value: "broker-dealer", label: "Broker-Dealer (FINRA/SEC)" },
      { value: "bank", label: "Bank (OCC/Fed)" },
      { value: "adviser", label: "Investment Adviser (SEC)" },
      { value: "dual-registered", label: "Dual-Registered (FINRA + SEC)" },
      { value: "insurance", label: "Insurance Company" },
      { value: "credit-union", label: "Credit Union (NCUA)" },
    ];
    form.appendChild(this.selectField("Institution Type", instOptions, sc.institutionType, function (v) {
      sc.institutionType = v;
      // Auto-populate regulations
      var inst = self.data.institutionTypes[v];
      if (inst) sc.regulations = inst.regulations.slice();
      self._debouncedSave();
    }, "Used to preselect relevant regulations for the assessment.", { required: true }));

    // Target Governance Level
    var levelOptions = [
      { value: "baseline", label: "Baseline \u2014 Minimum viable governance for initial Copilot deployment" },
      { value: "recommended", label: "Recommended \u2014 Best practices for production environments" },
      { value: "regulated", label: "Regulated \u2014 Comprehensive, examination-ready governance" },
    ];
    form.appendChild(this.selectField("Target Governance Level", levelOptions, sc.targetLevel || "recommended", function (v) {
      sc.targetLevel = v;
      self._debouncedSave();
    }, "Determines which governance tiers are scored and displayed in Results.", { required: true }));

    // Adoption phase
    var phaseOptions = [
      { value: "0", label: "Phase 0 — Governance Setup (0-30 days)" },
      { value: "1", label: "Phase 1 — Pilot Deployment (1-3 months)" },
      { value: "2", label: "Phase 2 — Expansion (3-12 months)" },
    ];
    form.appendChild(this.selectField("Current Adoption Phase", phaseOptions, String(sc.adoptionPhase), function (v) {
      sc.adoptionPhase = parseInt(v, 10);
      self._debouncedSave();
    }));

    // Assessment name
    form.appendChild(this.field("Assessment Name", "text",
      this.state.assessmentName || this.getDefaultAssessmentName(),
      function (v) {
        self.state.assessmentName = v;
        self._debouncedSave();
      },
      "Optional — defaults to Organization Name + date and is used in exports."));

    wrap.appendChild(form);

    // Navigation
    var btns = h("div", { className: "ag-btn-group" });
    btns.appendChild(h("button", {
      className: "ag-btn ag-btn-secondary",
      onClick: function () { self.goToStep("welcome"); }
    }, "Back"));
    btns.appendChild(h("button", {
      className: "ag-btn ag-btn-primary",
      onClick: function () {
        var errors = self.validateScoping();
        if (errors.length > 0) {
          self.showScopingErrors(errors);
          return;
        }
        if (!self.state.assessmentName) {
          self.state.assessmentName = self.getDefaultAssessmentName();
        }
        self.clearMessage();
        self.markStep("scoping");
        self.saveToStorage();
        self.goToStep("phase1");
      }
    }, "Begin Assessment"));
    wrap.appendChild(btns);

    parent.appendChild(wrap);
  };

  AssessmentApp.prototype.markStep = function (stepId) {
    if (!this.state.completedSteps) this.state.completedSteps = [];
    if (this.state.completedSteps.indexOf(stepId) < 0) {
      this.state.completedSteps.push(stepId);
    }
  };

  AssessmentApp.prototype.clearFieldError = function (inputId) {
    var input = this.el.querySelector("#" + inputId);
    var errorId = inputId + "-error";
    var error = this.el.querySelector("#" + errorId);
    if (error && error.parentNode) error.parentNode.removeChild(error);
    if (!input) return;
    input.removeAttribute("aria-invalid");
    var describedBy = (input.getAttribute("aria-describedby") || "").split(/\s+/).filter(function (id) {
      return id && id !== errorId;
    });
    if (describedBy.length > 0) input.setAttribute("aria-describedby", describedBy.join(" "));
    else input.removeAttribute("aria-describedby");
  };

  AssessmentApp.prototype.showFieldError = function (inputId, message) {
    this.clearFieldError(inputId);
    var input = this.el.querySelector("#" + inputId);
    if (!input || !input.parentNode) return;
    var errorId = inputId + "-error";
    input.setAttribute("aria-invalid", "true");
    var describedBy = (input.getAttribute("aria-describedby") || "").split(/\s+/).filter(Boolean);
    describedBy.push(errorId);
    input.setAttribute("aria-describedby", describedBy.join(" "));
    input.parentNode.appendChild(h("div", { className: "ag-field-error", id: errorId }, message));
  };

  AssessmentApp.prototype.validateScoping = function () {
    var sc = this.state && this.state.scoping ? this.state.scoping : {};
    var errors = [];
    if (!sc.organizationName) {
      errors.push({ id: "ag-field-organization-name", message: "Organization Name is required." });
    }
    if (!sc.institutionType) {
      errors.push({ id: "ag-select-institution-type", message: "Institution Type is required." });
    }
    if (!sc.targetLevel) {
      errors.push({ id: "ag-select-target-governance-level", message: "Target Governance Level is required." });
    }
    return errors;
  };

  AssessmentApp.prototype.showScopingErrors = function (errors) {
    var self = this;
    errors.forEach(function (error) {
      self.showFieldError(error.id, error.message);
    });
    if (errors.length > 0) {
      this.setMessage("error", "Complete the required scoping fields", "Fix the highlighted fields before continuing.");
      var firstField = this.el.querySelector("#" + errors[0].id);
      if (firstField) firstField.focus();
    }
  };

  /* ---- Form helpers ---- */
  AssessmentApp.prototype.field = function (label, type, value, onChange, hint, options) {
    var self = this;
    options = options || {};
    var inputId = "ag-field-" + label.toLowerCase().replace(/\s+/g, "-");
    var wrap = h("div", { className: "ag-field" });
    var labelEl = h("label", { className: "ag-label", htmlFor: inputId });
    labelEl.appendChild(document.createTextNode(label));
    if (options.required) {
      labelEl.appendChild(h("span", { className: "ag-required", "aria-hidden": "true" }, " *"));
    }
    wrap.appendChild(labelEl);
    if (hint) wrap.appendChild(h("span", { className: "ag-hint", id: inputId + "-hint" }, hint));
    var input = h("input", {
      className: "ag-input",
      type: type,
      value: value || "",
      id: inputId,
      required: options.required ? "required" : null,
      "aria-describedby": hint ? inputId + "-hint" : null,
    });
    input.addEventListener("input", function () {
      self.clearFieldError(inputId);
      onChange(input.value);
    });
    wrap.appendChild(input);
    return wrap;
  };

  AssessmentApp.prototype.selectField = function (label, options, value, onChange, hint, config) {
    var self = this;
    config = config || {};
    var selectId = "ag-select-" + label.toLowerCase().replace(/\s+/g, "-");
    var wrap = h("div", { className: "ag-field" });
    var labelEl = h("label", { className: "ag-label", htmlFor: selectId });
    labelEl.appendChild(document.createTextNode(label));
    if (config.required) {
      labelEl.appendChild(h("span", { className: "ag-required", "aria-hidden": "true" }, " *"));
    }
    wrap.appendChild(labelEl);
    if (hint) wrap.appendChild(h("span", { className: "ag-hint", id: selectId + "-hint" }, hint));
    var sel = h("select", {
      className: "ag-select",
      id: selectId,
      required: config.required ? "required" : null,
      "aria-describedby": hint ? selectId + "-hint" : null,
    });
    options.forEach(function (o) {
      var opt = h("option", { value: o.value }, o.label);
      if (o.value === value) opt.selected = true;
      sel.appendChild(opt);
    });
    sel.addEventListener("change", function () {
      self.clearFieldError(selectId);
      onChange(sel.value);
    });
    wrap.appendChild(sel);
    return wrap;
  };

  AssessmentApp.prototype.checkboxGroup = function (label, items, onChange, hint) {
    var fieldset = h("fieldset", { className: "ag-field ag-fieldset" });
    fieldset.appendChild(h("legend", { className: "ag-label" }, label));
    if (hint) {
      fieldset.appendChild(hint);
    }
    var group = h("div", { className: "ag-check-group" });
    items.forEach(function (item) {
      var lbl = h("label", { className: "ag-check-label" });
      var cb = h("input", { type: "checkbox", value: String(item.value) });
      cb.checked = item.checked;
      cb.addEventListener("change", function () {
        var vals = [];
        group.querySelectorAll("input:checked").forEach(function (el) { vals.push(el.value); });
        onChange(vals);
      });
      lbl.appendChild(cb);
      if (item.description) {
        var wrap = h("span", { className: "ag-check-label-content" });
        wrap.appendChild(h("span", null, item.label));
        wrap.appendChild(h("span", { className: "ag-check-desc" }, item.description));
        lbl.appendChild(wrap);
      } else {
        lbl.appendChild(document.createTextNode(item.label));
      }
      group.appendChild(lbl);
    });
    fieldset.appendChild(group);
    return fieldset;
  };

  AssessmentApp.prototype.getAnswerMeta = function (answer) {
    if (answer === "yes") return { key: "yes", label: "Implemented" };
    if (answer === "partial") return { key: "partial", label: "Partial" };
    if (answer === "no") return { key: "no", label: "Gap" };
    if (answer === "na") return { key: "na", label: "N/A" };
    return null;
  };

  /* ================================================================
     D1: SPA ENHANCEMENTS — drawer, facilitator, yes-bars, solutions
     ================================================================ */

  /** Fetch the manifest row for a control id (empty object when missing). */
  AssessmentApp.prototype.getManifestCtrl = function (id) {
    if (this.manifestById && this.manifestById[id]) return this.manifestById[id];
    if (Array.isArray(this.manifest)) {
      for (var i = 0; i < this.manifest.length; i++) {
        if (this.manifest[i] && this.manifest[i].id === id) return this.manifest[i];
      }
    }
    return {};
  };

  /** Drawer notes are stored per-control outside the assessment state. */
  AssessmentApp.prototype.getDrawerNotes = function (id) {
    try { return localStorage.getItem(DRAWER_NOTES_PREFIX + id) || ""; }
    catch (_e) { return ""; }
  };
  AssessmentApp.prototype.setDrawerNotes = function (id, text) {
    try {
      if (text) localStorage.setItem(DRAWER_NOTES_PREFIX + id, text);
      else localStorage.removeItem(DRAWER_NOTES_PREFIX + id);
    } catch (_e) { /* ignore */ }
  };

  /** Toggle facilitator mode, persist, and re-render. */
  AssessmentApp.prototype.toggleFacilitatorMode = function () {
    this.facilitatorMode = !this.facilitatorMode;
    try { localStorage.setItem(FACILITATOR_MODE_KEY, this.facilitatorMode ? "1" : "0"); }
    catch (_e) { /* ignore */ }
    this.render();
  };

  /**
   * Render the three sector-calibration yes-bar badges (yes / partial / no)
   * using manifest `yesBar` / `partialBar` / `noBar` criteria. Hidden
   * entirely when none of the three fields are authored. Hover text is
   * provided via `title` so the badges stay compact in the row.
   */
  AssessmentApp.prototype.renderYesBarBadges = function (ctrl) {
    var m = this.getManifestCtrl(ctrl.id);
    var defs = [
      { key: "yes",     cls: "yes-bar-badge",     label: "Yes bar",     text: m.yesBar },
      { key: "partial", cls: "partial-bar-badge", label: "Partial bar", text: m.partialBar },
      { key: "no",      cls: "no-bar-badge",      label: "No bar",      text: m.noBar },
    ];
    var anyAuthored = defs.some(function (d) { return isAuthored(d.text); });
    if (!anyAuthored && !isAuthored(m.sectorYesBar)) return null;

    var wrap = h("div", { className: "yes-bar-row", "aria-label": "Calibration bars" });
    defs.forEach(function (d) {
      if (!isAuthored(d.text)) return;
      wrap.appendChild(h("span", {
        className: "yes-bar-badge " + d.cls,
        title: d.text,
        "data-bar": d.key,
      }, d.label));
    });

    // Sector-specific yes bar (hover preview only when authored for the selected sector).
    var sector = this.state && this.state.selectedSector;
    if (sector && m.sectorYesBar && isAuthored(m.sectorYesBar[sector])) {
      wrap.appendChild(h("span", {
        className: "yes-bar-badge sector-bar-badge",
        title: m.sectorYesBar[sector],
        "data-bar": "sector",
      }, "Sector: " + sector));
    }

    // Optional partial/no one-liners below the badges (task spec D1.c).
    var extras = h("div", { className: "calibration-bar-lines" });
    if (isAuthored(m.partialBar)) {
      extras.appendChild(h("div", { className: "calibration-bar-line partial" },
        [h("strong", null, "Partial: "), document.createTextNode(m.partialBar)]));
    }
    if (isAuthored(m.noBar)) {
      extras.appendChild(h("div", { className: "calibration-bar-line no" },
        [h("strong", null, "No: "), document.createTextNode(m.noBar)]));
    }
    if (extras.childNodes.length) wrap.appendChild(extras);

    return wrap;
  };

  /**
   * Render the inline facilitator panel (ask + followUp) shown when
   * facilitator mode is on. Returns null when the control has no
   * authored facilitatorNotes.ask (spec: do not render for TODOs).
   */
  AssessmentApp.prototype.renderFacilitatorPanel = function (ctrl) {
    var self = this;
    var m = this.getManifestCtrl(ctrl.id);
    var notes = m && m.facilitatorNotes;
    if (!notes || !isAuthored(notes.ask)) return null;

    var panel = h("div", { className: "facilitator-panel", role: "group",
      "aria-label": "Facilitator prompts for " + ctrl.id });
    panel.appendChild(h("div", { className: "facilitator-panel-label" }, "🎤 Facilitator prompt"));
    panel.appendChild(h("p", { className: "facilitator-ask" }, notes.ask));
    if (isAuthored(notes.followUp)) {
      panel.appendChild(h("p", { className: "facilitator-followup" },
        [h("strong", null, "Follow up: "), document.createTextNode(notes.followUp)]));
    }
    if (typeof notes.timeBudgetMinutes === "number" && notes.timeBudgetMinutes > 0) {
      panel.appendChild(h("p", { className: "facilitator-time" },
        "Time budget: " + notes.timeBudgetMinutes + " min"));
    }
    panel.appendChild(h("button", {
      className: "ag-btn ag-btn-sm ag-btn-secondary facilitator-next",
      type: "button",
      onClick: function () { self.focusNextControlCard(ctrl.id); },
    }, "Next control →"));
    return panel;
  };

  /** Move focus to the next control card (facilitator-mode workshop flow). */
  AssessmentApp.prototype.focusNextControlCard = function (currentId) {
    var cards = this.el.querySelectorAll(".ag-control-card");
    for (var i = 0; i < cards.length; i++) {
      if (cards[i].getAttribute("data-control-id") === currentId) {
        var next = cards[i + 1];
        if (next) {
          next.scrollIntoView({ behavior: "smooth", block: "start" });
          var btn = next.querySelector(".ag-answer-btn");
          if (btn && btn.focus) btn.focus();
        }
        return;
      }
    }
  };

  /**
   * Render solution recommendation cards for the control using the
   * solutions-lock metadata. Returns null when no solutions are mapped.
   */
  AssessmentApp.prototype.renderSolutionCards = function (ctrl) {
    var m = this.getManifestCtrl(ctrl.id);
    var solutions = Array.isArray(m.solutions) ? m.solutions : [];
    var wrap = h("div", { className: "solution-card-list" });
    if (!solutions.length) {
      wrap.appendChild(h("p", { className: "solution-empty" },
        "No solution mappings yet — manual verification required."));
      return wrap;
    }
    var lock = this.solutionsLockById || {};
    solutions.forEach(function (s) {
      if (!s) return;
      var id = typeof s === "string" ? s : s.id;
      var tier = typeof s === "object" ? s.tier : null;
      var role = typeof s === "object" ? s.role : null;
      var entry = lock[id] || null;
      var name = entry && entry.name ? entry.name : id;
      var url = entry && entry.url ? entry.url : (SOLUTIONS_BASE_URL + id);
      var card = h("a", {
        className: "solution-card",
        href: url,
        target: "_blank",
        rel: "noopener noreferrer",
        "data-solution-id": id,
      });
      card.appendChild(h("span", { className: "solution-card-name" }, name));
      var meta = h("span", { className: "solution-card-meta" });
      if (tier) {
        meta.appendChild(h("span", { className: "solution-card-tier tier-" + tier },
          "Tier " + tier));
      }
      if (role) {
        meta.appendChild(h("span", { className: "solution-card-role role-" + role }, role));
      }
      if (entry && entry.version) {
        meta.appendChild(h("span", { className: "solution-card-version" }, "v" + entry.version));
      }
      if (meta.childNodes.length) card.appendChild(meta);
      if (entry && entry.summary) {
        card.appendChild(h("span", { className: "solution-card-summary" }, entry.summary));
      }
      wrap.appendChild(card);
    });
    return wrap;
  };

  /**
   * Render the evidence drawer body for a control. Graceful-degrades on
   * TODO fields: missing manual_question/evidence/facilitator fields are
   * replaced with "content pending" placeholders rather than "undefined".
   */
  AssessmentApp.prototype.renderDrawer = function (ctrl) {
    var self = this;
    var m = this.getManifestCtrl(ctrl.id);
    var wrap = h("div", { className: "control-drawer-inner" });

    // Header block
    var header = h("div", { className: "control-drawer-header" });
    header.appendChild(h("div", { className: "control-drawer-id" }, ctrl.id));
    header.appendChild(h("h3", { className: "control-drawer-title" }, ctrl.title));
    var meta = h("div", { className: "control-drawer-meta" });
    meta.appendChild(h("span", { className: "control-drawer-pillar" },
      "Pillar " + ctrl.pillar));
    if (ctrl.targetLevel) {
      meta.appendChild(h("span", {
        className: "control-drawer-tier tier-" + ctrl.targetLevel,
      }, ctrl.targetLevel));
    }
    if (Array.isArray(ctrl.surfaces) && ctrl.surfaces.length) {
      ctrl.surfaces.slice(0, 4).forEach(function (s) {
        meta.appendChild(h("span", { className: "control-drawer-surface" }, s));
      });
    }
    header.appendChild(meta);
    wrap.appendChild(header);

    // Question / objective
    var questionSec = h("section", { className: "control-drawer-section" });
    questionSec.appendChild(h("h4", null, "Question"));
    var question = (m && isAuthored(m.manual_question))
      ? m.manual_question
      : (ctrl.title + " (detailed question pending)");
    questionSec.appendChild(h("p", null, question));
    wrap.appendChild(questionSec);

    // Verify-in chips
    var verifyIn = (m && Array.isArray(m.verifyIn)) ? m.verifyIn : [];
    var verifySec = h("section", { className: "control-drawer-section" });
    verifySec.appendChild(h("h4", null, "Verify in"));
    if (verifyIn.length) {
      var chips = h("div", { className: "verify-in-chips" });
      verifyIn.forEach(function (entry) {
        if (!entry) return;
        var url = typeof entry === "string" ? entry : entry.url;
        var label = typeof entry === "string"
          ? entry
          : (entry.portal ? (entry.portal + (entry.path ? " — " + entry.path : ""))
                          : (entry.label || entry.name || entry.url || ""));
        if (!label) return;
        if (url) {
          chips.appendChild(h("a", {
            className: "verify-in-chip",
            href: url,
            target: "_blank",
            rel: "noopener noreferrer",
          }, label));
        } else {
          chips.appendChild(h("span", { className: "verify-in-chip" }, label));
        }
      });
      verifySec.appendChild(chips);
    } else {
      verifySec.appendChild(h("p", { className: "control-drawer-pending" },
        "Portal verification paths being authored."));
    }
    wrap.appendChild(verifySec);

    // Evidence expected
    var evSec = h("section", { className: "control-drawer-section" });
    evSec.appendChild(h("h4", null, "Evidence expected"));
    var evidence = (m && Array.isArray(m.evidenceExpected)) ? m.evidenceExpected : [];
    var authoredEvidence = evidence.filter(function (e) { return isAuthored(e); });
    if (authoredEvidence.length) {
      var ul = h("ul", { className: "evidence-list" });
      authoredEvidence.forEach(function (e) {
        ul.appendChild(h("li", null, String(e)));
      });
      evSec.appendChild(ul);
    } else {
      evSec.appendChild(h("p", { className: "control-drawer-pending" },
        "Evidence list being authored — contact your governance lead for guidance."));
    }
    wrap.appendChild(evSec);

    // Facilitator (only when authored — mirrors D1.a spec)
    if (m && m.facilitatorNotes && isAuthored(m.facilitatorNotes.ask)) {
      var facSec = h("section", { className: "control-drawer-section" });
      facSec.appendChild(h("h4", null, "Facilitator prompt"));
      facSec.appendChild(h("p", { className: "facilitator-ask" }, m.facilitatorNotes.ask));
      if (isAuthored(m.facilitatorNotes.followUp)) {
        facSec.appendChild(h("p", { className: "facilitator-followup" },
          [h("strong", null, "Follow up: "),
           document.createTextNode(m.facilitatorNotes.followUp)]));
      }
      wrap.appendChild(facSec);
    }

    // D2: Collector evidence (if any rows imported for this control).
    var ce = this.getCollectorEvidenceFor(ctrl.id);
    if (ce && ((ce.evidence && ce.evidence.length) || ce.status)) {
      var ceSec = h("section", { className: "control-drawer-section collector-evidence-section" });
      ceSec.appendChild(h("h4", null, "Collector evidence"));
      var metaParts = [];
      if (ce.runId) metaParts.push("Run: " + ce.runId);
      if (ce.importedAt) metaParts.push("imported " + fmtDate(ce.importedAt));
      if (ce.status) metaParts.push("aggregate: " + ce.status);
      if (metaParts.length) {
        ceSec.appendChild(h("p", { className: "collector-evidence-meta" }, metaParts.join(" · ")));
      }
      var ceList = h("ul", { className: "collector-evidence-list" });
      (ce.evidence || []).forEach(function (ev) {
        var li = h("li", { className: "collector-evidence-item" });
        var keyTxt = ev.key || "(unkeyed)";
        li.appendChild(h("strong", { className: "collector-evidence-key" }, keyTxt));
        if (ev.status) {
          li.appendChild(h("span", { className: "collector-evidence-status status-" + ev.status },
            " " + ev.status));
        }
        if (ev.raw) {
          li.appendChild(document.createTextNode(" — "));
          li.appendChild(h("span", { className: "collector-evidence-raw" }, ev.raw));
        }
        if (ev.collectedAt) {
          li.appendChild(h("span", { className: "collector-evidence-at" }, " · " + ev.collectedAt));
        }
        ceList.appendChild(li);
      });
      ceSec.appendChild(ceList);
      wrap.appendChild(ceSec);
    }

    // Recommended solutions (D1.d)
    var solSec = h("section", { className: "control-drawer-section" });
    solSec.appendChild(h("h4", null, "Recommended solutions"));
    solSec.appendChild(this.renderSolutionCards(ctrl));
    wrap.appendChild(solSec);

    // Personal notes textarea (persists to localStorage).
    var notesSec = h("section", { className: "control-drawer-section" });
    notesSec.appendChild(h("h4", null, "Notes"));
    var notesArea = h("textarea", {
      className: "ag-textarea control-drawer-notes",
      id: "control-drawer-notes-" + ctrl.id,
      placeholder: "Your private notes for this control (stored on this device)…",
      "aria-label": "Drawer notes for control " + ctrl.id,
      rows: "4",
    });
    notesArea.value = this.getDrawerNotes(ctrl.id);
    var persistNotes = debounce(function () {
      self.setDrawerNotes(ctrl.id, notesArea.value);
    }, 400);
    notesArea.addEventListener("input", persistNotes);
    notesSec.appendChild(notesArea);
    wrap.appendChild(notesSec);

    return wrap;
  };

  /** Ensure a drawer root + backdrop exist at the app root. */
  AssessmentApp.prototype._ensureDrawerRoot = function () {
    if (this._drawerRoot && this._drawerRoot.parentNode) return;
    var backdrop = h("div", {
      className: "control-drawer-backdrop",
      "aria-hidden": "true",
    });
    var drawer = h("aside", {
      className: "control-drawer",
      role: "dialog",
      "aria-modal": "true",
      "aria-label": "Control evidence drawer",
      "aria-hidden": "true",
      tabindex: "-1",
    });
    var self = this;
    backdrop.addEventListener("click", function () { self.closeDrawer(); });
    drawer.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { e.preventDefault(); self.closeDrawer(); }
    });
    this.el.appendChild(backdrop);
    this.el.appendChild(drawer);
    this._drawerRoot = drawer;
    this._drawerBackdrop = backdrop;
  };

  /** Open the evidence drawer for a control. */
  AssessmentApp.prototype.openDrawer = function (ctrl) {
    if (!ctrl) return;
    this._ensureDrawerRoot();
    var drawer = this._drawerRoot;
    drawer.innerHTML = "";

    var header = h("div", { className: "control-drawer-bar" });
    var closeBtn = h("button", {
      className: "control-drawer-close",
      type: "button",
      "aria-label": "Close evidence drawer",
    }, "×");
    var self = this;
    closeBtn.addEventListener("click", function () { self.closeDrawer(); });
    header.appendChild(closeBtn);
    drawer.appendChild(header);
    drawer.appendChild(this.renderDrawer(ctrl));

    drawer.classList.add("open");
    drawer.setAttribute("aria-hidden", "false");
    this._drawerBackdrop.classList.add("open");
    this._drawerBackdrop.setAttribute("aria-hidden", "false");
    this._drawerCtrlId = ctrl.id;
    this._drawerPrevFocus = document.activeElement;
    closeBtn.focus();
  };

  AssessmentApp.prototype.closeDrawer = function () {
    if (!this._drawerRoot) return;
    this._drawerRoot.classList.remove("open");
    this._drawerRoot.setAttribute("aria-hidden", "true");
    if (this._drawerBackdrop) {
      this._drawerBackdrop.classList.remove("open");
      this._drawerBackdrop.setAttribute("aria-hidden", "true");
    }
    this._drawerCtrlId = null;
    if (this._drawerPrevFocus && typeof this._drawerPrevFocus.focus === "function") {
      this._drawerPrevFocus.focus();
    }
    this._drawerPrevFocus = null;
  };

  /* ================================================================
     STEP 3: PHASE 1 — CONTROL-LEVEL ASSESSMENT
     ================================================================ */
  AssessmentApp.prototype.renderPhase1 = function (parent) {
    var self = this;
    var wrap = h("div", {
      className: "phase1-wrap" + (this.facilitatorMode ? " facilitator-mode" : ""),
    });
    var completion = this.getAssessmentCompletion();
    var answered = completion.answered;
    var total = completion.total;
    var pct = total > 0 ? Math.round((answered / total) * 100) : 0;
    var gaps = this.getGapControls();
    var drilldownStats = this.getDrilldownStats();

    wrap.appendChild(h("h2", { style: "font-size:1.3rem;margin-bottom:0.3rem", "data-step-heading": "true", tabindex: "-1" }, "Phase 1: Control-Level Assessment"));
    wrap.appendChild(h("p", { className: "ag-card-subtitle" },
      "For each control, indicate your organization's implementation status before moving on to Drill-Down or Results."
    ));

    var callout = h("div", { className: "ag-callout" });
    callout.appendChild(h("strong", null, "How to answer: "));
    callout.appendChild(document.createTextNode("Yes = fully in place, Partial = some aspects implemented and worth refining in Drill-Down, No = not yet implemented, and N/A = not applicable and excluded from scoring. "));
    callout.appendChild(document.createTextNode("Browser drafts save automatically on this device, and Save to File creates the shareable JSON record."));
    wrap.appendChild(callout);

    var progressText = h("div", { className: "ag-progress-text" },
      answered + " of " + total + " controls answered (" + pct + "%)");
    wrap.appendChild(progressText);
    var progress = h("div", { className: "ag-progress" });
    progress.appendChild(h("div", {
      className: "ag-progress-bar",
      role: "progressbar",
      "aria-valuenow": String(pct),
      "aria-valuemin": "0",
      "aria-valuemax": "100",
      "aria-label": "Assessment progress",
      style: "width:" + pct + "%",
    }));
    wrap.appendChild(progress);

    wrap.appendChild(h("div", {
      className: "ag-sr-only",
      "aria-live": "polite",
      "aria-atomic": "true",
      id: "ag-progress-live",
    }));

    var topBtns = h("div", { className: "ag-btn-group", style: "margin-bottom:1rem" });
    topBtns.appendChild(h("button", {
      className: "ag-btn ag-btn-sm ag-btn-secondary",
      type: "button",
      onClick: function () { self.exportJSON(); }
    }, "Save to File"));
    topBtns.appendChild(h("button", {
      className: "ag-info-btn",
      type: "button",
      onClick: function () { self.showScoringModal(); }
    }, "\u2139 How Scoring Works"));
    topBtns.appendChild(h("button", {
      id: "facilitator-toggle",
      className: "ag-btn ag-btn-sm " + (self.facilitatorMode ? "ag-btn-primary" : "ag-btn-secondary"),
      type: "button",
      "aria-pressed": self.facilitatorMode ? "true" : "false",
      onClick: function () { self.toggleFacilitatorMode(); },
    }, "🎤 Facilitator Mode: " + (self.facilitatorMode ? "On" : "Off")));
    // D2: Import collector evidence (CSV/JSON) — button + drop zone live inline.
    topBtns.appendChild(self.renderCollectorImportControls());
    wrap.appendChild(topBtns);

    if (!completion.complete) {
      wrap.appendChild(h("div", { className: "ag-disclaimer" },
        completion.remaining + " control" + (completion.remaining == 1 ? "" : "s") +
        " still need an answer before you can continue to Drill-Down or Results."
      ));
    } else if (gaps.length > 0) {
      var drilldownText = "You have " + gaps.length + " gap control" + (gaps.length == 1 ? "" : "s") + ".";
      if (drilldownStats.totalQuestions > 0) {
        drilldownText += " Drill-Down includes " + drilldownStats.totalQuestions +
          " verification check" + (drilldownStats.totalQuestions == 1 ? "" : "s") +
          " for your selected target governance level.";
      }
      drilldownText += " If you skip Drill-Down, Partial answers keep their default 50% score and Results stay preliminary.";
      wrap.appendChild(h("div", { className: "ag-disclaimer", style: "background:var(--md-default-fg-color--lightest);border-left-color:var(--md-primary-fg-color)" }, drilldownText));
    } else {
      wrap.appendChild(h("div", { className: "ag-disclaimer", style: "background:var(--ag-green-bg);border-left-color:var(--ag-green)" },
        "No gap controls require Drill-Down for the selected target governance level. You can continue directly to Results."
      ));
    }

    Object.keys(this.data.pillars).sort().forEach(function (pillarKey) {
      var pillarNum = parseInt(pillarKey, 10);
      var pillarName = self.data.pillars[pillarKey].name;
      var controls = self.data.controls.filter(function (c) { return c.pillar === pillarNum; });
      var answeredInPillar = controls.filter(function (c) { return self.hasAnsweredControl(c.id); }).length;
      var allAnswered = answeredInPillar === controls.length;

      var group = h("div", { className: "ag-pillar-group" });
      var header = h("div", {
        className: "ag-pillar-header" + (allAnswered ? " collapsed" : ""),
        role: "button",
        tabindex: "0",
        "aria-expanded": allAnswered ? "false" : "true",
        "aria-controls": "ag-pillar-" + pillarNum,
      });
      header.appendChild(h("span", { className: "ag-pillar-name" }, "Pillar " + pillarNum + " \u2014 " + pillarName));
      header.appendChild(h("span", { className: "ag-pillar-count" }, answeredInPillar + "/" + controls.length));
      group.appendChild(header);

      var controlsContainer = h("div", {
        className: "ag-pillar-controls" + (allAnswered ? " collapsed" : ""),
        id: "ag-pillar-" + pillarNum,
      });
      controls.forEach(function (ctrl) {
        controlsContainer.appendChild(self.renderControlCard(ctrl));
      });
      group.appendChild(controlsContainer);

      var toggle = function () {
        var isCollapsed = controlsContainer.classList.contains("collapsed");
        controlsContainer.classList.toggle("collapsed", !isCollapsed);
        header.classList.toggle("collapsed", !isCollapsed);
        header.setAttribute("aria-expanded", isCollapsed ? "true" : "false");
      };
      header.addEventListener("click", toggle);
      header.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); toggle(); }
      });

      wrap.appendChild(group);
    });

    var btns = h("div", { className: "ag-btn-group" });
    btns.appendChild(h("button", {
      className: "ag-btn ag-btn-secondary",
      type: "button",
      onClick: function () { self.goToStep("scoping"); }
    }, "Back to Scoping"));

    if (gaps.length > 0) {
      btns.appendChild(h("button", {
        className: "ag-btn ag-btn-primary",
        type: "button",
        disabled: completion.complete ? null : "disabled",
        onClick: function () {
          if (!completion.complete) return;
          self.markStep("phase1");
          self.saveToStorage();
          self.goToStep("phase2");
        }
      }, "Continue to Drill-Down (" + gaps.length + " gap control" + (gaps.length == 1 ? "" : "s") + ")"));
    }

    btns.appendChild(h("button", {
      className: "ag-btn " + (gaps.length > 0 ? "ag-btn-secondary" : "ag-btn-primary"),
      type: "button",
      disabled: completion.complete ? null : "disabled",
      onClick: function () {
        if (!completion.complete) return;
        self.markStep("phase1");
        self.saveToStorage();
        if (gaps.length > 0) {
          self.setMessage(
            "warning",
            "Results are preliminary",
            "You skipped Drill-Down. Partial answers keep their default 50% score until you complete the verification checks."
          );
        } else {
          self.clearMessage();
        }
        self.goToStep("results");
      }
    }, gaps.length > 0 ? "View Preliminary Results" : "View Results"));
    wrap.appendChild(btns);

    parent.appendChild(wrap);
  };

  AssessmentApp.prototype.renderControlCard = function (ctrl) {
    var self = this;
    var resp = this.state.responses[ctrl.id] || {};
    var cls = "ag-control-card control-row";
    if (resp.answer === "yes") cls += " answered";
    else if (resp.answer === "partial") cls += " partial";
    else if (resp.answer === "no") cls += " gap";
    if (this.facilitatorMode) cls += " facilitator-active";

    var statusMeta = this.getAnswerMeta(resp.answer);
    var card = h("div", { className: cls, "data-control-id": ctrl.id, tabindex: "-1" });

    var header = h("div", { className: "ag-control-header" });
    var left = h("div", { style: "flex:1" });
    var titleLine = h("div", { style: "display:flex;align-items:center;gap:0.5rem;flex-wrap:wrap" });
    titleLine.appendChild(h("span", { className: "ag-control-id" }, ctrl.id));
    titleLine.appendChild(h("span", { className: "ag-control-title" }, ctrl.title));
    var statusBadge = h("span", {
      className: "ag-status-chip" + (statusMeta ? " ag-status-" + statusMeta.key : " ag-status-empty"),
      "aria-hidden": statusMeta ? null : "true",
    }, statusMeta ? statusMeta.label : "Status pending");
    var statusText = h("span", { className: "ag-sr-only" }, "Status: " + (statusMeta ? statusMeta.label : "Not answered"));
    titleLine.appendChild(statusBadge);
    titleLine.appendChild(statusText);
    left.appendChild(titleLine);

    var badges = h("div", { className: "ag-control-badges", style: "margin-top:0.3rem" });
    if (ctrl.adoptionPhase) {
      var pCls = "ag-badge ag-badge-" + ctrl.adoptionPhase.priority.toLowerCase();
      badges.appendChild(h("span", { className: pCls }, "Phase " + ctrl.adoptionPhase.phase + " " + ctrl.adoptionPhase.priority));
    }
    if (ctrl.solutions && ctrl.solutions.length > 0) {
      badges.appendChild(h("span", { className: "ag-badge ag-badge-solution" }, "Automation"));
    }
    left.appendChild(badges);
    header.appendChild(left);

    // D1.a: "View evidence" button opens the slide-in drawer.
    var drawerBtn = h("button", {
      className: "control-drawer-trigger",
      type: "button",
      "aria-label": "View evidence, verification paths, and solutions for " + ctrl.id,
      onClick: function (e) { e.stopPropagation(); self.openDrawer(ctrl); },
    }, "View evidence ›");
    header.appendChild(drawerBtn);
    card.appendChild(header);

    var displayText = ctrl.questionText || ctrl.objective;
    var m = this.getManifestCtrl(ctrl.id);
    if (m && isAuthored(m.manual_question)) {
      displayText = m.manual_question;
    } else if (!displayText) {
      displayText = ctrl.title + " (detailed question pending)";
    }
    card.appendChild(h("div", { className: "ag-control-objective" }, displayText));

    var answerGroup = h("div", { className: "ag-answer-group", role: "group", "aria-label": "Implementation status for " + ctrl.id });
    ANSWERS.forEach(function (a) {
      var bcls = "ag-answer-btn";
      var isPressed = resp.answer === a.value;
      if (isPressed) bcls += " " + a.cls;
      var btn = h("button", {
        className: bcls,
        type: "button",
        "aria-label": "Mark " + ctrl.id + " as " + a.label,
        "aria-pressed": isPressed ? "true" : "false",
        onClick: function () {
          var nextMeta = self.getAnswerMeta(a.value);
          self.state.responses[ctrl.id] = self.state.responses[ctrl.id] || {};
          self.state.responses[ctrl.id].answer = a.value;
          self.saveToStorage();
          statusBadge.textContent = nextMeta ? nextMeta.label : "Status pending";
          statusBadge.className = "ag-status-chip" + (nextMeta ? " ag-status-" + nextMeta.key : " ag-status-empty");
          statusBadge.removeAttribute("aria-hidden");
          statusText.textContent = "Status: " + (nextMeta ? nextMeta.label : "Not answered");
          self.render();
          self.focusControlCard(ctrl.id);
          self.announce("Updated " + ctrl.id + " to " + (nextMeta ? nextMeta.label : a.label) + ".");
        }
      }, a.label);
      answerGroup.appendChild(btn);
    });
    card.appendChild(answerGroup);

    // D1.c: sector-calibration yes-bar badges (hidden on all-TODO controls).
    var yesBars = this.renderYesBarBadges(ctrl);
    if (yesBars) card.appendChild(yesBars);

    // D1.b: facilitator prompts (only when mode is on AND notes authored).
    if (this.facilitatorMode) {
      var facPanel = this.renderFacilitatorPanel(ctrl);
      if (facPanel) card.appendChild(facPanel);
    }

    var notesVisible = !!resp.notes;
    var notesBtn = h("button", {
      className: "ag-notes-toggle",
      type: "button",
      "aria-expanded": notesVisible ? "true" : "false",
      "aria-controls": "ag-notes-" + ctrl.id,
    }, resp.notes ? "Edit notes" : "Add notes");
    var notesArea = h("textarea", {
      className: "ag-textarea",
      id: "ag-notes-" + ctrl.id,
      style: "display:" + (notesVisible ? "block" : "none") + ";margin-top:0.4rem",
      placeholder: "Notes (optional)",
      value: resp.notes || "",
      "aria-label": "Notes for control " + ctrl.id,
    });
    notesArea.value = resp.notes || "";
    notesArea.addEventListener("input", function () {
      self.state.responses[ctrl.id] = self.state.responses[ctrl.id] || {};
      self.state.responses[ctrl.id].notes = notesArea.value;
      self._debouncedSave();
    });
    notesBtn.addEventListener("click", function () {
      var showing = notesArea.style.display != "none";
      notesArea.style.display = showing ? "none" : "block";
      notesBtn.textContent = showing ? (notesArea.value ? "Edit notes" : "Add notes") : "Hide notes";
      notesBtn.setAttribute("aria-expanded", showing ? "false" : "true");
      if (!showing) notesArea.focus();
    });
    card.appendChild(notesBtn);
    card.appendChild(notesArea);

    return card;
  };

  AssessmentApp.prototype.updateProgress = function () {
    var completion = this.getAssessmentCompletion();
    var answered = completion.answered;
    var total = completion.total;
    var pct = total > 0 ? Math.round((answered / total) * 100) : 0;
    var msg = answered + " of " + total + " controls answered (" + pct + "%)";
    var txt = this.el.querySelector(".ag-progress-text");
    if (txt) txt.textContent = msg;
    var bar = this.el.querySelector(".ag-progress-bar");
    if (bar) {
      bar.style.width = pct + "%";
      bar.setAttribute("aria-valuenow", String(pct));
    }
    var live = this.el.querySelector("#ag-progress-live");
    if (live) live.textContent = msg;
  };

  AssessmentApp.prototype.renderPhase2 = function (parent) {
    var self = this;
    var wrap = h("div");
    var gaps = this.getGapControls();
    var drilldownStats = this.getDrilldownStats();

    wrap.appendChild(h("h2", { style: "font-size:1.3rem;margin-bottom:0.3rem", "data-step-heading": "true", tabindex: "-1" }, "Phase 2: Drill-Down and Delegation"));
    wrap.appendChild(h("p", { className: "ag-card-subtitle" },
      "Answer detailed verification checks for gap controls, then export or import delegated sections as needed before reviewing Results."
    ));

    wrap.appendChild(h("div", { className: "ag-disclaimer", style: "background:var(--md-default-fg-color--lightest);border-left-color:var(--md-primary-fg-color)" },
      "Drill-Down refines Partial and No responses using verification checks that apply to your selected target governance level."
    ));

    var topBtns = h("div", { className: "ag-btn-group", style: "margin-bottom:1rem" });
    topBtns.appendChild(h("button", {
      className: "ag-btn ag-btn-sm ag-btn-secondary",
      type: "button",
      onClick: function () { self.exportJSON(); }
    }, "Save to File"));
    topBtns.appendChild(h("button", {
      className: "ag-info-btn",
      type: "button",
      onClick: function () { self.showScoringModal(); }
    }, "\u2139 How Scoring Works"));
    wrap.appendChild(topBtns);

    var collaboration = h("div", { className: "ag-collab-callout" });
    collaboration.appendChild(h("strong", null, "Delegate and re-import sections"));
    collaboration.appendChild(h("p", { style: "margin:0.3rem 0" },
      "Export a role-specific JSON section for a team member, then import the completed section back into this same assessment. Conflicting answers stay in your current assessment so you can review them manually."
    ));
    var collabBtns = h("div", { className: "ag-btn-group", style: "margin-top:0.75rem" });
    Object.keys(this.data.roleAssignments).forEach(function (role) {
      collabBtns.appendChild(h("button", {
        className: "ag-btn ag-btn-sm ag-btn-secondary",
        type: "button",
        onClick: function () { self.exportRoleSection(role); }
      }, "Export " + role));
    });
    collabBtns.appendChild(h("button", {
      className: "ag-btn ag-btn-sm ag-btn-primary",
      type: "button",
      onClick: function () { self.triggerImport("section"); }
    }, "Import Completed Section"));
    collaboration.appendChild(collabBtns);
    wrap.appendChild(collaboration);

    if (drilldownStats.totalQuestions > 0) {
      wrap.appendChild(h("div", { className: "ag-progress-text" },
        drilldownStats.answeredQuestions + " of " + drilldownStats.totalQuestions + " verification checks answered across " +
        drilldownStats.controlsWithQuestions + " gap control" + (drilldownStats.controlsWithQuestions == 1 ? "" : "s") + "."
      ));
    }

    if (gaps.length == 0) {
      wrap.appendChild(h("div", { className: "ag-card" },
        h("p", null, "No gap controls require Drill-Down for the selected target governance level. You can continue to Results.")));
    } else {
      var byPillar = {};
      gaps.forEach(function (c) {
        if (!byPillar[c.pillar]) byPillar[c.pillar] = [];
        byPillar[c.pillar].push(c);
      });

      Object.keys(byPillar).sort().forEach(function (pNum) {
        var pillarName = self.data.pillars[pNum].name;
        var controls = byPillar[pNum];

        var group = h("div", { className: "ag-pillar-group" });
        var header = h("div", { className: "ag-pillar-header ag-pillar-header-static" });
        header.appendChild(h("span", { className: "ag-pillar-name" },
          "Pillar " + pNum + " \u2014 " + pillarName));
        header.appendChild(h("span", { className: "ag-pillar-count" },
          controls.length + " gap" + (controls.length > 1 ? "s" : "")));
        group.appendChild(header);

        controls.forEach(function (ctrl) {
          group.appendChild(self.renderDrilldownCard(ctrl));
        });
        wrap.appendChild(group);
      });
    }

    var btns = h("div", { className: "ag-btn-group" });
    btns.appendChild(h("button", {
      className: "ag-btn ag-btn-secondary",
      type: "button",
      onClick: function () { self.goToStep("phase1"); }
    }, "Back to Assessment"));
    btns.appendChild(h("button", {
      className: "ag-btn ag-btn-primary",
      type: "button",
      onClick: function () {
        self.markStep("phase2");
        self.saveToStorage();
        if (drilldownStats.pendingControls > 0) {
          self.setMessage(
            "warning",
            "Results are still preliminary",
            drilldownStats.pendingControls + " gap control" + (drilldownStats.pendingControls == 1 ? " still has" : "s still have") +
            " unanswered verification checks. Complete Drill-Down for the most accurate refined scores."
          );
        } else {
          self.clearMessage();
        }
        self.goToStep("results");
      }
    }, drilldownStats.pendingControls > 0 ? "View Preliminary Results" : "View Results"));
    wrap.appendChild(btns);

    parent.appendChild(wrap);
  };

  AssessmentApp.prototype.renderDrilldownCard = function (ctrl) {
    var self = this;
    var card = h("div", { className: "ag-card" });
    var targetLevel = this.getTargetLevel();
    var questions = this.getVerificationCriteria(ctrl, targetLevel);
    var hiddenCriteria = this.getHiddenCriteriaCount(ctrl, targetLevel);

    var header = h("div", { style: "margin-bottom:0.75rem" });
    var titleLine = h("div", { style: "display:flex;align-items:center;gap:0.5rem;flex-wrap:wrap" });
    titleLine.appendChild(h("span", { className: "ag-control-id" }, ctrl.id));
    titleLine.appendChild(h("span", { className: "ag-control-title" }, ctrl.title));
    var resp = this.state.responses[ctrl.id] || {};
    var statusMeta = this.getAnswerMeta(resp.answer);
    if (statusMeta) {
      titleLine.appendChild(h("span", { className: "ag-status-chip ag-status-" + statusMeta.key }, statusMeta.label));
    }
    header.appendChild(titleLine);
    card.appendChild(header);

    if (hiddenCriteria > 0) {
      card.appendChild(h("p", { className: "ag-card-subtitle" },
        hiddenCriteria + " additional verification check" + (hiddenCriteria == 1 ? " applies" : "s apply") +
        " to a higher governance level and is hidden for this assessment target."
      ));
    }

    if (questions.length == 0) {
      card.appendChild(h("p", { style: "font-size:0.82rem;color:var(--md-default-fg-color--light)" },
        "No target-level verification checks are available for this control. The score will continue to use the top-level answer."));
      return card;
    }

    if (!this.state.drilldown[ctrl.id]) this.state.drilldown[ctrl.id] = {};
    var dd = this.state.drilldown[ctrl.id];

    var scoreEl = h("div", {
      style: "font-size:0.82rem;margin-bottom:0.5rem;font-weight:600"
    });
    var updateScore = function () {
      var answeredChecks = 0;
      var yesCount = 0;
      questions.forEach(function (question) {
        if (dd[question.id] === "yes") {
          yesCount++;
          answeredChecks++;
        } else if (dd[question.id] === "no") {
          answeredChecks++;
        }
      });
      var pct = answeredChecks > 0 ? Math.round((yesCount / questions.length) * 100) : (resp.answer === "partial" ? 50 : 0);
      if (answeredChecks > 0) {
        scoreEl.textContent = "Refined score: " + pct + "% (" + yesCount + "/" + questions.length + " checks met)";
      } else if (resp.answer === "partial") {
        scoreEl.textContent = "Current score: 50% until you answer the verification checks.";
      } else {
        scoreEl.textContent = "Current score: 0% until the verification checks are met.";
      }
      scoreEl.style.color = pct >= 80 ? "var(--ag-green)" : pct >= 50 ? "var(--ag-amber)" : "var(--ag-red)";
    };
    card.appendChild(scoreEl);

    questions.forEach(function (question) {
      var row = h("div", { className: "ag-drilldown-q" });
      row.appendChild(h("span", { style: "flex:1;margin-right:0.5rem" }, question.text));
      var btns = h("div", { className: "ag-drilldown-btns" });

      ["yes", "no"].forEach(function (val) {
        var bcls = "ag-answer-btn ag-btn-sm";
        var isPressed = dd[question.id] === val;
        if (isPressed) bcls += " " + (val === "yes" ? "selected" : "selected-no");
        var btn = h("button", {
          className: bcls,
          type: "button",
          "aria-label": (val === "yes" ? "Mark check as met for " : "Mark check as not met for ") + ctrl.id,
          "aria-pressed": isPressed ? "true" : "false",
          onClick: function () {
            dd[question.id] = val;
            self.saveToStorage();
            btns.querySelectorAll(".ag-answer-btn").forEach(function (b) {
              b.className = "ag-answer-btn ag-btn-sm";
              b.setAttribute("aria-pressed", "false");
            });
            btn.className = "ag-answer-btn ag-btn-sm " + (val === "yes" ? "selected" : "selected-no");
            btn.setAttribute("aria-pressed", "true");
            updateScore();
            self.announce("Updated verification check for " + ctrl.id + ".");
          }
        }, val === "yes" ? "Yes" : "No");
        btns.appendChild(btn);
      });

      row.appendChild(btns);
      card.appendChild(row);
    });

    updateScore();
    return card;
  };

  AssessmentApp.prototype.exportRoleSection = function (role) {
    var controlIds = this.data.roleAssignments[role] || [];
    var sectionData = {
      assessmentId: this.state.assessmentId,
      schemaVersion: STATE_SCHEMA_VERSION,
      dataVersion: this.data && this.data.version ? String(this.data.version) : "",
      frameworkVersion: this.data && this.data.frameworkVersion ? String(this.data.frameworkVersion) : "",
      sectionExport: {
        role: role,
        controlIds: controlIds,
        exportedAt: new Date().toISOString(),
        exportedBy: this.state.scoping.assessorName || "",
      },
      scoping: this.state.scoping,
      responses: {},
      drilldown: {},
    };
    var self = this;
    controlIds.forEach(function (cid) {
      if (self.state.responses[cid]) sectionData.responses[cid] = self.state.responses[cid];
      if (self.state.drilldown[cid]) sectionData.drilldown[cid] = self.state.drilldown[cid];
    });
    var blob = new Blob([JSON.stringify(sectionData, null, 2)], { type: "application/json" });
    var safeName = role.replace(/\s+/g, "-").toLowerCase();
    downloadBlob(blob, "assessment-section-" + safeName + ".json");
    this.setMessage(
      "success",
      "Role section exported",
      "Downloaded a role-specific section for " + role + ". Import the completed file back into this same assessment from Drill-Down."
    );
  };

  AssessmentApp.prototype.focusControlCard = function (controlId) {
    var card = this.el.querySelector('.ag-control-card[data-control-id="' + controlId + '"]');
    if (!card) return;
    var pillarControls = card.closest(".ag-pillar-controls");
    if (pillarControls && pillarControls.classList.contains("collapsed")) {
      pillarControls.classList.remove("collapsed");
      var pillarHeader = pillarControls.previousElementSibling;
      if (pillarHeader) {
        pillarHeader.classList.remove("collapsed");
        pillarHeader.setAttribute("aria-expanded", "true");
      }
    }
    card.scrollIntoView({ behavior: "smooth", block: "center" });
    card.classList.add("ag-highlight");
    card.focus();
    setTimeout(function () { card.classList.remove("ag-highlight"); }, 2000);
  };

  /* ================================================================
     STEP 5: RESULTS DASHBOARD
     ================================================================ */
  AssessmentApp.prototype.renderResults = function (parent) {
    var self = this;
    var wrap = h("div");
    var drilldownStats = this.getDrilldownStats();

    // Print header (hidden on screen, shown in print)
    var printHeader = h("div", { className: "ag-print-header", style: "display:none" });
    printHeader.appendChild(h("h1", null, "Governance Scorecard Report"));
    printHeader.appendChild(h("p", null,
      (this.state.assessmentName || "Assessment") + " — " + fmtDate(this.state.updatedAt)));
    printHeader.appendChild(h("p", null,
      "Organization: " + (this.state.scoping.organizationName || "—") +
      " | Assessor: " + (this.state.scoping.assessorName || "—")));
    wrap.appendChild(printHeader);

    wrap.appendChild(h("h2", { style: "font-size:1.3rem;margin-bottom:0.3rem", "data-step-heading": "true", tabindex: "-1" }, "Results Dashboard"));

    // Disclaimer
    wrap.appendChild(h("div", { className: "ag-disclaimer" },
      "This assessment helps support governance readiness. Scores reflect self-reported implementation " +
      "status and do not constitute a compliance certification."
    ));
    if (drilldownStats.pendingControls > 0) {
      wrap.appendChild(h("div", { className: "ag-disclaimer", style: "background:var(--md-default-fg-color--lightest);border-left-color:var(--md-primary-fg-color)" },
        drilldownStats.pendingControls + " gap control" + (drilldownStats.pendingControls === 1 ? " still has" : "s still have") +
        " unanswered verification checks. These results are preliminary until Drill-Down is complete."
      ));
    }

    // Tabs
    var tabs = [
      { id: "scorecard", label: "Executive Scorecard" },
      { id: "regulatory", label: "Regulatory Exposure" },
      { id: "zones", label: "Governance Levels" },
      { id: "gaps", label: "Gap Analysis" },
      { id: "responses", label: "Review Responses" },
      { id: "roadmap", label: "Remediation Roadmap" },
    ];
    var tabBar = h("div", { className: "ag-tabs", role: "tablist", "aria-label": "Results views" });
    var panels = h("div");

    var activateTab = function (tabEl, tabId) {
      tabBar.querySelectorAll(".ag-tab").forEach(function (b) {
        b.className = "ag-tab";
        b.setAttribute("aria-selected", "false");
        b.setAttribute("tabindex", "-1");
      });
      tabEl.className = "ag-tab active";
      tabEl.setAttribute("aria-selected", "true");
      tabEl.setAttribute("tabindex", "0");
      tabEl.focus();
      panels.querySelectorAll(".ag-tab-panel").forEach(function (p) { p.className = "ag-tab-panel"; });
      var panel = panels.querySelector('[data-tab="' + tabId + '"]');
      if (panel) panel.className = "ag-tab-panel active";
    };

    tabs.forEach(function (t, idx) {
      var tabId = "ag-tab-" + t.id;
      var panelId = "ag-panel-" + t.id;
      var tab = h("button", {
        className: "ag-tab" + (idx === 0 ? " active" : ""),
        role: "tab",
        id: tabId,
        "aria-selected": idx === 0 ? "true" : "false",
        "aria-controls": panelId,
        tabindex: idx === 0 ? "0" : "-1",
        onClick: function () { activateTab(tab, t.id); },
        onKeydown: function (e) {
          var tabEls = Array.prototype.slice.call(tabBar.querySelectorAll(".ag-tab"));
          var curIdx = tabEls.indexOf(tab);
          var nextIdx = -1;
          if (e.key === "ArrowRight" || e.key === "ArrowDown") {
            nextIdx = (curIdx + 1) % tabEls.length;
          } else if (e.key === "ArrowLeft" || e.key === "ArrowUp") {
            nextIdx = (curIdx - 1 + tabEls.length) % tabEls.length;
          } else if (e.key === "Home") {
            nextIdx = 0;
          } else if (e.key === "End") {
            nextIdx = tabEls.length - 1;
          }
          if (nextIdx >= 0) {
            e.preventDefault();
            var nextTab = tabEls[nextIdx];
            var nextId = tabs[nextIdx].id;
            activateTab(nextTab, nextId);
          }
        }
      }, t.label);
      tabBar.appendChild(tab);

      var panel = h("div", {
        className: "ag-tab-panel" + (idx === 0 ? " active" : ""),
        "data-tab": t.id,
        role: "tabpanel",
        id: panelId,
        "aria-labelledby": tabId,
      });
      switch (t.id) {
        case "scorecard": self.renderScorecard(panel); break;
        case "regulatory": self.renderRegulatory(panel); break;
        case "zones": self.renderZones(panel); break;
        case "gaps": self.renderGaps(panel); break;
        case "responses": self.renderResponseReview(panel); break;
        case "roadmap": self.renderRoadmap(panel); break;
      }
      panels.appendChild(panel);
    });

    wrap.appendChild(tabBar);
    wrap.appendChild(panels);

    // Collaboration callout
    var collabCard = h("div", { className: "ag-collab-callout" });
    collabCard.appendChild(h("strong", null, "Delegate Sections to Team Members"));
    collabCard.appendChild(h("p", { style: "margin:0.3rem 0" },
      "Export role-specific sections as JSON for admins to complete independently. " +
      "Import completed sections back during Drill-Down, where conflicts stay in the current assessment for manual review."));
    collabCard.appendChild(h("button", {
      className: "ag-btn ag-btn-sm ag-btn-secondary",
      type: "button",
      onClick: function () { self.goToStep("phase2"); }
    }, "Manage Delegated Sections"));
    wrap.appendChild(collabCard);

    // Re-render charts on dark mode toggle
    var observer = new MutationObserver(function (mutations) {
      mutations.forEach(function (m) {
        if (m.attributeName === "data-md-color-scheme") {
          self.charts.forEach(function (c) { try { c.destroy(); } catch (e) { /* */ } });
          self.charts = [];
          // Re-render charts by finding canvases and recreating
          var radarCanvas = panels.querySelector('[data-tab="scorecard"] canvas');
          var zoneCanvas = panels.querySelector('[data-tab="zones"] canvas');
          if (radarCanvas) self.renderRadarChart(radarCanvas);
          if (zoneCanvas) self.renderZoneChart(zoneCanvas);
        }
      });
    });
    observer.observe(document.documentElement, { attributes: true, attributeFilter: ["data-md-color-scheme"] });
    this._observers.push(observer);

    // Navigation
    var btns = h("div", { className: "ag-btn-group" });
    btns.appendChild(h("button", {
      className: "ag-btn ag-btn-secondary",
      type: "button",
      onClick: function () { self.goToStep("phase1"); }
    }, "Back to Assessment"));
    btns.appendChild(h("button", {
      className: "ag-btn ag-btn-primary",
      type: "button",
      onClick: function () {
        self.markStep("results");
        self.saveToStorage();
        self.goToStep("export");
      }
    }, "Export Results"));
    wrap.appendChild(btns);

    parent.appendChild(wrap);
  };

  /* ---- Scorecard tab ---- */
  AssessmentApp.prototype.renderScorecard = function (panel) {
    var overall = this.getOverallScore();
    var grid = h("div", { className: "ag-dashboard ag-dashboard-3col" });

    // Overall score
    var scoreCard = h("div", { className: "ag-card", style: "text-align:center" });
    scoreCard.appendChild(h("div", {
      className: "ag-score-big " + ragClass(overall || 0)
    }, (overall !== null ? overall + "%" : "—")));
    scoreCard.appendChild(h("div", { className: "ag-score-label" }, "Overall Score"));
    grid.appendChild(scoreCard);

    // Answered count
    var answered = this.getAnsweredControlCount();
    var total = this.data.controls.length;
    var countCard = h("div", { className: "ag-card", style: "text-align:center" });
    countCard.appendChild(h("div", { className: "ag-score-big", style: "color:var(--md-primary-fg-color)" },
      answered + "/" + total));
    countCard.appendChild(h("div", { className: "ag-score-label" }, "Controls Assessed"));
    grid.appendChild(countCard);

    // Gaps
    var gapCount = this.getGapControls().length;
    var gapCard = h("div", { className: "ag-card", style: "text-align:center" });
    gapCard.appendChild(h("div", {
      className: "ag-score-big " + (gapCount > 10 ? "red" : gapCount > 5 ? "amber" : "green")
    }, String(gapCount)));
    gapCard.appendChild(h("div", { className: "ag-score-label" }, "Gaps Identified"));
    grid.appendChild(gapCard);

    panel.appendChild(grid);

    // Pillar bars
    var self = this;
    var barSection = h("div", { className: "ag-card", style: "margin-top:1rem" });
    barSection.appendChild(h("div", { className: "ag-card-title" }, "Score by Pillar"));
    [1, 2, 3, 4].forEach(function (p) {
      var score = self.getPillarScore(p);
      var pct = score !== null ? score : 0;
      barSection.appendChild(self.renderRagBar(
        "Pillar " + p + " — " + self.data.pillars[String(p)].name, pct
      ));
    });
    panel.appendChild(barSection);

    // Radar chart
    var chartCard = h("div", { className: "ag-card", style: "margin-top:1rem" });
    chartCard.appendChild(h("div", { className: "ag-card-title" }, "Pillar Radar"));
    var chartWrap = h("div", { className: "ag-chart-container" });
    var canvas = h("canvas");
    chartWrap.appendChild(canvas);
    chartCard.appendChild(chartWrap);
    panel.appendChild(chartCard);

    // Render chart after DOM append
    var self2 = this;
    setTimeout(function () { self2.renderRadarChart(canvas); }, 50);
  };

  AssessmentApp.prototype.renderRagBar = function (label, pct) {
    var bar = h("div", { className: "ag-rag-bar" });
    bar.appendChild(h("span", { className: "ag-rag-label" }, label));
    var track = h("div", { className: "ag-rag-track" });
    track.appendChild(h("div", {
      className: "ag-rag-fill " + ragClass(pct),
      style: "width:" + clamp(pct, 0, 100) + "%"
    }));
    bar.appendChild(track);
    bar.appendChild(h("span", { className: "ag-rag-value" },
      (pct !== null ? pct + "%" : "—")));
    return bar;
  };

  AssessmentApp.prototype.renderRadarChart = function (canvas) {
    if (typeof Chart === "undefined") return;
    var self = this;
    var labels = [1, 2, 3, 4].map(function (p) {
      return "P" + p + " " + self.data.pillars[String(p)].name;
    });
    var scores = [1, 2, 3, 4].map(function (p) {
      return self.getPillarScore(p) || 0;
    });

    var isDark = document.documentElement.getAttribute("data-md-color-scheme") === "slate";
    var gridColor = isDark ? "rgba(255,255,255,0.15)" : "rgba(0,0,0,0.1)";
    var textColor = isDark ? "#ccc" : "#666";

    var chart = new Chart(canvas, {
      type: "radar",
      data: {
        labels: labels,
        datasets: [{
          label: "Score %",
          data: scores,
          backgroundColor: "rgba(63, 81, 181, 0.2)",
          borderColor: "rgba(63, 81, 181, 0.8)",
          borderWidth: 2,
          pointBackgroundColor: "rgba(63, 81, 181, 1)",
        }],
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
        plugins: { legend: { display: false } },
        scales: {
          r: {
            beginAtZero: true,
            max: 100,
            ticks: { stepSize: 20, color: textColor, backdropColor: "transparent" },
            grid: { color: gridColor },
            pointLabels: { color: textColor, font: { size: 11 } },
            angleLines: { color: gridColor },
          },
        },
      },
    });
    this.charts.push(chart);
  };

  /* ---- Regulatory tab ---- */
  var REGULATION_NOTES = {
    "FINRA AI Supervision and Governance":
      "Note: FINRA Regulatory Notice 25-07 addresses workplace modernization. " +
      "Its AI governance scope is limited to recordkeeping for AI-generated communications.",
  };

  AssessmentApp.prototype.renderRegulatory = function (panel) {
    var self = this;
    var card = h("div", { className: "ag-card" });
    card.appendChild(h("div", { className: "ag-card-title" }, "Compliance Score by Regulation"));
    card.appendChild(h("p", { className: "ag-card-subtitle" },
      "Scores based on controls mapped to each regulation."
    ));

    // Show regulations relevant to selected institution type first
    var activeRegs = this.state.scoping.regulations || [];
    var allRegs = Object.keys(this.data.regulatoryMappings);

    // Sort: active regs first (exact match), then alphabetical
    var sorted = allRegs.sort(function (a, b) {
      var aActive = activeRegs.indexOf(a) >= 0;
      var bActive = activeRegs.indexOf(b) >= 0;
      if (aActive && !bActive) return -1;
      if (!aActive && bActive) return 1;
      return a.localeCompare(b);
    });

    sorted.forEach(function (regKey) {
      var score = self.getRegulationScore(regKey);
      if (score === null) score = 0;
      var mapping = self.data.regulatoryMappings[regKey];
      card.appendChild(self.renderRagBar(
        regKey + " (" + mapping.controls.length + " controls)", score
      ));
      // Show contextual note if applicable
      if (REGULATION_NOTES[regKey]) {
        card.appendChild(h("div", {
          style: "font-size:0.75rem;color:var(--md-default-fg-color--light);margin:-0.3rem 0 0.5rem 130px;font-style:italic"
        }, REGULATION_NOTES[regKey]));
      }
    });

    panel.appendChild(card);
  };

  /* ---- Governance Levels tab ---- */
  AssessmentApp.prototype.renderZones = function (panel) {
    var self = this;
    var card = h("div", { className: "ag-card" });
    card.appendChild(h("div", { className: "ag-card-title" }, "Score by Governance Level"));
    card.appendChild(h("p", { className: "ag-card-subtitle" },
      "Selected target governance level: " + (this.getTargetLevel() === "baseline" ? "Baseline" : this.getTargetLevel() === "recommended" ? "Recommended" : "Regulated") +
      ". Scores are cumulative up to that target."
    ));

    var levelNames = { "baseline": "Baseline", "recommended": "Recommended", "regulated": "Regulated" };
    var levels = this.getIncludedLevels();
    levels.forEach(function (lvl) {
      var score = self.getLevelScore(lvl);
      card.appendChild(self.renderRagBar(levelNames[lvl], score !== null ? score : 0));
    });
    panel.appendChild(card);

    // Level chart
    var chartCard = h("div", { className: "ag-card", style: "margin-top:1rem" });
    chartCard.appendChild(h("div", { className: "ag-card-title" }, "Governance Level Comparison"));
    var canvas = h("canvas", { style: "max-height:300px" });
    chartCard.appendChild(canvas);
    panel.appendChild(chartCard);

    var self2 = this;
    setTimeout(function () { self2.renderZoneChart(canvas); }, 50);
  };

  AssessmentApp.prototype.renderZoneChart = function (canvas) {
    if (typeof Chart === "undefined") return;
    var self = this;
    var isDark = document.documentElement.getAttribute("data-md-color-scheme") === "slate";
    var textColor = isDark ? "#ccc" : "#666";

    var levelNames = { "baseline": "Baseline", "recommended": "Recommended", "regulated": "Regulated" };
    var levels = this.getIncludedLevels();
    var chart = new Chart(canvas, {
      type: "bar",
      data: {
        labels: levels.map(function (lvl) { return levelNames[lvl]; }),
        datasets: [{
          label: "Score %",
          data: levels.map(function (lvl) { return self.getLevelScore(lvl) || 0; }),
          backgroundColor: levels.map(function (lvl) {
            var s = self.getLevelScore(lvl) || 0;
            return s >= 80 ? "rgba(46,125,50,0.7)" : s >= 50 ? "rgba(230,81,0,0.7)" : "rgba(198,40,40,0.7)";
          }),
        }],
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
        plugins: { legend: { display: false } },
        scales: {
          y: { beginAtZero: true, max: 100, ticks: { color: textColor }, grid: { color: isDark ? "rgba(255,255,255,0.1)" : "rgba(0,0,0,0.06)" } },
          x: { ticks: { color: textColor }, grid: { display: false } },
        },
      },
    });
    this.charts.push(chart);
  };

  /* ---- Gaps tab ---- */
  AssessmentApp.prototype.renderGaps = function (panel) {
    var self = this;
    var gaps = this.getGapControls();

    var card = h("div", { className: "ag-card" });
    card.appendChild(h("div", { className: "ag-card-title" }, "Gap Analysis (" + gaps.length + " controls)"));
    card.appendChild(h("p", { className: "ag-card-subtitle" },
      "Controls sorted by risk priority (regulatory weight, governance level, and adoption phase)."
    ));

    if (gaps.length === 0) {
      card.appendChild(h("p", null, "No gaps detected."));
    } else {
      var wrap = h("div", { className: "ag-table-wrap" });
      var table = h("table", { className: "ag-table" });
      var thead = h("thead");
      var hrow = h("tr");
      ["Control", "Title", "Status", "Score", "Risk", "Regulations", "Playbooks"].forEach(function (col) {
        hrow.appendChild(h("th", null, col));
      });
      thead.appendChild(hrow);
      table.appendChild(thead);

      var tbody = h("tbody");
      var basePath = getBasePath();
      gaps.forEach(function (ctrl) {
        var score = self.getControlScore(ctrl.id);
        var resp = self.state.responses[ctrl.id] || {};
        var row = h("tr");
        row.appendChild(h("td", null, h("strong", null, ctrl.id)));
        row.appendChild(h("td", null, ctrl.title));
        row.appendChild(h("td", null, resp.answer || "—"));
        row.appendChild(h("td", null, score !== null ? Math.round(score * 100) + "%" : "—"));
        row.appendChild(h("td", null, self.getRiskPriority(ctrl).toFixed(1)));
        row.appendChild(h("td", null, ctrl.regulations.slice(0, 3).join(", ")));

        var links = h("td");
        var linkWrap = h("span", { className: "ag-roadmap-links" });
        linkWrap.appendChild(h("a", { href: basePath + ctrl.playbooks.portalWalkthrough }, "Portal"));
        linkWrap.appendChild(h("a", { href: basePath + ctrl.playbooks.powershellSetup }, "PS"));
        links.appendChild(linkWrap);
        row.appendChild(links);
        tbody.appendChild(row);
      });
      table.appendChild(tbody);
      wrap.appendChild(table);
      card.appendChild(wrap);
    }

    panel.appendChild(card);
  };

  /* ---- Response review tab ---- */
  AssessmentApp.prototype.renderResponseReview = function (panel) {
    var self = this;
    var card = h("div", { className: "ag-card" });
    card.appendChild(h("div", { className: "ag-card-title" }, "All Responses (" + this.data.controls.length + " controls)"));
    card.appendChild(h("p", { className: "ag-card-subtitle" },
      "Review every response. Click Edit to navigate back and change an answer."));

    var wrap = h("div", { className: "ag-table-wrap" });
    var table = h("table", { className: "ag-table" });
    var thead = h("thead");
    var hrow = h("tr");
    ["Control", "Title", "Response", "Score", "Notes", ""].forEach(function (col) {
      hrow.appendChild(h("th", null, col));
    });
    thead.appendChild(hrow);
    table.appendChild(thead);

    var tbody = h("tbody");
    this.data.controls.forEach(function (ctrl) {
      var resp = self.state.responses[ctrl.id] || {};
      var score = self.getControlScore(ctrl.id);
      var row = h("tr");
      row.appendChild(h("td", null, h("strong", null, ctrl.id)));
      row.appendChild(h("td", null, ctrl.title));
      row.appendChild(h("td", null, resp.answer || "\u2014"));
      row.appendChild(h("td", null, score !== null ? Math.round(score * 100) + "%" : "\u2014"));
      var notesTd = h("td", null);
      if (resp.notes) {
        notesTd.appendChild(h("span", { style: "font-size:0.78rem" },
          resp.notes.length > 60 ? resp.notes.substring(0, 60) + "\u2026" : resp.notes));
      }
      row.appendChild(notesTd);
      var editTd = h("td");
      editTd.appendChild(h("button", {
        className: "ag-edit-link",
        type: "button",
        "aria-label": "Edit response for " + ctrl.id,
        onClick: function () {
          self.goToStep("phase1");
          self.focusControlCard(ctrl.id);
        }
      }, "Edit"));
      row.appendChild(editTd);
      tbody.appendChild(row);
    });
    table.appendChild(tbody);
    wrap.appendChild(table);
    card.appendChild(wrap);
    panel.appendChild(card);
  };

  /* ---- Roadmap tab ---- */
  AssessmentApp.prototype.renderRoadmap = function (panel) {
    var self = this;
    var gaps = this.getGapControls();

    var card = h("div");
    card.appendChild(h("div", { className: "ag-card-title", style: "font-size:1.1rem;margin-bottom:0.5rem" },
      "Remediation Roadmap"));
    card.appendChild(h("p", { className: "ag-card-subtitle" },
      "Gaps grouped by responsible role, sequenced by adoption phase, sorted by risk priority."
    ));

    if (gaps.length === 0) {
      card.appendChild(h("div", { className: "ag-card" },
        h("p", null, "No gaps to remediate.")));
      panel.appendChild(card);
      return;
    }

    // Build role → phase → controls structure
    var rolePhaseMap = {};
    var basePath = getBasePath();

    gaps.forEach(function (ctrl) {
      var roles = ctrl.assignedRoles.length > 0 ? ctrl.assignedRoles : ["AI Governance Lead"];
      var phase = ctrl.adoptionPhase ? ctrl.adoptionPhase.phase : 2;

      roles.forEach(function (role) {
        if (!rolePhaseMap[role]) rolePhaseMap[role] = {};
        if (!rolePhaseMap[role][phase]) rolePhaseMap[role][phase] = [];
        rolePhaseMap[role][phase].push(ctrl);
      });
    });

    // Render by phase, then by role within each phase
    var phases = [0, 1, 2];
    phases.forEach(function (phaseNum) {
      var phaseData = self.data.adoptionPhases[String(phaseNum)];
      var hasGaps = false;
      Object.keys(rolePhaseMap).forEach(function (role) {
        if (rolePhaseMap[role][phaseNum] && rolePhaseMap[role][phaseNum].length > 0) hasGaps = true;
      });
      if (!hasGaps) return;

      var phaseSection = h("div", { className: "ag-roadmap-phase" });
      phaseSection.appendChild(h("div", { className: "ag-roadmap-phase-header" },
        "Phase " + phaseNum + ": " + (phaseData ? phaseData.name : "Other") +
        (phaseData ? " (" + phaseData.duration + ")" : "")));

      Object.keys(rolePhaseMap).sort().forEach(function (role) {
        var controls = rolePhaseMap[role][phaseNum];
        if (!controls || controls.length === 0) return;

        // Sort by risk priority within role
        controls.sort(function (a, b) {
          return self.getRiskPriority(b) - self.getRiskPriority(a);
        });

        var roleGroup = h("div", { className: "ag-roadmap-role-group" });
        roleGroup.appendChild(h("div", { className: "ag-roadmap-role-header" },
          role + " (" + controls.length + " item" + (controls.length > 1 ? "s" : "") + ")"));

        controls.forEach(function (ctrl) {
          var item = h("div", { className: "ag-roadmap-item" });

          var info = h("div", { style: "flex:1" });
          var titleLine = h("div");
          titleLine.appendChild(h("strong", null, ctrl.id + " "));
          titleLine.appendChild(document.createTextNode(ctrl.title));

          // Solution badge
          if (ctrl.solutions.length > 0) {
            titleLine.appendChild(document.createTextNode(" "));
            titleLine.appendChild(h("span", { className: "ag-badge ag-badge-solution" },
              "Automation: " + ctrl.solutions[0]));
          }
          info.appendChild(titleLine);

          // Links
          var links = h("div", { className: "ag-roadmap-links", style: "margin-top:0.2rem" });
          links.appendChild(h("a", { href: basePath + ctrl.playbooks.portalWalkthrough }, "Portal Walkthrough"));
          links.appendChild(h("a", { href: basePath + ctrl.playbooks.powershellSetup }, "PowerShell Setup"));
          links.appendChild(h("a", { href: basePath + ctrl.playbooks.verificationTesting }, "Verification"));
          links.appendChild(h("a", { href: basePath + ctrl.playbooks.troubleshooting }, "Troubleshooting"));
          info.appendChild(links);
          item.appendChild(info);

          roleGroup.appendChild(item);
        });

        phaseSection.appendChild(roleGroup);
      });

      card.appendChild(phaseSection);
    });

    // Effort estimates
    var effortCard = h("div", { className: "ag-card", style: "margin-top:1rem" });
    effortCard.appendChild(h("div", { className: "ag-card-title" }, "Estimated Effort by Phase"));
    var effortWrap = h("div", { className: "ag-table-wrap" });
    var effortTable = h("table", { className: "ag-table" });
    var eHead = h("tr");
    ["Phase", "Power Platform Admin", "Compliance", "Security", "AI Governance Lead"].forEach(function (col) {
      eHead.appendChild(h("th", null, col));
    });
    effortTable.appendChild(eHead);
    [0, 1, 2].forEach(function (p) {
      var est = self.data.effortEstimates[String(p)];
      if (!est) return;
      var row = h("tr");
      row.appendChild(h("td", null, h("strong", null, "Phase " + p)));
      row.appendChild(h("td", null, est["Power Platform Admin"] + " hrs"));
      row.appendChild(h("td", null, est["Compliance"] + " hrs"));
      row.appendChild(h("td", null, est["Security"] + " hrs"));
      row.appendChild(h("td", null, est["AI Governance Lead"] + " hrs"));
      effortTable.appendChild(row);
    });
    effortWrap.appendChild(effortTable);
    effortCard.appendChild(effortWrap);
    card.appendChild(effortCard);

    panel.appendChild(card);
  };

  /* ================================================================
     STEP 6: EXPORT
     ================================================================ */
  AssessmentApp.prototype.renderExport = function (parent) {
    var self = this;
    var wrap = h("div");
    wrap.appendChild(h("h2", { style: "font-size:1.3rem;margin-bottom:0.3rem", "data-step-heading": "true", tabindex: "-1" }, "Export Results"));
    wrap.appendChild(h("p", { className: "ag-card-subtitle" },
      "Download your assessment results in various formats."
    ));
    wrap.appendChild(h("div", { className: "ag-callout" },
      "Export a portal-ready governance envelope (.json) for upload to GRC, Purview, or Sentinel portals — " +
      "this bundles answers, collector evidence, solutions-lock version, and summary scores. " +
      "Use Load saved envelope to restore a prior export on another device. " +
      "Role-specific delegated sections are exported separately during Drill-Down."
    ));

    var grid = h("div", { className: "ag-export-grid" });

    // E: Portal envelope (primary answer-export).
    grid.appendChild(this.exportCard("ENV", "Export envelope (.json)",
      "Portal-ready envelope: answers, collector evidence, summary, and solutions-lock version",
      function () { self.exportEnvelope(); }));

    // Legacy full-state JSON (kept for trend-compare backwards compatibility).
    grid.appendChild(this.exportCard("JSON", "Full Assessment (legacy)",
      "Raw state snapshot used by the trend-compare tool below",
      function () { self.exportJSON(); }));

    // Excel export
    grid.appendChild(this.exportCard("XLSX", "Excel Workbook",
      "Multi-sheet workbook with scorecard, gaps, and roadmap",
      function () { self.exportExcel(); }));

    // CSV export
    grid.appendChild(this.exportCard("CSV", "Gap List",
      "Lightweight gap list for spreadsheet import",
      function () { self.exportCSV(); }));

    // PDF (print)
    grid.appendChild(this.exportCard("PDF", "Print to PDF",
      "Open print dialog for browser print-to-PDF",
      function () {
        self.goToStep("results");
        setTimeout(function () { window.print(); }, 300);
      }));

    wrap.appendChild(grid);

    // E: Load saved envelope — reverse path for envelope round-trip.
    wrap.appendChild(h("h3", { style: "font-size:1rem;margin-top:2rem" }, "Load saved envelope"));
    wrap.appendChild(h("p", { className: "ag-card-subtitle" },
      "Restore a previously-exported envelope JSON to resume assessor work or compare to a baseline."
    ));
    var loadBtn = h("button", {
      className: "ag-btn ag-btn-secondary",
      type: "button",
      id: "envelope-import-btn",
      onClick: function () { self.importEnvelopeFromFile(); },
    }, "Load saved envelope");
    wrap.appendChild(loadBtn);

    // Trend comparison
    wrap.appendChild(h("h3", { style: "font-size:1rem;margin-top:2rem" }, "Trend Comparison"));
    wrap.appendChild(h("p", { className: "ag-card-subtitle" },
      "Upload a previous full assessment JSON export to compare score trends side-by-side."
    ));
    var compareBtn = h("button", {
      className: "ag-btn ag-btn-secondary",
      type: "button",
      onClick: function () { self.triggerTrendCompare(); }
    }, "Upload Previous Assessment");
    wrap.appendChild(compareBtn);

    var compareResult = h("div", { id: "ag-trend-result", "aria-live": "polite", "aria-atomic": "true" });
    wrap.appendChild(compareResult);

    // Navigation
    var btns = h("div", { className: "ag-btn-group" });
    btns.appendChild(h("button", {
      className: "ag-btn ag-btn-secondary",
      type: "button",
      onClick: function () { self.goToStep("results"); }
    }, "Back to Results"));
    wrap.appendChild(btns);

    parent.appendChild(wrap);
  };

  AssessmentApp.prototype.exportCard = function (icon, title, desc, onClick) {
    var card = h("button", {
      className: "ag-export-card",
      type: "button",
      "aria-label": "Export as " + title,
      onClick: onClick,
    });
    card.appendChild(h("div", { className: "ag-export-icon" }, icon));
    card.appendChild(h("div", { className: "ag-export-label" }, title));
    card.appendChild(h("div", { className: "ag-export-desc" }, desc));
    return card;
  };

  /* ---- JSON export ---- */
  AssessmentApp.prototype.exportJSON = function () {
    this.saveToStorage();
    var blob = new Blob([JSON.stringify(this.state, null, 2)], { type: "application/json" });
    var name = (this.state.assessmentName || "assessment").replace(/[^a-zA-Z0-9-_]/g, "-");
    downloadBlob(blob, name + ".json");
    this.setMessage(
      "success",
      "Assessment exported",
      "Downloaded the full assessment JSON file. Use this file to re-import the assessment later or compare trends."
    );
  };

  /* ---- CSV export ---- */
  AssessmentApp.prototype.exportCSV = function () {
    var self = this;
    var csvField = function (val) {
      val = sanitizeCell(String(val));
      // Escape newlines and quotes for CSV
      if (/[",\n\r]/.test(val)) {
        return '"' + val.replace(/"/g, '""').replace(/[\r\n]+/g, " ") + '"';
      }
      return val;
    };
    var rows = [["Control ID", "Title", "Pillar", "Status", "Score", "Risk Priority", "Regulations", "Notes"]];
    this.getGapControls().forEach(function (ctrl) {
      var resp = self.state.responses[ctrl.id] || {};
      var score = self.getControlScore(ctrl.id);
      rows.push([
        csvField(ctrl.id),
        csvField(ctrl.title),
        csvField(ctrl.pillarName),
        csvField(resp.answer || ""),
        csvField(score !== null ? Math.round(score * 100) + "%" : ""),
        csvField(self.getRiskPriority(ctrl).toFixed(1)),
        csvField(ctrl.regulations.join(", ")),
        csvField(resp.notes || ""),
      ]);
    });
    var csv = rows.map(function (r) { return r.join(","); }).join("\n");
    var blob = new Blob([csv], { type: "text/csv" });
    var name = (this.state.assessmentName || "assessment").replace(/[^a-zA-Z0-9-_]/g, "-");
    downloadBlob(blob, name + "-gaps.csv");
    this.setMessage(
      "success",
      "Gap list exported",
      "Downloaded the current gap list as CSV for spreadsheet review."
    );
  };

  /* ---- Excel export ---- */
  AssessmentApp.prototype.exportExcel = function () {
    var self = this;

    // Lazy-load SheetJS
    var base = "";
    var scripts = document.querySelectorAll('script[src*="assessment-loader"]');
    if (scripts.length) {
      var src = scripts[scripts.length - 1].src;
      base = src.substring(0, src.lastIndexOf("/") + 1);
    }

    var doExport = function () {
      if (typeof XLSX === "undefined") {
        self.setMessage(
          "error",
          "Excel export unavailable",
          "The Excel export library is not available. Use the CSV export instead."
        );
        return;
      }
      var wb = XLSX.utils.book_new();

      // Sheet 1: Summary
      var summaryData = [
        ["FSI Copilot Governance — Governance Scorecard Report"],
        [],
        ["Assessment Name", sanitizeCell(self.state.assessmentName || "")],
        ["Organization", sanitizeCell(self.state.scoping.organizationName || "")],
        ["Assessor", sanitizeCell(self.state.scoping.assessorName || "")],
        ["Institution Type", sanitizeCell(self.state.scoping.institutionType || "")],
        ["Target Governance Level", sanitizeCell(self.getTargetLevel())],
        ["Date", fmtDate(self.state.updatedAt)],
        ["Data Version", sanitizeCell(self.state.dataVersion || "")],
        ["Framework Version", sanitizeCell(self.state.frameworkVersion || "")],
        [],
        ["Overall Score", (self.getOverallScore() || 0) + "%"],
        ["Controls Assessed", self.getAnsweredControlCount() + " / " + self.data.totalControls],
        ["Gaps Identified", self.getGapControls().length],
        [],
        ["Pillar", "Score"],
      ];
      [1, 2, 3, 4].forEach(function (p) {
        summaryData.push([
          "Pillar " + p + " — " + self.data.pillars[String(p)].name,
          (self.getPillarScore(p) || 0) + "%",
        ]);
      });
      var ws1 = XLSX.utils.aoa_to_sheet(summaryData);
      XLSX.utils.book_append_sheet(wb, ws1, "Summary");

      // Sheet 2: All Controls
      var ctrlData = [["Control ID", "Title", "Pillar", "Status", "Score", "Notes", "Phase", "Priority"]];
      self.data.controls.forEach(function (ctrl) {
        var resp = self.state.responses[ctrl.id] || {};
        var score = self.getControlScore(ctrl.id);
        ctrlData.push([
          ctrl.id, ctrl.title, ctrl.pillarName,
          resp.answer || "Not assessed",
          score !== null ? Math.round(score * 100) + "%" : "N/A",
          sanitizeCell(resp.notes || ""),
          ctrl.adoptionPhase ? "Phase " + ctrl.adoptionPhase.phase : "",
          ctrl.adoptionPhase ? ctrl.adoptionPhase.priority : "",
        ]);
      });
      var ws2 = XLSX.utils.aoa_to_sheet(ctrlData);
      XLSX.utils.book_append_sheet(wb, ws2, "Control Details");

      // Sheet 3: Gap Analysis
      var gapData = [["Control ID", "Title", "Pillar", "Status", "Score", "Risk Priority", "Regulations", "Solutions", "Notes"]];
      self.getGapControls().forEach(function (ctrl) {
        var resp = self.state.responses[ctrl.id] || {};
        var score = self.getControlScore(ctrl.id);
        gapData.push([
          ctrl.id, ctrl.title, ctrl.pillarName,
          resp.answer || "",
          score !== null ? Math.round(score * 100) + "%" : "",
          self.getRiskPriority(ctrl).toFixed(1),
          ctrl.regulations.join(", "),
          ctrl.solutions.join(", "),
          sanitizeCell(resp.notes || ""),
        ]);
      });
      var ws3 = XLSX.utils.aoa_to_sheet(gapData);
      XLSX.utils.book_append_sheet(wb, ws3, "Gap Analysis");

      // Sheet 4: Regulatory Matrix
      var regData = [["Regulation", "Controls Mapped", "Score"]];
      Object.keys(self.data.regulatoryMappings).forEach(function (regKey) {
        var mapping = self.data.regulatoryMappings[regKey];
        var score = self.getRegulationScore(regKey);
        regData.push([
          regKey,
          mapping.controls.length,
          score !== null ? score + "%" : "N/A",
        ]);
      });
      var ws4 = XLSX.utils.aoa_to_sheet(regData);
      XLSX.utils.book_append_sheet(wb, ws4, "Regulatory Matrix");

      // Sheet 5: Remediation Plan by Role
      var remData = [["Phase", "Role", "Control ID", "Title", "Risk Priority", "Solution Available"]];
      var gaps = self.getGapControls();
      gaps.forEach(function (ctrl) {
        var roles = ctrl.assignedRoles.length > 0 ? ctrl.assignedRoles : ["AI Governance Lead"];
        var phase = ctrl.adoptionPhase ? ctrl.adoptionPhase.phase : 2;
        roles.forEach(function (role) {
          remData.push([
            "Phase " + phase, role, ctrl.id, ctrl.title,
            self.getRiskPriority(ctrl).toFixed(1),
            ctrl.solutions.length > 0 ? ctrl.solutions.join(", ") : "No",
          ]);
        });
      });
      var ws5 = XLSX.utils.aoa_to_sheet(remData);
      XLSX.utils.book_append_sheet(wb, ws5, "Remediation Plan");

      // Generate and download
      var buf = XLSX.write(wb, { bookType: "xlsx", type: "array" });
      var blob = new Blob([buf], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
      var name = (self.state.assessmentName || "assessment").replace(/[^a-zA-Z0-9-_]/g, "-");
      downloadBlob(blob, name + ".xlsx");
      self.setMessage(
        "success",
        "Excel workbook exported",
        "Downloaded the multi-sheet Excel workbook for the current assessment."
      );
    };

    if (typeof XLSX !== "undefined") {
      doExport();
    } else {
      // Check if script is already loading
      var xlsxSrc = base + "lib/xlsx.full.min.js";
      var existing = document.querySelector('script[src="' + xlsxSrc + '"]');
      if (existing) {
        existing.addEventListener("load", doExport);
        return;
      }
      // Lazy load SheetJS with SRI
      var s = document.createElement("script");
      s.src = xlsxSrc;
      s.integrity = "sha256-yVBhl8r4CaB1tt7h2g02+xnacVj/6KiOewyWxdhiPJk=";
      s.crossOrigin = "anonymous";
      s.onload = doExport;
      s.onerror = function () {
        self.setMessage(
          "error",
          "Excel export unavailable",
          "The Excel export library could not be loaded. Try the CSV export instead."
        );
      };
      document.head.appendChild(s);
    }
  };

  /* ---- Trend comparison ---- */
  AssessmentApp.prototype.triggerTrendCompare = function () {
    var self = this;
    var input = document.createElement("input");
    input.type = "file";
    input.accept = ".json";
    input.onchange = function () {
      var file = input.files[0];
      if (!file) return;
      var reader = new FileReader();
      reader.onload = function () {
        try {
          var prev = JSON.parse(reader.result);
          self.showTrendComparison(prev);
        } catch (e) {
          var container = document.getElementById("ag-trend-result");
          if (container) {
            container.innerHTML = "";
            container.appendChild(h("div", { className: "ag-disclaimer" },
              "The selected file is not valid JSON. Upload a full assessment JSON export to compare trends."
            ));
          }
          self.setMessage("error", "Trend comparison failed", "The selected file is not valid JSON. " + e.message);
        }
      };
      reader.readAsText(file);
    };
    input.click();
  };

  AssessmentApp.prototype.showTrendComparison = function (prevState) {
    var container = document.getElementById("ag-trend-result");
    if (!container) return;
    container.innerHTML = "";

    // Validate uploaded file is a valid assessment
    if (!this.validateState(prevState)) {
      this.setMessage(
        "error",
        "Trend comparison failed",
        "Upload a full assessment JSON export created from this scorecard."
      );
      container.appendChild(h("div", { className: "ag-disclaimer" },
        "The uploaded file does not appear to be a valid assessment export."));
      return;
    }

    if (prevState.schemaVersion && prevState.schemaVersion > STATE_SCHEMA_VERSION) {
      this.setMessage(
        "error",
        "Trend comparison blocked",
        "The uploaded assessment file was created by a newer scorecard version."
      );
      container.appendChild(h("div", { className: "ag-disclaimer" },
        "The uploaded file was created by a newer scorecard version and cannot be compared here."));
      return;
    }

    var self = this;
    var previous = this.buildCleanState(prevState);
    var currentTarget = this.getTargetLevel();
    var previousTarget = this.getTargetLevel(previous);
    var card = h("div", { className: "ag-card" });
    card.appendChild(h("div", { className: "ag-card-title" }, "Trend Comparison"));
    card.appendChild(h("p", { className: "ag-card-subtitle" },
      "Current assessment vs. " + fmtDate(previous.updatedAt)));
    if (previousTarget !== currentTarget) {
      card.appendChild(h("div", { className: "ag-disclaimer" },
        "The uploaded assessment used the " +
        (previousTarget === "baseline" ? "Baseline" : previousTarget === "recommended" ? "Recommended" : "Regulated") +
        " target governance level, while the current assessment uses " +
        (currentTarget === "baseline" ? "Baseline" : currentTarget === "recommended" ? "Recommended" : "Regulated") +
        ". Compare the results with that scope difference in mind."
      ));
    }

    var wrap = h("div", { className: "ag-table-wrap" });
    var table = h("table", { className: "ag-table" });
    var head = h("tr");
    ["Metric", "Previous", "Current", "Change"].forEach(function (col) {
      head.appendChild(h("th", null, col));
    });
    table.appendChild(head);

    // Calculate previous scores
    var prevOverall = this.getOverallScore(undefined, previous) || 0;
    var currOverall = self.getOverallScore() || 0;

    var addRow = function (label, prev, curr) {
      var row = h("tr");
      row.appendChild(h("td", null, label));
      row.appendChild(h("td", null, prev + "%"));
      row.appendChild(h("td", null, curr + "%"));
      var delta = curr - prev;
      var deltaStr = (delta >= 0 ? "+" : "") + delta + "%";
      row.appendChild(h("td", { style: "color:" + (delta > 0 ? "var(--ag-green)" : delta < 0 ? "var(--ag-red)" : "inherit") }, deltaStr));
      return row;
    };

    table.appendChild(addRow("Overall", prevOverall, currOverall));
    [1, 2, 3, 4].forEach(function (pillarNum) {
      table.appendChild(addRow(
        "Pillar " + pillarNum,
        self.getPillarScore(pillarNum, undefined, previous) || 0,
        self.getPillarScore(pillarNum) || 0
      ));
    });
    wrap.appendChild(table);
    card.appendChild(wrap);
    container.appendChild(card);
    this.setMessage(
      "success",
      "Trend comparison loaded",
      "Compared the current assessment with the uploaded assessment export."
    );
  };

  /* ================================================================
     D2: COLLECTOR EVIDENCE — apply, clear, persist
     ================================================================ */
  AssessmentApp.prototype.applyCollectorEvidence = function (map, runId) {
    if (!this.state) return;
    this.state.collectorEvidence = this.state.collectorEvidence || {};
    this.state.collectorPriorAnswers = this.state.collectorPriorAnswers || {};
    if (runId) this.state.collectorRunId = runId;
    var importedAt = new Date().toISOString();
    var self = this;
    var prefillCount = 0;
    var evidenceCount = 0;
    Object.keys(map || {}).forEach(function (ctrlId) {
      var entry = map[ctrlId];
      if (!entry) return;
      self.state.collectorEvidence[ctrlId] = {
        status: entry.status || null,
        evidence: Array.isArray(entry.evidence) ? entry.evidence : [],
        runId: runId || self.state.collectorRunId || "",
        importedAt: importedAt,
      };
      evidenceCount += self.state.collectorEvidence[ctrlId].evidence.length;
      if (entry.status) {
        var resp = self.state.responses[ctrlId] || {};
        if (!Object.prototype.hasOwnProperty.call(self.state.collectorPriorAnswers, ctrlId)) {
          self.state.collectorPriorAnswers[ctrlId] = resp.answer || null;
        }
        resp.answer = entry.status;
        self.state.responses[ctrlId] = resp;
        prefillCount++;
      }
    });
    try {
      if (runId) {
        localStorage.setItem(COLLECTOR_EVIDENCE_KEY_PREFIX + runId, JSON.stringify({
          runId: runId,
          importedAt: importedAt,
          evidence: this.state.collectorEvidence,
          priorAnswers: this.state.collectorPriorAnswers,
        }));
      }
    } catch (_e) { /* quota / private mode */ }
    this.saveToStorage();
    return { prefillCount: prefillCount, evidenceCount: evidenceCount };
  };

  AssessmentApp.prototype.clearCollectorEvidence = function () {
    if (!this.state) return;
    var prior = this.state.collectorPriorAnswers || {};
    var self = this;
    Object.keys(prior).forEach(function (id) {
      var prev = prior[id];
      var resp = self.state.responses[id];
      if (!resp) return;
      if (prev) {
        resp.answer = prev;
      } else {
        delete resp.answer;
      }
      if (!resp.answer && !resp.notes) {
        delete self.state.responses[id];
      }
    });
    var runId = this.state.collectorRunId;
    if (runId) {
      try { localStorage.removeItem(COLLECTOR_EVIDENCE_KEY_PREFIX + runId); } catch (_e) { /* */ }
    }
    delete this.state.collectorEvidence;
    delete this.state.collectorPriorAnswers;
    delete this.state.collectorRunId;
    this.saveToStorage();
  };

  AssessmentApp.prototype.hasCollectorEvidence = function () {
    return !!(this.state && this.state.collectorEvidence && Object.keys(this.state.collectorEvidence).length);
  };

  AssessmentApp.prototype.getCollectorEvidenceFor = function (ctrlId) {
    if (!this.state || !this.state.collectorEvidence) return null;
    return this.state.collectorEvidence[ctrlId] || null;
  };

  /** Wire up the import UI: file input + drag-drop zone. Returns the root element. */
  AssessmentApp.prototype.renderCollectorImportControls = function () {
    var self = this;
    var wrap = h("div", { className: "collector-import-controls" });

    var fileInput = h("input", {
      type: "file",
      id: "collector-import-input",
      accept: ".csv,.json,text/csv,application/json",
      style: "display:none",
      "aria-hidden": "true",
    });
    wrap.appendChild(fileInput);

    var hasEvidence = self.hasCollectorEvidence();
    var importBtn = h("button", {
      className: "ag-btn ag-btn-sm ag-btn-secondary collector-import-btn",
      type: "button",
      id: "collector-import-btn",
      "aria-label": "Import collector evidence CSV or JSON",
      onClick: function () { fileInput.click(); },
    }, "📥 Import evidence");
    wrap.appendChild(importBtn);

    if (hasEvidence) {
      var summary = this.state.collectorRunId ? (" (" + this.state.collectorRunId + ")") : "";
      wrap.appendChild(h("span", { className: "collector-import-status" },
        "Collector evidence loaded" + summary));
      wrap.appendChild(h("button", {
        className: "ag-btn ag-btn-sm ag-btn-secondary collector-clear-btn",
        type: "button",
        id: "collector-clear-btn",
        onClick: function () { self._confirmClearCollectorEvidence(); },
      }, "Clear collector evidence"));
    }

    fileInput.addEventListener("change", function (e) {
      var files = e.target && e.target.files;
      if (!files || !files.length) return;
      self._handleCollectorFile(files[0]);
      // Reset so re-selecting the same file still triggers change.
      fileInput.value = "";
    });

    // Drop-zone: entire wrap accepts drag-drop for convenience.
    wrap.addEventListener("dragover", function (e) {
      e.preventDefault();
      wrap.classList.add("drag-over");
    });
    wrap.addEventListener("dragleave", function () { wrap.classList.remove("drag-over"); });
    wrap.addEventListener("drop", function (e) {
      e.preventDefault();
      wrap.classList.remove("drag-over");
      var files = e.dataTransfer && e.dataTransfer.files;
      if (!files || !files.length) return;
      self._handleCollectorFile(files[0]);
    });

    return wrap;
  };

  AssessmentApp.prototype._confirmClearCollectorEvidence = function () {
    if (typeof window !== "undefined" && typeof window.confirm === "function") {
      if (!window.confirm("Clear all collector evidence and revert any auto-prefilled answers? Your manual answers will be preserved.")) {
        return;
      }
    }
    this.clearCollectorEvidence();
    this.setMessage(
      "success",
      "Collector evidence cleared",
      "Auto-prefilled answers have been reverted. Your manual answers were preserved."
    );
    this.render();
  };

  AssessmentApp.prototype._handleCollectorFile = function (file) {
    if (!file) return;
    var self = this;
    var name = file.name || "collector-import";
    var reader = new FileReader();
    reader.onload = function (ev) {
      var text = ev.target && ev.target.result ? String(ev.target.result) : "";
      var map;
      var looksJson = /\.json$/i.test(name) || /^\s*[{\[]/.test(text);
      try {
        map = looksJson ? parseCollectorJson(text) : parseCollectorCsv(text);
      } catch (err) {
        self.setMessage("error", "Could not parse collector file",
          "The file could not be parsed. Confirm it is a collector CSV or JSON export.");
        return;
      }
      var rowCount = Object.keys(map || {}).length;
      if (!rowCount) {
        self.setMessage("warning", "No evidence rows found",
          "The file parsed, but contained no usable rows. Confirm the CSV has a control_id column.");
        return;
      }
      var result = self.applyCollectorEvidence(map, name) || { prefillCount: 0, evidenceCount: 0 };
      self.setMessage("success", "Collector evidence imported",
        "Loaded " + rowCount + " control" + (rowCount === 1 ? "" : "s") +
        " — " + result.prefillCount + " answer" + (result.prefillCount === 1 ? "" : "s") +
        " auto-prefilled from " + result.evidenceCount + " evidence row" + (result.evidenceCount === 1 ? "" : "s") + ".");
      self.render();
    };
    reader.onerror = function () {
      self.setMessage("error", "File read error",
        "Could not read " + name + ". Try again or use a different file.");
    };
    reader.readAsText(file);
  };

  /* ================================================================
     C3: SOLUTIONS CATALOG VIEW
     Top-level view listing every solution from solutions-lock.json
     (count is derived from the loaded manifest at runtime, not hard-coded),
     with filters (tier/domain/search), reverse-lookup from manifest
     showing which controls reference each solution, and a click-to-
     detail panel.
     ================================================================ */

  /** Return all manifest rows that reference `solId` (string) in their .solutions array. */
  AssessmentApp.prototype.getControlsForSolution = function (solId) {
    if (!this.manifest || !Array.isArray(this.manifest)) return [];
    return this.manifest.filter(function (m) {
      if (!m || !Array.isArray(m.solutions)) return false;
      return m.solutions.some(function (s) {
        if (typeof s === "string") return s === solId;
        return s && s.id === solId;
      });
    });
  };

  AssessmentApp.prototype._getSolutionsFilter = function () {
    return this._solutionsFilter || (this._solutionsFilter = {
      tier: "all",    // "all" | 1 | 2 | 3
      domain: "all",  // "all" | domain string
      search: "",
      selectedId: null,
    });
  };

  AssessmentApp.prototype.renderSolutionsView = function (parent) {
    var self = this;
    var wrap = h("div", { className: "solutions-view" });
    wrap.appendChild(h("h2", {
      style: "font-size:1.3rem;margin-bottom:0.3rem",
      "data-step-heading": "true",
      tabindex: "-1",
    }, "🧩 Solutions Catalog"));

    var lock = this.solutionsLock;
    var solutions = (lock && Array.isArray(lock.solutions)) ? lock.solutions : [];
    if (!solutions.length) {
      wrap.appendChild(h("p", { className: "solution-empty" },
        "Solutions catalog not yet loaded. Run mkdocs build to refresh assessment data."));
      parent.appendChild(wrap);
      return;
    }

    wrap.appendChild(h("p", { className: "ag-card-subtitle" },
      "Catalog of " + solutions.length + " solutions from the FSI-CopilotGov-Solutions sister repo" +
      (lock && lock.source && lock.source.ref ? " (" + lock.source.ref + ")" : "") +
      ". Click a card to see which controls it covers."));

    // ----- filter bar -----
    var filter = this._getSolutionsFilter();
    var filterBar = h("div", { className: "solutions-filter-bar" });
    // Tier chips
    var tierGroup = h("div", { className: "solutions-filter-group", role: "group", "aria-label": "Filter by tier" });
    tierGroup.appendChild(h("span", { className: "solutions-filter-label" }, "Tier:"));
    [["all", "All"], [1, "Tier 1"], [2, "Tier 2"], [3, "Tier 3"]].forEach(function (pair) {
      var val = pair[0];
      var active = filter.tier === val;
      tierGroup.appendChild(h("button", {
        className: "solutions-filter-chip" + (active ? " active" : ""),
        type: "button",
        "aria-pressed": active ? "true" : "false",
        "data-filter-tier": String(val),
        onClick: function () {
          filter.tier = val;
          filter.selectedId = null;
          self.render();
        },
      }, pair[1]));
    });
    filterBar.appendChild(tierGroup);

    // Domain chips — built from unique domain values in the catalog.
    var domains = {};
    solutions.forEach(function (s) { if (s && s.domain) domains[s.domain] = true; });
    var domainList = Object.keys(domains).sort();
    if (domainList.length) {
      var domGroup = h("div", { className: "solutions-filter-group", role: "group", "aria-label": "Filter by domain" });
      domGroup.appendChild(h("span", { className: "solutions-filter-label" }, "Domain:"));
      [["all", "All"]].concat(domainList.map(function (d) { return [d, d]; })).forEach(function (pair) {
        var val = pair[0];
        var active = filter.domain === val;
        domGroup.appendChild(h("button", {
          className: "solutions-filter-chip" + (active ? " active" : ""),
          type: "button",
          "aria-pressed": active ? "true" : "false",
          "data-filter-domain": String(val),
          onClick: function () {
            filter.domain = val;
            filter.selectedId = null;
            self.render();
          },
        }, pair[1]));
      });
      filterBar.appendChild(domGroup);
    }

    // Search
    var searchWrap = h("div", { className: "solutions-filter-group solutions-filter-search" });
    searchWrap.appendChild(h("label", { htmlFor: "solutions-search-input", className: "solutions-filter-label" }, "Search:"));
    var searchInput = h("input", {
      type: "search",
      id: "solutions-search-input",
      className: "ag-input",
      placeholder: "name, summary, or slug",
      value: filter.search,
    });
    var runSearch = debounce(function () {
      filter.search = searchInput.value;
      filter.selectedId = null;
      self.render();
    }, 250);
    searchInput.addEventListener("input", runSearch);
    searchWrap.appendChild(searchInput);
    filterBar.appendChild(searchWrap);

    wrap.appendChild(filterBar);

    // ----- apply filter -----
    var needle = (filter.search || "").toLowerCase();
    var filtered = solutions.filter(function (s) {
      if (!s) return false;
      if (filter.tier !== "all" && s.tier !== filter.tier) return false;
      if (filter.domain !== "all" && s.domain !== filter.domain) return false;
      if (needle) {
        var hay = [s.id, s.name, s.summary, s.domain].filter(Boolean).join(" ").toLowerCase();
        if (hay.indexOf(needle) < 0) return false;
      }
      return true;
    });

    wrap.appendChild(h("p", { className: "solutions-count", "aria-live": "polite" },
      "Showing " + filtered.length + " of " + solutions.length + " solutions"));

    // ----- grid of cards -----
    var grid = h("div", { className: "solutions-catalog-grid" });
    filtered.forEach(function (s) {
      grid.appendChild(self._renderSolutionCatalogCard(s, filter.selectedId === s.id));
    });
    wrap.appendChild(grid);

    // ----- detail panel -----
    if (filter.selectedId) {
      var selected = solutions.filter(function (x) { return x && x.id === filter.selectedId; })[0];
      if (selected) {
        wrap.appendChild(this._renderSolutionDetailPanel(selected));
      }
    }

    var btns = h("div", { className: "ag-btn-group", style: "margin-top:1.5rem" });
    btns.appendChild(h("button", {
      className: "ag-btn ag-btn-secondary",
      type: "button",
      onClick: function () {
        // Return to phase1 if accessible, otherwise welcome.
        self.goToStep(self.canAccessStep("phase1") ? "phase1" : "welcome");
      },
    }, "Back to assessment"));
    wrap.appendChild(btns);

    parent.appendChild(wrap);
  };

  AssessmentApp.prototype._renderSolutionCatalogCard = function (s, selected) {
    var self = this;
    var coverage = this.getControlsForSolution(s.id).length;
    var card = h("button", {
      className: "solution-catalog-card" + (selected ? " selected" : ""),
      type: "button",
      "data-solution-id": s.id,
      "aria-pressed": selected ? "true" : "false",
      onClick: function () {
        var filter = self._getSolutionsFilter();
        filter.selectedId = (filter.selectedId === s.id) ? null : s.id;
        self.render();
      },
    });
    card.appendChild(h("div", { className: "solution-catalog-name" }, s.name || s.id));
    var meta = h("div", { className: "solution-catalog-meta" });
    if (s.tier) meta.appendChild(h("span", { className: "solution-catalog-tier tier-" + s.tier }, "Tier " + s.tier));
    if (s.domain) meta.appendChild(h("span", { className: "solution-catalog-domain" }, s.domain));
    if (s.version) meta.appendChild(h("span", { className: "solution-catalog-version" }, "v" + s.version));
    card.appendChild(meta);
    if (s.summary) {
      card.appendChild(h("p", { className: "solution-catalog-summary" }, s.summary));
    }
    card.appendChild(h("span", {
      className: "solution-catalog-coverage",
      "data-coverage-count": String(coverage),
    }, "Covers " + coverage + " of 62 control" + (coverage === 1 ? "" : "s")));
    return card;
  };

  AssessmentApp.prototype._renderSolutionDetailPanel = function (s) {
    var self = this;
    var panel = h("aside", { className: "solution-detail-panel", role: "region",
      "aria-label": "Solution detail: " + (s.name || s.id) });
    var header = h("div", { className: "solution-detail-header" });
    header.appendChild(h("h3", { className: "solution-detail-title" }, s.name || s.id));
    if (s.tier) header.appendChild(h("span", { className: "solution-catalog-tier tier-" + s.tier }, "Tier " + s.tier));
    if (s.domain) header.appendChild(h("span", { className: "solution-catalog-domain" }, s.domain));
    if (s.version) header.appendChild(h("span", { className: "solution-catalog-version" }, "v" + s.version));
    panel.appendChild(header);

    if (s.summary) panel.appendChild(h("p", { className: "solution-detail-summary" }, s.summary));

    if (s.url) {
      panel.appendChild(h("a", {
        className: "solution-detail-link",
        href: s.url, target: "_blank", rel: "noopener noreferrer",
      }, "Open solution repo ↗"));
    }

    var controls = this.getControlsForSolution(s.id);
    var ctrlSec = h("div", { className: "solution-detail-controls" });
    ctrlSec.appendChild(h("h4", null,
      "Controls covered (" + controls.length + " of 62)"));
    if (!controls.length) {
      ctrlSec.appendChild(h("p", { className: "solution-empty" },
        "This solution is not yet mapped to any manifest controls."));
    } else {
      var list = h("ul", { className: "solution-detail-control-list" });
      controls.forEach(function (m) {
        var li = h("li", { className: "solution-detail-control-item" });
        var link = h("a", {
          href: "#",
          className: "solution-detail-control-link",
          "data-control-id": m.id,
          onClick: function (e) {
            e.preventDefault();
            self.jumpToControl(m.id);
          },
        }, m.id + " — " + (m.title || m.name || ""));
        li.appendChild(link);
        // Show pillar + tier/role for this mapping if available.
        var meta = h("span", { className: "solution-detail-control-meta" });
        meta.appendChild(h("span", { className: "solution-detail-control-pillar" }, "P" + m.pillar));
        var mapping = (m.solutions || []).filter(function (x) {
          return (typeof x === "string" ? x : x && x.id) === s.id;
        })[0];
        if (mapping && typeof mapping === "object") {
          if (mapping.role) meta.appendChild(h("span", { className: "solution-detail-control-role role-" + mapping.role }, mapping.role));
          if (mapping.tier) meta.appendChild(h("span", { className: "solution-detail-control-tier tier-" + mapping.tier }, "T" + mapping.tier));
        }
        li.appendChild(meta);
        list.appendChild(li);
      });
      ctrlSec.appendChild(list);
    }
    panel.appendChild(ctrlSec);
    return panel;
  };

  /** Jump to phase1 and scroll/focus on a specific control card. */
  AssessmentApp.prototype.jumpToControl = function (controlId) {
    if (!controlId) return;
    if (!this.canAccessStep("phase1")) {
      this.setMessage("warning", "Complete scoping first",
        "Finish the scoping step before jumping into controls.");
      return;
    }
    this.step = "phase1";
    this.render();
    var self = this;
    setTimeout(function () {
      var row = self.el.querySelector('.control-row[data-control-id="' + controlId + '"]');
      if (row) {
        row.scrollIntoView({ behavior: "smooth", block: "center" });
        row.classList.add("jump-highlight");
        setTimeout(function () { row.classList.remove("jump-highlight"); }, 1500);
      }
    }, 50);
  };

  /* ================================================================
     E: PORTAL EXPORT ENVELOPE
     Builds a portal-upload-ready JSON envelope and supports round-trip
     re-import for assessor continuity across sessions/devices.
     ================================================================ */
  AssessmentApp.prototype.getEnvelopeIdentity = function () {
    try {
      var raw = localStorage.getItem(ENVELOPE_IDENTITY_KEY);
      if (!raw) return { name: "", role: "", org: "" };
      var parsed = JSON.parse(raw);
      return {
        name: String((parsed && parsed.name) || ""),
        role: String((parsed && parsed.role) || ""),
        org: String((parsed && parsed.org) || ""),
      };
    } catch (_e) {
      return { name: "", role: "", org: "" };
    }
  };

  AssessmentApp.prototype.setEnvelopeIdentity = function (identity) {
    try {
      localStorage.setItem(ENVELOPE_IDENTITY_KEY, JSON.stringify({
        name: String((identity && identity.name) || ""),
        role: String((identity && identity.role) || ""),
        org: String((identity && identity.org) || ""),
      }));
    } catch (_e) { /* */ }
  };

  /**
   * Compose the envelope object for the current state. Pure — no DOM side
   * effects — so it can be unit-tested without booting the whole SPA.
   */
  AssessmentApp.prototype.buildEnvelope = function () {
    var self = this;
    var state = this.state || {};
    var scoping = state.scoping || {};
    var identity = this.getEnvelopeIdentity();
    if (!identity.name && scoping.assessorName) identity.name = scoping.assessorName;
    if (!identity.role && scoping.assessorRole) identity.role = scoping.assessorRole;
    if (!identity.org && scoping.organizationName) identity.org = scoping.organizationName;

    var tier = this.getTargetLevel ? this.getTargetLevel() : (scoping.targetLevel || "recommended");
    var pillars = [1, 2, 3, 4];

    var answers = [];
    var summary = { yes: 0, partial: 0, no: 0, na: 0, unanswered: 0 };
    var controlsList = (this.data && this.data.controls) ? this.data.controls : [];
    controlsList.forEach(function (ctrl) {
      var resp = (state.responses && state.responses[ctrl.id]) || {};
      var ce = self.getCollectorEvidenceFor ? self.getCollectorEvidenceFor(ctrl.id) : null;
      if (!resp.answer) summary.unanswered++;
      else if (resp.answer === "yes") summary.yes++;
      else if (resp.answer === "partial") summary.partial++;
      else if (resp.answer === "no") summary.no++;
      else if (resp.answer === "na") summary.na++;
      answers.push({
        controlId: ctrl.id,
        pillar: ctrl.pillar,
        answer: resp.answer || null,
        notes: resp.notes || "",
        collectorEvidence: ce ? {
          status: ce.status || null,
          runId: ce.runId || "",
          importedAt: ce.importedAt || "",
          evidence: Array.isArray(ce.evidence) ? ce.evidence.slice() : [],
        } : null,
      });
    });

    var scoreByPillar = {};
    pillars.forEach(function (p) {
      try { scoreByPillar[p] = self.getPillarScore ? (self.getPillarScore(p) || 0) : 0; }
      catch (_e) { scoreByPillar[p] = 0; }
    });
    var overall = 0;
    try { overall = self.getOverallScore ? (self.getOverallScore() || 0) : 0; } catch (_e) { /* */ }
    var maturityLevel;
    if (overall >= 80) maturityLevel = "Established";
    else if (overall >= 50) maturityLevel = "Developing";
    else if (overall > 0) maturityLevel = "Initial";
    else maturityLevel = "Not assessed";

    var manifestVersion = "";
    if (this.solutionsLock && this.solutionsLock.source && this.solutionsLock.source.ref) {
      manifestVersion = String(this.solutionsLock.source.ref);
    }
    if (!manifestVersion && this.data && this.data.frameworkVersion) {
      manifestVersion = String(this.data.frameworkVersion);
    }

    var solutionsLock = { ref: "", commit: "" };
    if (this.solutionsLock && this.solutionsLock.source) {
      solutionsLock.ref = String(this.solutionsLock.source.ref || "");
      solutionsLock.commit = String(this.solutionsLock.source.commit || "");
    }

    return {
      schemaVersion: ENVELOPE_SCHEMA_VERSION,
      generatedAt: new Date().toISOString(),
      assessor: identity,
      scope: { tier: tier, pillars: pillars },
      manifest: { version: manifestVersion, controlCount: controlsList.length || 58 },
      solutionsLock: solutionsLock,
      answers: answers,
      summary: {
        yes: summary.yes,
        partial: summary.partial,
        no: summary.no,
        na: summary.na,
        unanswered: summary.unanswered,
        overall: overall,
        scoreByPillar: scoreByPillar,
        maturityLevel: maturityLevel,
      },
      signatures: {
        assessorSignedAt: null,
        facilitatorSignedAt: null,
      },
    };
  };

  /** Apply a previously-exported envelope back into state. */
  AssessmentApp.prototype.importEnvelope = function (envelope) {
    if (!envelope || typeof envelope !== "object") {
      throw new Error("Envelope must be an object");
    }
    if (envelope.schemaVersion && String(envelope.schemaVersion).indexOf("fsi-copilotgov-envelope/") !== 0) {
      throw new Error("Not a CopilotGov envelope: " + envelope.schemaVersion);
    }
    if (!this.state) {
      this.state = this.newState();
    }
    var state = this.state;
    state.responses = state.responses || {};
    state.collectorEvidence = {};
    state.collectorPriorAnswers = state.collectorPriorAnswers || {};

    if (envelope.assessor) {
      this.setEnvelopeIdentity(envelope.assessor);
      state.scoping = state.scoping || {};
      if (envelope.assessor.name) state.scoping.assessorName = envelope.assessor.name;
      if (envelope.assessor.role) state.scoping.assessorRole = envelope.assessor.role;
      if (envelope.assessor.org) state.scoping.organizationName = envelope.assessor.org;
    }
    if (envelope.scope && envelope.scope.tier) {
      state.scoping = state.scoping || {};
      state.scoping.targetLevel = normalizeLevel(envelope.scope.tier);
    }

    var anyCollector = false;
    var anyRunId = "";
    (Array.isArray(envelope.answers) ? envelope.answers : []).forEach(function (a) {
      if (!a || !a.controlId) return;
      var resp = state.responses[a.controlId] || {};
      if (a.answer) resp.answer = a.answer;
      if (typeof a.notes === "string") resp.notes = a.notes;
      state.responses[a.controlId] = resp;
      if (a.collectorEvidence) {
        anyCollector = true;
        state.collectorEvidence[a.controlId] = {
          status: a.collectorEvidence.status || null,
          runId: a.collectorEvidence.runId || "",
          importedAt: a.collectorEvidence.importedAt || "",
          evidence: Array.isArray(a.collectorEvidence.evidence) ? a.collectorEvidence.evidence : [],
        };
        if (a.collectorEvidence.runId) anyRunId = a.collectorEvidence.runId;
      }
    });
    if (anyCollector && anyRunId) state.collectorRunId = anyRunId;
    if (!anyCollector) delete state.collectorEvidence;
    this.saveToStorage();
    return { controls: (envelope.answers || []).length, collectorRows: anyCollector };
  };

  AssessmentApp.prototype.exportEnvelope = function () {
    var self = this;
    var identity = this.getEnvelopeIdentity();
    if (!identity.name || !identity.org) {
      this._promptEnvelopeIdentity(function (id) {
        self.setEnvelopeIdentity(id);
        self._finalizeEnvelopeDownload();
      });
      return;
    }
    this._finalizeEnvelopeDownload();
  };

  AssessmentApp.prototype._finalizeEnvelopeDownload = function () {
    var envelope = this.buildEnvelope();
    var blob = new Blob([JSON.stringify(envelope, null, 2)], { type: "application/json" });
    var now = new Date();
    var pad = function (n) { return String(n).length < 2 ? "0" + n : String(n); };
    var stamp = now.getUTCFullYear() + pad(now.getUTCMonth() + 1) + pad(now.getUTCDate()) + "-" +
      pad(now.getUTCHours()) + pad(now.getUTCMinutes());
    downloadBlob(blob, "fsi-copilotgov-assessment-" + stamp + ".json");
    this.setMessage(
      "success",
      "Envelope exported",
      "Downloaded the portal governance envelope (schema " + ENVELOPE_SCHEMA_VERSION + ")."
    );
  };

  AssessmentApp.prototype._promptEnvelopeIdentity = function (onSave) {
    var self = this;
    var content = h("div");
    content.appendChild(h("p", { className: "ag-card-subtitle" },
      "These identity fields are saved in your browser for future exports. " +
      "They are embedded in the envelope so portal reviewers know who submitted the assessment."));
    var form = h("div", { className: "ag-identity-form" });
    var current = this.getEnvelopeIdentity();
    var nameIn = h("input", { type: "text", id: "envelope-identity-name", className: "ag-input", value: current.name, placeholder: "e.g., Jane Doe" });
    var roleIn = h("input", { type: "text", id: "envelope-identity-role", className: "ag-input", value: current.role, placeholder: "e.g., Compliance Lead" });
    var orgIn  = h("input", { type: "text", id: "envelope-identity-org",  className: "ag-input", value: current.org,  placeholder: "e.g., Acme Bank, N.A." });
    form.appendChild(h("label", { htmlFor: "envelope-identity-name" }, "Assessor name"));
    form.appendChild(nameIn);
    form.appendChild(h("label", { htmlFor: "envelope-identity-role" }, "Role"));
    form.appendChild(roleIn);
    form.appendChild(h("label", { htmlFor: "envelope-identity-org" }, "Organization"));
    form.appendChild(orgIn);
    content.appendChild(form);
    var actions = h("div", { className: "ag-btn-group", style: "margin-top:1rem" });
    actions.appendChild(h("button", {
      className: "ag-btn ag-btn-primary",
      type: "button",
      onClick: function () {
        var id = { name: nameIn.value.trim(), role: roleIn.value.trim(), org: orgIn.value.trim() };
        if (!id.name || !id.org) {
          self.setMessage("warning", "Identity required",
            "Assessor name and organization are required for portal envelopes.");
          return;
        }
        var backdrop = form.closest ? form.closest(".ag-modal-backdrop") : null;
        if (backdrop && backdrop.parentNode) backdrop.parentNode.removeChild(backdrop);
        onSave(id);
      },
    }, "Save and continue"));
    content.appendChild(actions);
    this.showModal("Identify the assessor", content);
  };

  /** Import a saved envelope JSON file via the browser file picker. */
  AssessmentApp.prototype.importEnvelopeFromFile = function () {
    var self = this;
    var input = document.createElement("input");
    input.type = "file";
    input.accept = ".json,application/json";
    input.style.display = "none";
    input.addEventListener("change", function (e) {
      var f = e.target.files && e.target.files[0];
      if (!f) return;
      var reader = new FileReader();
      reader.onload = function (ev) {
        try {
          var parsed = JSON.parse(String(ev.target.result || "{}"));
          var result = self.importEnvelope(parsed);
          self.setMessage("success", "Envelope imported",
            "Restored " + result.controls + " answer rows. Review your progress before exporting again.");
          self.render();
        } catch (err) {
          self.setMessage("error", "Could not import envelope",
            "The file was not a valid CopilotGov envelope JSON. Details: " + (err && err.message ? err.message : err));
        }
      };
      reader.readAsText(f);
    });
    document.body.appendChild(input);
    input.click();
    setTimeout(function () { if (input.parentNode) input.parentNode.removeChild(input); }, 500);
  };

  window.AssessmentApp = AssessmentApp;
  // Test seam: expose AssessmentApp (and D1 helpers) to Node/vitest when present.
  // No-op in browser.
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
      AssessmentApp: AssessmentApp,
      isAuthored: isAuthored,
      isTodoString: isTodoString,
      authoredOr: authoredOr,
      parseCollectorCsv: parseCollectorCsv,
      parseCollectorJson: parseCollectorJson,
      DRAWER_NOTES_PREFIX: DRAWER_NOTES_PREFIX,
      FACILITATOR_MODE_KEY: FACILITATOR_MODE_KEY,
      SOLUTIONS_BASE_URL: SOLUTIONS_BASE_URL,
      COLLECTOR_EVIDENCE_KEY_PREFIX: COLLECTOR_EVIDENCE_KEY_PREFIX,
      COLLECTOR_STATUS_MAP: COLLECTOR_STATUS_MAP,
      ENVELOPE_SCHEMA_VERSION: ENVELOPE_SCHEMA_VERSION,
      ENVELOPE_IDENTITY_KEY: ENVELOPE_IDENTITY_KEY,
    };
  }
})();
