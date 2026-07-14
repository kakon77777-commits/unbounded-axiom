# attachments-pending/

Staging area for companion files (code, images) whose parent paper doesn't have
an lm-id yet — either because the paper hasn't been ingested, or because it's
easier to group "these files go together" before sorting out exactly which
paper they attach to.

## How to use it

Drop a folder per paper/series, named however makes sense to you (paper title,
working name, series name — doesn't have to match anything else). Put whatever
belongs together inside it: code, images, data, notes.

```
ingest/attachments-pending/
  三門問題系列圖示/
    monty-hall-tree.png
    payoff-matrix.png
  Kneser圖驗證補充/
    verify_extra.py
```

Nothing here is processed automatically — no build step, no ingest stage reads
this folder. It's purely a human-curated holding area.

## How it gets resolved

Once the parent paper is published (has a real lm-id in `registry/papers.json`),
tell Claude which pending folder belongs to which paper. Claude will:

1. Copy the files into `content/attachments/{lm-id}/`
2. Add entries to `registry/companions.json` (`kind: "image"` gets an inline
   `<img>` preview on the paper's page instead of a plain download link — see
   `shell/src/pages/p/[id].astro`)
3. Rebuild so it shows up on the site

This folder is gitignored — it's a local workspace, not canon. The canonical
home for a resolved attachment is always `content/attachments/{lm-id}/`.
