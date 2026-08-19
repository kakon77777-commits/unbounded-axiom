# Anima Metadata Census / Source Adapter v0.2

## Executive Result

v0.2 now has a **real, runnable source adapter**, not only a schema.

It supports both observed source shapes:

```text
Legacy upstream JS:
{id, name, post_count, p, uniqueness_score}

Normalized JSON snapshot:
{id, tag, works, p, uniqueness_score}
```

The implementation never evaluates JavaScript. It extracts the `galleryData` array and feeds only the array text into `json.loads()`.

---

## 1. Exact remotely verifiable snapshot

A directly readable normalized snapshot in `fulletLab/comfyui-anima-style-nodes/data/artists.json` was inspected.

Facts established from the raw file:

- total file lines: **140,002**
- record formatting: **7 lines / record**
- exact record count: **20,000**
- preview partitions observed: **1 … 20**
- highest Works entry: **18,629**
- tail Works entry: **96**

Because the list is Works-descending, positional Works thresholds are:

```text
Rank 1      18,629
Rank 5,000     314
Rank 10,000    194
Rank 15,000    141
Rank 20,000     96
```

So the ascending Works quartiles are approximately/exactly by position:

```text
Q1      141
Median  194
Q3      314
```

The file is a **20k normalized snapshot**. It must not be confused with the current upstream Anima Style Explorer claim of **40,000+ artist previews**.

---

## 2. Why this is useful

The normalized source makes the first ingestion stage straightforward:

$$
\text{source metadata}
\rightarrow
\text{canonical artist identity}
\rightarrow
\text{model-conditioned observation}
$$

But it does **not** justify:

$$
\text{artist identity}
=
\text{Anima model style}
$$

Therefore the canonical split remains:

```text
artist_tag.csv
style_observation.jsonl
style_kernel.jsonl
```

where `style_kernel.jsonl` is still `pending_visual_analysis`.

---

## 3. Preview resolver verified from consumer code

The reference preview path for the legacy Theta dataset is:

```text
https://raw.githubusercontent.com/ThetaCursed/Anima-Assets/main/images/{p}/{id}.webp
```

Therefore the source pair `(p, id)` is enough to produce a stable preview reference without downloading the preview.

Default policy remains:

```text
preview_policy = reference_only
```

---

## 4. Canonical normalization

Example:

```text
source tag:
hammer \(sunset beach\)

display:
hammer (sunset beach)

normalized join/search key:
hammer_(sunset_beach)

prompt tag:
@hammer \(sunset beach\)
```

This deliberately separates display identity, database key, and prompt syntax.

---

## 5. What the runnable adapter calculates on a full local source

Once a full `data.js` or `artists.json` is materialized locally, the adapter automatically emits exact:

- record count
- normalized unique tag count
- duplicate normalized tags
- missing-field counts
- Works min/Q1/median/Q3/max/mean
- Uniqueness min/Q1/median/Q3/max/mean
- partition counts
- preview-reference coverage

So we do not need to manually maintain those statistics.

---

## 6. What v0.2 intentionally does not fabricate

This package does **not** claim a full Uniqueness distribution for the 20k remote snapshot, because the complete file was not copied into the execution container in this session.

It also does not claim:

- preview HTTP success rate
- full duplicate count
- full missing-field count
- eight-dimensional Style Kernel values

Those become exact automatically when the adapter is run against the materialized source.

---

## 7. Tests

The bundled test suite validates:

1. safe JS parsing
2. normalized JSON parsing
3. parenthesis normalization
4. preview URL construction
5. end-to-end canonical output generation

All tests pass in this artifact build.

---

## 8. Next step

v0.3 should be the **Visual Observation Analyzer**:

```text
preview reference
→ private/on-demand cache
→ vision analysis
→ 8D Style Kernel
→ style embedding
→ nearest-neighbor graph
```

At that point the 20k/40k metadata nodes start becoming actual model-conditioned style geometry.
