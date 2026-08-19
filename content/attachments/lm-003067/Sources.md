# Sources — v0.2

Primary / repository sources consulted:

- ThetaCursed/Anima-Style-Explorer
  - https://github.com/ThetaCursed/Anima-Style-Explorer
  - The project describes 40,000+ Danbooru-tagged artist previews, fixed-control benchmarking, Works, and Uniqueness.

- nregret/Comfyui-Anima-Tools
  - https://github.com/nregret/Comfyui-Anima-Tools
  - Contains a large `js/data.js` artist database and frontend selector code.

- fulletLab/comfyui-anima-style-nodes
  - https://github.com/fulletLab/comfyui-anima-style-nodes
  - `artist_data.py` documents the safe legacy parse pattern:
    `const galleryData = [...]` -> JSON -> normalized records.
  - `data/artists.json` is a directly readable normalized snapshot.
  - Preview URL mapping is `ThetaCursed/Anima-Assets/main/images/{p}/{id}.webp`.
  - DATA_SOURCE.md states the dataset/reference materials derive from Anima Style Explorer and preview images come from Anima-Assets.

- Exact remotely inspected normalized snapshot:
  - https://raw.githubusercontent.com/fulletLab/comfyui-anima-style-nodes/refs/heads/master/data/artists.json
  - GitHub reports 140,002 lines; the file has 20,000 seven-line records plus array delimiters.

Important version boundary:
- The current upstream Explorer advertises 40,000+ previews.
- The exact normalized snapshot remotely inspected in this v0.2 census is 20,000 records.
- These are deliberately stored as different source snapshots and are not treated as the same release.
