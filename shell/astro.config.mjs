import { defineConfig } from 'astro/config';

// Prototype: static human shell that reads the engine's JSON output in ../dist
// (api/papers/index.json, ai/corpus.json, ai/timeline.json) + raw markdown.
export default defineConfig({
  site: 'https://unboundedaxiom.org',  // the one place the domain is written; pages read Astro.site
  build: { format: 'directory' },
});
