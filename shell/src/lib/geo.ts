// GEO (Generative/Answer-Engine Optimization) signal extraction.
//
// TypeScript mirror of scripts/geo_layer.py — keep the two conventions identical:
// docs/AI-Native 論文寫作規範.md defines an answer-first Q&A "## " heading and a
// self-contained "> **定義｜term**" blockquote. Both are detected straight out of
// the RAW MARKDOWN SOURCE (not the marked-rendered HTML) so parsing is independent
// of the renderer. This file is the one that actually ships: the Astro build
// overlays shell/dist onto dist/, replacing the Python engine's /p/{id}/ pages in
// production (see build-site.sh) — the Python side's own injection
// (scripts/idroutes.py) only matters for a standalone `python build.py` preview.
// The warn-only geo-lint report (registry/generated/geo-lint.json) is generated
// once, by the Python pass, ahead of this step — not duplicated here.

export interface QaSignal { question: string; answer: string }
export interface DefinitionSignal { term: string; body: string }
export interface GeoSignals { qa: QaSignal[]; definitions: DefinitionSignal[] }

const H2_QUESTION = /^##\s+(.+?)\s*$/gm;
const HEADING_ANY = /^#{1,6}\s+/;
const DEFINITION = /^>\s*\*\*(?:定義|Definition)\s*[｜:：]\s*(.+?)\*\*\s*[:：]?\s*(.*)$/gim;
const MD_EMPHASIS = /\*\*([^*]+)\*\*|\*([^*]+)\*|`([^`]+)`/g;

function stripEmphasis(text: string): string {
  return text.replace(MD_EMPHASIS, (_m, a, b, c) => a ?? b ?? c ?? '').trim();
}

function looksLikeQuestion(heading: string): boolean {
  const h = heading.trim();
  return h.endsWith('?') || h.endsWith('？');
}

export function extractGeoSignals(mdSource: string): GeoSignals {
  const src = mdSource.replace(/\r\n/g, '\n');
  const lines = src.split('\n');

  const qa: QaSignal[] = [];
  for (const m of src.matchAll(H2_QUESTION)) {
    const heading = m[1].trim();
    if (!looksLikeQuestion(heading)) continue;
    const startLine = src.slice(0, (m.index ?? 0) + m[0].length).split('\n').length;
    const answerLines: string[] = [];
    for (let i = startLine; i < lines.length; i++) {
      const ln = lines[i];
      if (!ln.trim()) {
        if (answerLines.length) break;
        continue;
      }
      if (HEADING_ANY.test(ln)) break;
      answerLines.push(ln.trim());
    }
    const answer = stripEmphasis(answerLines.join(' '));
    if (answer) qa.push({ question: stripEmphasis(heading), answer });
  }

  const definitions: DefinitionSignal[] = [];
  for (const m of src.matchAll(DEFINITION)) {
    const term = stripEmphasis((m[1] ?? '').trim());
    const body = stripEmphasis((m[2] ?? '').trim());
    if (term && body) definitions.push({ term, body });
  }

  return { qa, definitions };
}

export function geoJsonLdBlocks(signals: GeoSignals, canonical: string): object[] {
  const blocks: object[] = [];
  if (signals.qa.length) {
    blocks.push({
      '@context': 'https://schema.org',
      '@type': 'FAQPage',
      mainEntity: signals.qa.map((item) => ({
        '@type': 'Question',
        name: item.question,
        acceptedAnswer: { '@type': 'Answer', text: item.answer },
      })),
    });
  }
  if (signals.definitions.length) {
    const setId = `${canonical}#definitions`;
    blocks.push({
      '@context': 'https://schema.org',
      '@type': 'DefinedTermSet',
      '@id': setId,
      hasDefinedTerm: signals.definitions.map((d) => ({
        '@type': 'DefinedTerm',
        name: d.term,
        description: d.body,
        inDefinedTermSet: setId,
      })),
    });
  }
  return blocks;
}
