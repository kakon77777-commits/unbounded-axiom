// Shared marked instance, configured ONCE (module singleton) so KaTeX runs at
// build time (server-side render → static <span class="katex"> HTML, no client JS).
// throwOnError:false → a malformed $...$ in any paper renders as inline error text
// instead of crashing the whole 1300+ paper build. nonStandard:false keeps the
// standard delimiter rules (opening $ not followed by space) to limit false matches
// on prose like currency.
import { marked } from 'marked';
import markedKatex from 'marked-katex-extension';
import katex from 'katex';

marked.use(markedKatex({ throwOnError: false, nonStandard: false }));

// ADDITIONAL delimiters: \[ … \] (display) and \( … \) (inline). GPT/Canvas authors
// math with these LaTeX-standard delimiters; without this they'd show as raw text
// (marked-katex only handles $/$$). This is a SEPARATE extension that never touches $
// handling, so currency ($5000, NT$120) stays literal. Guards keep it from eating
// non-math \[…\]: display must not cross a blank line (paragraph = code/prose, not a
// single math block) and must look like math; inline must be single-line and look
// like math too. "Looks like math" = a LaTeX command, OR a bare comparison/assignment
// (^ _ = < > ≤ ≥ ≠) — terse proof-style content (e.g. "\[ A>D \]", "\[ S_i \]") has
// neither prose nor a command, just the operator itself, and was silently falling
// through to literal bracketed text before this second signal was added.
const LATEX_CMD = /\\[a-zA-Z]/;
const LOOKS_LIKE_MATH = /[\^_=<>≤≥≠]/;
const BLANK_LINE = /\n[ \t]*\n/;
marked.use({
  extensions: [
    {
      name: 'displayMathBracket',
      level: 'block',
      start(src: string) { const i = src.indexOf('\\['); return i < 0 ? undefined : i; },
      tokenizer(src: string) {
        const m = /^\\\[[ \t]*\r?\n?([\s\S]*?)\r?\n?[ \t]*\\\]/.exec(src);
        if (!m) return undefined;
        const body = m[1];
        if (BLANK_LINE.test(body) || (!LATEX_CMD.test(body) && !LOOKS_LIKE_MATH.test(body))) return undefined;
        return { type: 'displayMathBracket', raw: m[0], text: body } as const;
      },
      renderer(token: any) {
        try { return katex.renderToString(token.text, { displayMode: true, throwOnError: false }); }
        catch { return token.raw; }
      },
    },
    {
      name: 'inlineMathParen',
      level: 'inline',
      start(src: string) { const i = src.indexOf('\\('); return i < 0 ? undefined : i; },
      tokenizer(src: string) {
        const m = /^\\\(([^\n]{1,300}?)\\\)/.exec(src);
        if (!m) return undefined;
        const body = m[1];
        if (!LATEX_CMD.test(body) && !LOOKS_LIKE_MATH.test(body)) return undefined;
        return { type: 'inlineMathParen', raw: m[0], text: body } as const;
      },
      renderer(token: any) {
        try { return katex.renderToString(token.text, { displayMode: false, throwOnError: false }); }
        catch { return token.raw; }
      },
    },
  ],
});

// marked-katex-extension's own $...$ boundary rule (read from its source, confirmed
// against the live renderer — see scripts/normalize_math.py's identical Python port,
// which this mirrors exactly): a closing $ needs whitespace/EOF/one of ?!.,:？！。，：
// right after it, and an opening $ needs a literal space/start-of-string before it.
// CJK enumeration punctuation like 、 and ； are NOT in that set, so "$X$、$Y$" written
// with no space (routine in Chinese academic prose) either silently drops or — worse —
// merges into one broken span containing a stray $ that KaTeX then rejects outright.
// Ingest-time padding (normalize_math.py) fixes this for newly-published papers, but
// that's a one-shot content mutation: it can't retroactively cover papers published
// before the rule existed, or before it was later refined. Padding here instead, right
// before every render, fixes ALL papers (old and new) permanently with no corpus sweep
// ever required again — and is a no-op on already-padded content (idempotent).
const FLANK_SAFE = new Set(['*', '_', '~']);
const RIGHT_SAFE_PUNCT = /^[\s?!.,:？！。，：]/;
const INLINE_MATH_SPAN = /\$(?:\\.|[^$\\\n])+?\$/g;
const DISPLAY_MATH_SPAN = /\$\$[\s\S]*?\$\$/g;

function padInlineMath(t: string): string {
  function padProse(seg: string): string {
    const out: string[] = [];
    let last = 0;
    let m: RegExpExecArray | null;
    INLINE_MATH_SPAN.lastIndex = 0;
    while ((m = INLINE_MATH_SPAN.exec(seg)) !== null) {
      out.push(seg.slice(last, m.index));
      const left = m.index > 0 ? seg[m.index - 1] : null;
      const right = m.index + m[0].length < seg.length ? seg[m.index + m[0].length] : null;
      const needLeft = left !== null && left !== ' ' && !FLANK_SAFE.has(left);
      const needRight = right !== null && !RIGHT_SAFE_PUNCT.test(right) && !FLANK_SAFE.has(right);
      out.push((needLeft ? ' ' : '') + m[0] + (needRight ? ' ' : ''));
      last = m.index + m[0].length;
    }
    out.push(seg.slice(last));
    return out.join('');
  }
  const res: string[] = [];
  let last = 0;
  let m: RegExpExecArray | null;
  DISPLAY_MATH_SPAN.lastIndex = 0;
  while ((m = DISPLAY_MATH_SPAN.exec(t)) !== null) {
    res.push(padProse(t.slice(last, m.index)));
    res.push(m[0]);
    last = m.index + m[0].length;
  }
  res.push(padProse(t.slice(last)));
  return res.join('');
}

// Render paper markdown: pad first (fixes $-boundary issues for every paper, old or
// new), then parse. Callers rendering paper content should use this instead of calling
// marked.parse directly; `marked` itself stays exported unwrapped for any other use.
function renderPaperMarkdown(raw: string): string {
  return marked.parse(padInlineMath(raw), { async: false }) as string;
}

export { marked, padInlineMath, renderPaperMarkdown };
