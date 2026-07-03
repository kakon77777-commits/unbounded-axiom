// Shared marked instance, configured ONCE (module singleton) so KaTeX runs at
// build time (server-side render → static <span class="katex"> HTML, no client JS).
// throwOnError:false → a malformed $...$ in any paper renders as inline error text
// instead of crashing the whole 1100+ paper build. nonStandard:false keeps the
// standard delimiter rules (opening $ not followed by space) to limit false matches
// on prose like currency.
import { marked } from 'marked';
import markedKatex from 'marked-katex-extension';

marked.use(markedKatex({ throwOnError: false, nonStandard: false }));

export { marked };
