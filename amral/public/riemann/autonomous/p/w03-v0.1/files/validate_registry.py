#!/usr/bin/env python3
import json
from pathlib import Path

root=Path(__file__).resolve().parent
rows=json.loads((root/'RH-W-03_subgaps_v0.1.json').read_text(encoding='utf-8'))
ids=[r['id'] for r in rows]
assert len(ids)==len(set(ids)), 'duplicate IDs'
assert all(i.startswith('RH-W-03-') for i in ids)
required={'id','parent','status','severity','statement','next_action'}
assert all(required <= set(r) for r in rows)
contract=json.loads((root/'separation_contract.json').read_text(encoding='utf-8'))
assert contract['negative_semantics'].startswith('certified')
assert 'does not prove RH' in contract['positive_semantics']
print(f'records={len(rows)}')
print('ids=OK')
print('contract=OK')
print('ONE_SIDED_SEMANTICS=OK')
