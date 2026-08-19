# Run Guide — Anima Metadata Census / Source Adapter v0.2

## A. Parse an already-downloaded `data.js`

```bash
python anima_source_adapter.py \
  --input data.js \
  --out dist/anima \
  --snapshot-id theta-data-js-YYYYMMDD
```

## B. Parse a normalized `artists.json`

```bash
python anima_source_adapter.py \
  --input artists.json \
  --out dist/anima \
  --snapshot-id fullet-artists-json-YYYYMMDD
```

## C. Download then parse (when the machine has network access)

```bash
python anima_source_adapter.py \
  --url "https://raw.githubusercontent.com/fulletLab/comfyui-anima-style-nodes/refs/heads/master/data/artists.json" \
  --download-to source/artists \
  --out dist/anima \
  --snapshot-id fullet-master-YYYYMMDD
```

The adapter can also consume the legacy Theta `data.js` shape if that source is available.

## Outputs

```text
artist_tag.csv
style_observation.jsonl
style_kernel.jsonl
source_provenance.json
census.json
```

`style_kernel.jsonl` intentionally contains null axes in v0.2. A model-conditioned preview is metadata evidence, not yet a validated eight-dimensional Style Kernel. Visual analysis belongs to v0.3.

## Safety

- JavaScript is never evaluated.
- Preview files are not downloaded by default.
- Preview URLs are recorded as references.
- `Works` and `Uniqueness` remain source-conditioned metrics, not artistic-quality scores.
