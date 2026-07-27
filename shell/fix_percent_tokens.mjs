// Fix: KaTeX treats an unescaped % as a LaTeX comment marker -- it silently
// consumes everything after it to end-of-input (there's no newline inside a
// single math expression string to terminate the "comment"), which is why
// this shows up as "Unexpected end of input in a macro argument, expected
// '}'": whatever brace-opening macro appeared before the % never finds its
// real closing brace, because that brace got eaten as commented-out text.
// Confirmed directly against katex.renderToString (see the commentAtEnd
// strict-mode warning). Every instance found in this corpus is a literal
// percentage ("28.3%", "100%") -- never an intentional LaTeX comment -- so
// escaping to \% is unconditionally correct wherever it appears inside a
// genuine math token.
//
// Same approach as fix_stray_dollar_tokens.mjs: use the real marked +
// marked-katex-extension tokenizer to find confirmed math tokens containing
// a bare %, then fix only within those exact raw spans.
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

function fixRaw(raw) {
  let out = '';
  let n = 0;
  for (let i = 0; i < raw.length; i++) {
    const ch = raw[i];
    if (ch === '%' && raw[i - 1] !== '\\') {
      out += '\\%';
      n += 1;
    } else {
      out += ch;
    }
  }
  return [out, n];
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
  const bad = mathTokens.filter(t => /(?<!\\)%/.test(t.text));
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
    report.push(`${path.relative(ROOT, f)}: ${fileEdits} percent(s) escaped`);
    if (!DRY) fs.writeFileSync(f, text, 'utf-8');
  }
}

fs.writeFileSync('D:/tmp/fix_percent_tokens_report.txt',
  `${DRY ? '[DRY RUN] ' : ''}files touched: ${totalFiles}, total edits: ${totalEdits}\n\n` + report.join('\n'), 'utf-8');
console.log(`${DRY ? '[DRY RUN] ' : ''}files touched: ${totalFiles}, total edits: ${totalEdits}`);
