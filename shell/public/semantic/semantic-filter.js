// Dynamic Semantic Revealing — main-thread controller.
// Spec: 02_動態語義顯影_本地端實作技術白皮書_v0.1.md (lm-001785), §14/§15/§28.
//
// Purely additive: if this script fails to load, or semantic_search_enabled
// is false in search.config.json, the page underneath is untouched — no URLs
// change, no row is removed from the DOM, nothing here is required to read
// the original timeline (§28.2).
(function () {
  "use strict";

  var ROOT_SELECTOR = "[data-semantic-root]";
  var root = document.querySelector(ROOT_SELECTOR);
  if (!root) return; // this page doesn't opt in to the search layer

  var rows = Array.prototype.slice.call(document.querySelectorAll(".paper-row[data-doc-id]"));
  if (!rows.length) return;

  var input = root.querySelector(".semantic-input");
  var inputWrap = root.querySelector(".semantic-input-wrap");
  var clearBtn = root.querySelector(".semantic-clear");
  var resetBtn = root.querySelector(".semantic-reset-btn");
  var modeBtns = Array.prototype.slice.call(root.querySelectorAll(".semantic-mode-btn"));
  var metaEl = root.querySelector(".semantic-meta");
  var expansionsEl = root.querySelector(".semantic-expansions");
  var bannerEl = root.querySelector(".semantic-banner");
  var box = root.querySelector(".semantic-box");
  if (!input) return;

  // Generic per-tier quality descriptor (§10). Kept deliberately mechanism-
  // agnostic — the specific WHY (title match, lexical overlap, same-series
  // relation, …) comes from the reason's own label right after it; a doc can
  // land in Tier D via either weak lexical similarity OR a real relation
  // match, so this prefix must not presume which one it was.
  var TIER_LABEL = { A: "A｜精確", B: "B｜近似", C: "C｜弱關聯", D: "D｜低相關" };
  var sections = Array.prototype.slice.call(document.querySelectorAll("section.section"));

  function escapeText(s) {
    var n = document.createTextNode(s == null ? "" : String(s));
    return n;
  }

  function clearNode(el) { while (el.firstChild) el.removeChild(el.firstChild); }

  // ---- worker lifecycle ----
  var worker = null;
  var reqSeq = 0;
  var latestReqId = 0;
  var ready = false;
  var pendingQuery = null;

  function startWorker() {
    try {
      worker = new Worker("/semantic/lexical-search-worker.js", { type: "module" });
    } catch (e) {
      box.style.display = "none";
      return;
    }
    worker.onmessage = function (e) {
      var msg = e.data || {};
      if (msg.type === "ready") {
        ready = true;
        if (msg.meta && typeof msg.meta.count === "number") {
          box.setAttribute("data-doc-count", String(msg.meta.count));
        }
        if (pendingQuery !== null) {
          var q = pendingQuery;
          pendingQuery = null;
          runSearch(q);
        }
        return;
      }
      if (msg.type === "result") {
        if (msg.reqId !== latestReqId) return; // stale reply, a newer keystroke already superseded it
        applyResult(msg.result, msg.latency_ms);
        return;
      }
      if (msg.type === "error") {
        metaEl.textContent = "";
        showBanner("索引載入失敗，搜尋暫時無法使用（原始時間線不受影響）。", "low");
      }
    };
    worker.postMessage({ type: "init" });
  }

  function runSearch(query) {
    if (!ready) { pendingQuery = query; return; }
    latestReqId = ++reqSeq;
    worker.postMessage({ type: "search", query: query, reqId: latestReqId });
  }

  // ---- reveal state ----
  function resetRows() {
    for (var i = 0; i < rows.length; i++) {
      var r = rows[i];
      r.classList.remove("semantic-tier-a", "semantic-tier-b", "semantic-tier-c", "semantic-tier-d", "semantic-hidden");
      r.removeAttribute("data-semantic-score");
      r.removeAttribute("data-semantic-tier");
      r.removeAttribute("data-semantic-visible");
      var reasonEl = r.querySelector(".semantic-reason");
      if (reasonEl) reasonEl.remove();
    }
    for (var s = 0; s < sections.length; s++) sections[s].classList.remove("semantic-empty-section");
  }

  function showBanner(text, cls) {
    clearNode(bannerEl);
    if (!text) { bannerEl.classList.remove("show", "low"); return; }
    bannerEl.appendChild(escapeText(text));
    bannerEl.classList.add("show");
    bannerEl.classList.toggle("low", cls === "low");
  }

  // §14.1 "顯示查詢展開" — a query that names a known concept (dictionary §7)
  // shows what it was ALSO expanded to search for, so a hit via an alias or a
  // related term is never a silent surprise.
  function renderExpansions(expansions) {
    clearNode(expansionsEl);
    if (!expansionsEl) return;
    var aliases = (expansions && expansions.aliases) || [];
    var related = (expansions && expansions.related) || [];
    if (!aliases.length && !related.length) {
      expansionsEl.classList.remove("show");
      return;
    }
    var parts = [];
    if (aliases.length) parts.push("別名：" + aliases.map(function (a) { return a.term; }).join("、"));
    if (related.length) parts.push("相關詞：" + related.map(function (r) { return r.term; }).join("、"));
    expansionsEl.appendChild(escapeText("查詢展開 — " + parts.join(" ｜ ")));
    expansionsEl.classList.add("show");
  }

  function applyResult(result, latencyMs) {
    resetRows();

    if (result.empty_query) {
      showBanner("");
      renderExpansions(null);
      metaEl.textContent = "";
      return;
    }

    var byId = {};
    for (var i = 0; i < result.results.length; i++) byId[result.results[i].id] = result.results[i];

    var tierCounts = { A: 0, B: 0, C: 0, D: 0 };
    for (var j = 0; j < rows.length; j++) {
      var row = rows[j];
      var id = row.getAttribute("data-doc-id");
      var hit = byId[id];
      if (hit) {
        var tierClass = "semantic-tier-" + hit.tier.toLowerCase();
        row.classList.add(tierClass);
        row.setAttribute("data-semantic-score", hit.score.toFixed(2));
        row.setAttribute("data-semantic-tier", hit.tier);
        row.setAttribute("data-semantic-visible", "true");
        tierCounts[hit.tier] = (tierCounts[hit.tier] || 0) + 1;
        if (hit.reasons && hit.reasons.length) {
          // Label with the doc's REAL final tier (hit.tier, from assignTier()
          // against the actual configured thresholds), not the reason's own
          // guessed tier — a lexical-overlap reason hardcodes a B/C guess that
          // doesn't know about doc-level score adjustments (e.g. a relation
          // bump), so the two can disagree. The description text still comes
          // from the reason itself; only the tier badge is corrected.
          var top = hit.reasons[0];
          var span = document.createElement("span");
          span.className = "semantic-reason";
          span.appendChild(escapeText("· " + (TIER_LABEL[hit.tier] || hit.tier) + "：" + top.label));
          var titleEl = row.querySelector(".pt");
          (titleEl || row).appendChild(span);
        }
      } else {
        row.classList.add("semantic-hidden");
        row.setAttribute("data-semantic-visible", "false");
      }
    }

    for (var s = 0; s < sections.length; s++) {
      var sec = sections[s];
      var secRows = sec.querySelectorAll(".paper-row[data-doc-id]");
      if (!secRows.length) continue;
      var allHidden = true;
      for (var k = 0; k < secRows.length; k++) {
        if (!secRows[k].classList.contains("semantic-hidden")) { allHidden = false; break; }
      }
      sec.classList.toggle("semantic-empty-section", allHidden);
    }

    var statsParts = [];
    statsParts.push(result.total_candidates + " 篇索引");
    statsParts.push("A:" + tierCounts.A + " B:" + tierCounts.B + " C:" + tierCounts.C + " D:" + tierCounts.D);
    statsParts.push(latencyMs + "ms");
    metaEl.textContent = statsParts.join(" · ");
    renderExpansions(result.expansions);

    if (result.low_confidence) {
      showBanner("沒有找到高可信度直接結果。以下僅列出語義上最接近的文件。", "low");
    } else if (result.relaxed) {
      showBanner("直接命中較少，已加入詞彙與語義近似結果。", "");
    } else {
      showBanner("");
    }
  }

  function fullReset() {
    input.value = "";
    inputWrap.classList.remove("has-query");
    resetRows();
    showBanner("");
    renderExpansions(null);
    metaEl.textContent = "";
    latestReqId = ++reqSeq; // invalidate any in-flight search reply
  }

  // ---- input wiring (§14.1: 300ms debounce, Enter immediate, clear) ----
  var debounceMs = 300;
  var debounceTimer = null;
  function scheduleSearch() {
    var q = input.value;
    inputWrap.classList.toggle("has-query", q.length > 0);
    if (debounceTimer) clearTimeout(debounceTimer);
    if (!q.trim()) { fullReset(); return; }
    debounceTimer = setTimeout(function () { runSearch(q); }, debounceMs);
  }

  input.addEventListener("input", scheduleSearch);
  input.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      if (debounceTimer) clearTimeout(debounceTimer);
      var q = input.value;
      if (q.trim()) runSearch(q); else fullReset();
    } else if (e.key === "Escape") {
      fullReset();
      input.blur();
    }
  });
  if (clearBtn) clearBtn.addEventListener("click", function () { fullReset(); input.focus(); });
  if (resetBtn) resetBtn.addEventListener("click", fullReset);

  modeBtns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var mode = btn.getAttribute("data-mode");
      modeBtns.forEach(function (b) { b.setAttribute("aria-pressed", String(b === btn)); });
      document.body.classList.toggle("semantic-focus", mode === "focus");
    });
  });

  // ---- boot: load config for the single-flag kill switch + debounce/maxlength, then start ----
  fetch("/semantic/search.config.json")
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (cfg) {
      if (cfg && cfg.semantic_search_enabled === false) {
        box.style.display = "none";
        return;
      }
      if (cfg && cfg.debounce_ms) debounceMs = cfg.debounce_ms;
      if (cfg && cfg.max_query_length) input.setAttribute("maxlength", String(cfg.max_query_length));
      startWorker();
    })
    .catch(function () { startWorker(); }); // config missing is not fatal — defaults still work
})();
