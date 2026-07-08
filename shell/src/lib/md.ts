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
// single math block) and must contain a LaTeX command; inline must be single-line and
// look like math (a command or ^ _ =).
const LATEX_CMD = /\\[a-zA-Z]/;
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
        if (BLANK_LINE.test(body) || !LATEX_CMD.test(body)) return undefined;
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
        if (!LATEX_CMD.test(body) && !/[\^_=]/.test(body)) return undefined;
        return { type: 'inlineMathParen', raw: m[0], text: body } as const;
      },
      renderer(token: any) {
        try { return katex.renderToString(token.text, { displayMode: false, throwOnError: false }); }
        catch { return token.raw; }
      },
    },
  ],
});

export { marked };
