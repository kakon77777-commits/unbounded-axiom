// Fix: \left{ ... \right} (bare braces as delimiter arguments) should be
// \left\{ ... \right\} -- a bare { immediately after \left is consumed by
// TeX/KaTeX as an ordinary grouping brace, not as \left's delimiter argument,
// which corrupts brace-depth tracking for everything until \right, producing
// "Expected '}', got '\right'" (confirmed directly against katex.renderToString).
// Same fix shape for \right} -> \right\}.
import { marked } from 'marked';
import markedKatex from 'marked-katex-extension';
import fs from 'node:fs';
import path from 'node:path';

marked.use(markedKatex({ throwOnError: false, nonStandard: false }));

const DRY = process.argv.includes('--dry-run');
const ROOT = path.resolve(process.cwd(), '..');
const PAPERS_DIR = path.join(ROOT, 'content', 'papers');

function walkFiles(dir) {
  let out = [];
  for (const name of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, name.name);
    if (name.isDirectory()) out = out.concat(walkFiles(p));
    else if (name.name.endsWith('.md')) out.push(p);
  }
  return out;
}

function collectMathTokens(tokens, out) {
  for (const t of tokens) {
    if (t.type === 'blockKatex' || t.type === 'inlineKatex') out.push(t);
    if (t.tokens) collectMathTokens(t.tokens, out);
    if (t.items) collectMathTokens(t.items, out);
    for (const key of ['header', 'rows']) {
      if (t[key]) {
        const cells = key === 'header' ? t[key] : t[key].flat();
        for (const cell of cells) {
          if (cell && cell.tokens) collectMathTokens(cell.tokens, out);
        }
      }
    }
  }
}

const LEFT_BRACE_RE = /\\left\{/g;
const RIGHT_BRACE_RE = /\\right\}/g;
function isBad(text) {
  return LEFT_BRACE_RE.test(text) || RIGHT_BRACE_RE.test(text);
}
function fixRaw(raw) {
  let n = 0;
  let fixed = raw.replace(/\\left\{/g, () => { n++; return '\\left\\{'; });
  fixed = fixed.replace(/\\right\}/g, () => { n++; return '\\right\\}'; });
  return [fixed, n];
}

const files = walkFiles(PAPERS_DIR);
let totalFiles = 0;
let totalEdits = 0;
const report = [];

for (const f of files) {
  let text = fs.readFileSync(f, 'utf-8');
  let tokens;
  try { tokens = marked.lexer(text); } catch { continue; }
  const mathTokens = [];
  collectMathTokens(tokens, mathTokens);
  const bad = mathTokens.filter(t => isBad(t.text));
  if (!bad.length) continue;

  let fileEdits = 0;
  const seen = new Set();
  for (const t of bad) {
    if (seen.has(t.raw)) continue;
    seen.add(t.raw);
    const [fixedRaw, n] = fixRaw(t.raw);
    if (n > 0 && text.includes(t.raw)) {
      text = text.split(t.raw).join(fixedRaw);
      fileEdits += n;
    }
  }
  if (fileEdits > 0) {
    totalFiles += 1;
    totalEdits += fileEdits;
    report.push(`${path.relative(ROOT, f)}: ${fileEdits} brace(s) escaped`);
    if (!DRY) fs.writeFileSync(f, text, 'utf-8');
  }
}

fs.writeFileSync('D:/tmp/fix_left_right_brace_report.txt',
  `${DRY ? '[DRY RUN] ' : ''}files touched: ${totalFiles}, total edits: ${totalEdits}\n\n` + report.join('\n'), 'utf-8');
console.log(`${DRY ? '[DRY RUN] ' : ''}files touched: ${totalFiles}, total edits: ${totalEdits}`);
