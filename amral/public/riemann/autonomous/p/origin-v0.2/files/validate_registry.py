import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'gap_registry.json').read_text(encoding='utf-8'))
records = DATA['records']

errors = []
seen = set()
valid_status = {
    'KNOWN','FILLED','PROVISIONAL','OPEN','BLOCKED','EQUIVALENT_RISK',
    'CIRCULAR','REFUTED','NOT_FORMALIZED','CERTIFIED_NUMERICAL','EXPERIMENTAL'
}
for i, r in enumerate(records):
    rid = r.get('id','')
    if not re.match(r'^RH-[A-Z]+-[0-9]{2}$', rid):
        errors.append(f'bad id: {rid}')
    if rid in seen:
        errors.append(f'duplicate id: {rid}')
    seen.add(rid)
    if r.get('status') not in valid_status:
        errors.append(f'{rid}: invalid status')
    if not r.get('gap_types'):
        errors.append(f'{rid}: no gap types')
    if r.get('status') == 'FILLED' and not r.get('circularity_checked'):
        errors.append(f'{rid}: FILLED without circularity audit')
    if r.get('equivalent_risk') and r.get('status') == 'FILLED':
        errors.append(f'{rid}: equivalent-risk gap cannot be FILLED without explicit review')

print(f'records={len(records)}')
if errors:
    print('FAILED')
    for e in errors:
        print('-', e)
    raise SystemExit(1)
print('OK')
