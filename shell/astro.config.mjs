import { defineConfig } from 'astro/config';

// Prototype: static human shell that reads the engine's JSON output in ../dist
// (api/papers/index.json, ai/corpus.json, ai/timeline.json) + raw markdown.
export default defineConfig({
  site: 'https://logic.evemisslab.com',
  build: { format: 'directory' },
});
