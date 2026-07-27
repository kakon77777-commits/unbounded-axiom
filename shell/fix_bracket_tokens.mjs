// Fix: interval notation like "\gamma \in (0,1\]" or "\beta_1 \in \[0, \beta_max\]"
// uses \[ / \] as if they were literal bracket characters, but \[ and \] have
// a reserved meaning to this site's renderer (the displayMathBracket /
// inlineMathParen extensions in md.ts use \[...\] as an ALTERNATE display-math
// delimiter pair, mirroring plain KaTeX where \] alone mid-expression is
// parsed as an attempted command -- "Can't use function '\]' in math mode").
// Since these instances appear INSIDE the .text of an already-tokenized
// blockKatex/inlineKatex token (i.e. already inside $...$/$$...$$), they can
// never be a genuine \[...\] block boundary -- that extension only ever
// matches at the top level, before the dollar-delimited tokenizer even runs.
// So any bare \[ or \] found inside a dollar-math token's text is unambiguously
// a literal bracket character that needs to lose its backslash. Excludes
// \left[ / \right] (valid auto-sizing-delimiter commands, not the target).
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

// Bare \[ or \] not preceded by "left"/"right" (case: \left[ \right]).
const BARE_BRACKET_RE = /\\([[\]])/g;
function isBad(text) {
  return [...text.matchAll(BARE_BRACKET_RE)].some(m => {
    const before = text.slice(Math.max(0, m.index - 5), m.index);
    return !/(left|right)$/.test(before);
  });
}

function fixRaw(raw) {
  let n = 0;
  const fixed = raw.replace(/\\([[\]])/g, (m, bracket, offset) => {
    const before = raw.slice(Math.max(0, offset - 5), offset);
    if (/(left|right)$/.test(before)) return m;
    n += 1;
    return bracket;
  });
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
    report.push(`${path.relative(ROOT, f)}: ${fileEdits} bracket(s) unescaped`);
    if (!DRY) fs.writeFileSync(f, text, 'utf-8');
  }
}

fs.writeFileSync('D:/tmp/fix_bracket_tokens_report.txt',
  `${DRY ? '[DRY RUN] ' : ''}files touched: ${totalFiles}, total edits: ${totalEdits}\n\n` + report.join('\n'), 'utf-8');
console.log(`${DRY ? '[DRY RUN] ' : ''}files touched: ${totalFiles}, total edits: ${totalEdits}`);
