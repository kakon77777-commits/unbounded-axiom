#!/usr/bin/env python3
import json
from pathlib import Path
p=Path(__file__).with_name('backend_snapshot.json');d=json.loads(p.read_text())
assert d['schema']=='RH-W-18-backend-selftest-v0.1'
assert d['claim_firewall']['RH_CLAIM'] is False
assert d['historical_record_count']==14
assert d['known_legacy_incomplete']==['RH-W-06']
assert d['superseded_recertified']==['RH-W-14']
assert len(set(d['certificate_kinds']))==5
print('BACKEND_SCHEMA_SELFTEST_OK')
print('RH_CLAIM=False')
