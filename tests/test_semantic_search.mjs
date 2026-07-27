#!/usr/bin/env node
// Runs tests/semantic_queries.jsonl against the REAL built index through the
// SAME semantic-core.js the browser Worker imports — no logic duplication.
// Usage: node tests/test_semantic_search.mjs
// Doubles as the §29 deliverable #12 "搜尋品質報告" — writes tests/quality-report.json.
import { readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { scoreCorpus, prepareIndex, DEFAULT_CONFIG } from "../shell/public/semantic/semantic-core.js";

const ROOT = dirname(dirname(fileURLToPath(import.meta.url)));

const indexPath = join(ROOT, "dist", "ai", "semantic-index.min.json");
const dictionaryPath = join(ROOT, "dist", "ai", "semantic-dictionary.min.json");
const configPath = join(ROOT, "shell", "public", "semantic", "search.config.json");
const queriesPath = join(ROOT, "tests", "semantic_queries.jsonl");

const index = JSON.parse(readFileSync(indexPath, "utf8"));
const dictionaryFile = JSON.parse(readFileSync(dictionaryPath, "utf8"));
const dictionary = dictionaryFile.entries || [];
const userConfig = JSON.parse(readFileSync(configPath, "utf8"));
const config = {
  ...DEFAULT_CONFIG, ...userConfig,
  search: { ...DEFAULT_CONFIG.search, ...userConfig.search },
  tiers: { ...DEFAULT_CONFIG.tiers, ...userConfig.tiers },
  weights: { ...DEFAULT_CONFIG.weights, ...userConfig.weights },
  channels: { ...DEFAULT_CONFIG.channels, ...userConfig.channels },
  expansion_limits: { ...DEFAULT_CONFIG.expansion_limits, ...userConfig.expansion_limits },
};
const documents = prepareIndex(index.documents);

const lines = readFileSync(queriesPath, "utf8").split("\n").map((l) => l.trim()).filter(Boolean);
const cases = lines.map((l) => JSON.parse(l));

let pass = 0, fail = 0;
const byCategory = {};
const details = [];

for (const c of cases) {
  const result = scoreCorpus(documents, c.query, config, dictionary);
  const ids = result.results.map((r) => r.id);
  const tierAIds = result.results.filter((r) => r.tier === "A").map((r) => r.id);
  const top10 = ids.slice(0, 10);

  let ok = true;
  const reasons = [];

  if (c.expected_tier_a) {
    const hit = c.expected_tier_a.some((id) => tierAIds.includes(id));
    if (!hit) { ok = false; reasons.push(`expected tier A among ${c.expected_tier_a}, got tiers=${JSON.stringify(result.results.slice(0, 5).map((r) => [r.id, r.tier, r.score.toFixed(2)]))}`); }
  }
  if (c.expected_any) {
    const hit = c.expected_any.some((id) => ids.includes(id));
    if (!hit) { ok = false; reasons.push(`expected any of ${c.expected_any} in ${ids.length} results`); }
  }
  if (c.expected_top10) {
    const hit = c.expected_top10.some((id) => top10.includes(id));
    if (!hit) { ok = false; reasons.push(`expected any of ${c.expected_top10} in top10=${JSON.stringify(top10)}`); }
  }
  if (c.expect_low_confidence) {
    if (!result.low_confidence) { ok = false; reasons.push(`expected low_confidence=true, got ${result.low_confidence} (relaxed=${result.relaxed}, threshold=${result.threshold})`); }
  }
  if (c.expect_not_low_confidence) {
    if (result.low_confidence) { ok = false; reasons.push(`expected low_confidence=false, got true (top result tier=${result.results[0] && result.results[0].tier}, score=${result.results[0] && result.results[0].score.toFixed(2)})`); }
  }
  if (c.expect_empty_query) {
    if (!result.empty_query) { ok = false; reasons.push(`expected empty_query=true`); }
  }
  if (c.expect_any_result) {
    if (!(result.results.length > 0)) { ok = false; reasons.push(`expected at least one result, got 0`); }
  }
  if (c.expect_alias_terms) {
    const gotTerms = (result.expansions.aliases || []).map((a) => a.term);
    const hit = c.expect_alias_terms.some((t) => gotTerms.includes(t));
    if (!hit) { ok = false; reasons.push(`expected one of alias terms ${JSON.stringify(c.expect_alias_terms)} in expansions.aliases=${JSON.stringify(gotTerms)}`); }
  }
  if (c.expect_no_expansion) {
    const total = (result.expansions.aliases || []).length + (result.expansions.related || []).length;
    if (total > 0) { ok = false; reasons.push(`expected no expansion terms, got aliases=${JSON.stringify(result.expansions.aliases)} related=${JSON.stringify(result.expansions.related)}`); }
  }
  // universal invariant regardless of category: with a non-empty corpus and a
  // non-empty query, the non-zero mechanism must never return zero results.
  if (c.query && documents.length > 0 && result.results.length === 0) {
    ok = false; reasons.push("non-zero guarantee violated: 0 results for a non-empty query against a non-empty index");
  }
  // §22.1 "支援最低結果數": ensure_minimum_results must actually reach the
  // configured floor whenever enough candidates exist in the whole corpus,
  // not just "more than zero" — a hand-typed exact title query legitimately
  // has few *lexical* neighbours, so this caught a real bug (relation-only
  // Tier D scores landing below absolute_floor and getting dropped).
  if (c.query && documents.length >= config.search.minimum_results && result.results.length < config.search.minimum_results && !result.empty_query) {
    ok = false; reasons.push(`minimum_results not met: expected >= ${config.search.minimum_results}, got ${result.results.length}`);
  }

  const cat = c.category || "uncategorized";
  byCategory[cat] = byCategory[cat] || { pass: 0, fail: 0 };
  if (ok) { pass++; byCategory[cat].pass++; } else { fail++; byCategory[cat].fail++; }
  details.push({ query: c.query, category: cat, ok, reasons, result_count: result.results.length, low_confidence: result.low_confidence, relaxed: result.relaxed });
  console.log(`[${ok ? "PASS" : "FAIL"}] (${cat}) ${JSON.stringify(c.query)}${ok ? "" : "\n       " + reasons.join("\n       ")}`);
}

console.log("");
console.log(`--- ${pass}/${cases.length} passed ---`);
for (const [cat, stats] of Object.entries(byCategory)) {
  console.log(`  ${cat}: ${stats.pass}/${stats.pass + stats.fail}`);
}

const report = {
  generated_at: new Date().toISOString(),
  index_count: documents.length,
  index_build_id: index.build_id,
  total: cases.length,
  passed: pass,
  failed: fail,
  by_category: byCategory,
  details,
};
writeFileSync(join(ROOT, "tests", "quality-report.json"), JSON.stringify(report, null, 2), "utf8");
console.log(`\nWrote tests/quality-report.json`);

process.exit(fail > 0 ? 1 : 0);
