from __future__ import annotations
import csv, json
from pathlib import Path

root=Path(__file__).parent
rows=list(csv.DictReader((root/'RH-W-02_subgaps_v0.2.csv').open(encoding='utf-8')))
data=json.loads((root/'RH-W-02_subgaps_v0.2.json').read_text(encoding='utf-8'))
ids=[r['id'] for r in rows]
assert len(ids)==len(set(ids))
assert rows==data
assert all(r['parent']=='RH-W-02' for r in rows)
assert 'RH-W-02-NORMALIZATION' in ids
assert next(r for r in rows if r['id']=='RH-W-02-NORMALIZATION')['status']=='CLOSED_FOR_ENDPOINT_NULL_CORE'
text=f"records={len(rows)}\nids=OK\ncsv_json_match=OK\nnormalization_status=OK\nVALID\n"
print(text,end='')
(root/'REGISTRY_VALIDATION.txt').write_text(text,encoding='utf-8')
