import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

// The engine publishes its JSON to ../dist (sibling of this shell/ dir).
// Resolve robustly regardless of how astro is launched (cwd may vary).
function distDir(): string {
  const here = path.dirname(fileURLToPath(import.meta.url)); // shell/src/lib
  const candidates = [
    path.resolve(process.cwd(), '..', 'dist'),
    path.resolve(here, '..', '..', '..', 'dist'),
    path.resolve(process.cwd(), 'dist'),
  ];
  for (const c of candidates) {
    if (fs.existsSync(path.join(c, 'api', 'papers', 'index.json'))) return c;
  }
  return candidates[0];
}

const DIST = distDir();

function readJSON(rel: string): any {
  return JSON.parse(fs.readFileSync(path.join(DIST, rel), 'utf8'));
}

export interface Paper {
  id: string;
  title: string;
  language: string;
  authorship: string;
  month: string | null;
  canonical_url: string;
  raw_url: string;
  api_url: string;
}

export function getPapers(): Paper[] {
  return readJSON('api/papers/index.json').items as Paper[];
}

export function getCorpus(): {
  count: number;
  languages: Record<string, number>;
  authorship: Record<string, number>;
  project: string;
  generated_at: string;
} {
  return readJSON('ai/corpus.json');
}

export interface Media { audio?: string; audio_kind?: string; audio_title?: string; video?: string; }
export function getMedia(): Record<string, Media> {
  try { return readJSON('ai/media.json').media || {}; }
  catch { return {}; }
}

export interface Featured {
  audio?: string; audio_title?: string; audio_kind?: string;
  video?: string; video_title?: string; desc_zh?: string; desc_en?: string;
}
// Project-level intro media (about the whole corpus, not one paper) — the /listen hero.
export function getFeaturedMedia(): Featured | null {
  try { return readJSON('ai/media.json').featured || null; }
  catch { return null; }
}

export interface Companion {
  file: string; orig: string; label: string; kind: string;
  ext: string; bytes: number; raw_url: string; mime: string; retired_id?: string;
}
// parent lm-id -> its companion attachments (accompanying code / proofs / data /
// example sets served at /raw/{parent}/{file}). Empty object if none / file absent.
export function getCompanions(): Record<string, Companion[]> {
  try { return readJSON('ai/companions.json').companions || {}; }
  catch { return {}; }
}

export function getTimeline(): Array<{
  year: number;
  count: number;
  months: Array<{ month: string; count: number }>;
}> {
  return readJSON('ai/timeline.json').timeline;
}

export function getRaw(rawUrl: string): string {
  const p = path.join(DIST, rawUrl.replace(/^\//, ''));
  try {
    return fs.readFileSync(p, 'utf8');
  } catch {
    return '';
  }
}

export function extOf(p: Paper): string {
  const m = p.raw_url.match(/\.([a-z0-9]+)$/i);
  return m ? m[1].toLowerCase() : 'md';
}
