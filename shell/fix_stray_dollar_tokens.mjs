// Fix for the dominant remaining KaTeX error category: marked-katex-extension's
// "standard" inline rule requires a closing $ to be followed by whitespace or
// one of [?!.,:？！。，：] (see node_modules/marked-katex-extension/src/index.js,
// inlineRule's trailing lookahead). When a closing $ is instead immediately
// followed by some other character -- most commonly `_` from markdown's
// underscore-bold syntax touching the delimiter with no space ("$math$__bold__")
// -- that lookahead fails, so the tokenizer does NOT treat it as a close. It
// backtracks and keeps extending the match forward until it finds a LATER $
// that does satisfy the lookahead, silently fusing what should have been two+
// separate math spans (and any prose between them) into one broken token whose
// text contains a stray, unescaped $ in the middle -- which is what KaTeX then
// chokes on ("Can't use function '$' in math mode", or a cascading parse
// failure if the fused span also swallows unrelated structure).
//
// This script uses the REAL marked + marked-katex-extension tokenizer (the
// same one shell/src/lib/md.ts configures for the actual site build) to find
// every math token whose text contains a bare $ -- i.e. every span the real
// renderer will genuinely choke on, no heuristic guessing about scope. For
// each, it inserts a single space after every "$" in that token's raw source
// text that isn't already followed by whitespace/allowed-punctuation/EOL,
// which lets the closing lookahead succeed at the FIRST intended boundary
// instead of bleeding into the next span. Fix is applied only within the
// confirmed-broken raw span (via exact string replace in the source file),
// never to healthy content elsewhere in the corpus.
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

// Allowed characters after a $ that should NOT get a space inserted: the
// exact set marked-katex-extension's own inlineRule lookahead accepts, plus
// end-of-string. Also skip when the $ is already followed by another $
// (part of a $$ pair) or preceded by a backslash (already-escaped \$).
const ALLOWED_AFTER = /[\s?!.,:？！。，：$]/;

function fixRaw(raw) {
  let out = '';
  let n = 0;
  for (let i = 0; i < raw.length; i++) {
    const ch = raw[i];
    out += ch;
    if (ch === '$' && raw[i - 1] !== '\\') {
      const next = raw[i + 1];
      if (next !== undefined && !ALLOWED_AFTER.test(next)) {
        out += ' ';
        n += 1;
      }
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
  try {
    tokens = marked.lexer(text);
  } catch (e) {
    continue;
  }
  const mathTokens = [];
  collectMathTokens(tokens, mathTokens);
  const bad = mathTokens.filter(t => /(?<!\\)\$/.test(t.text));
  if (!bad.length) continue;

  let fileEdits = 0;
  const seen = new Set();
  for (const t of bad) {
    if (seen.has(t.raw)) continue; // same raw span already fixed this file
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
    report.push(`${path.relative(ROOT, f)}: ${fileEdits} space(s) inserted`);
    if (!DRY) fs.writeFileSync(f, text, 'utf-8');
  }
}

fs.writeFileSync('D:/tmp/fix_stray_dollar_tokens_report.txt',
  `${DRY ? '[DRY RUN] ' : ''}files touched: ${totalFiles}, total edits: ${totalEdits}\n\n` + report.join('\n'), 'utf-8');
console.log(`${DRY ? '[DRY RUN] ' : ''}files touched: ${totalFiles}, total edits: ${totalEdits}`);
