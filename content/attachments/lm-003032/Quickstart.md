# Quickstart — Global Style Closed-Loop Runtime v0.9

## 1. Run one query

```bash
python -m style_runtime "低飽和、空氣感、偏日式、不要太網紅臉" --output result.json
```

## 2. Run bundled demos

```bash
python run_demo.py
```

## 3. Run tests

```bash
python -m unittest discover -s tests -v
```

## 4. What this prototype really does

It executes the full control loop:

```text
query
→ style search
→ prompt compile
→ GAR-like binding
→ runtime packet
→ mock backend
→ P/Q/A/S/D/H/C/R scoring
→ adaptive decision
→ state patch
→ next round
```

The backend is intentionally mock-only in v0.9. The generated `ComfyUI patch plan` and `Diffusers config` are the handoff boundary for a real image backend.
