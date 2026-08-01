#!/usr/bin/env python3
from pathlib import Path
import json,tempfile
from verify_negative_certificate import verify
ROOT=Path(__file__).resolve().parent

def dump(p,o):p.write_text(json.dumps(o),encoding='utf-8')
def main():
 base={'certificate_version':'RH-W-04-v0.1','semantics':'NEGATIVE_ONLY','dimension':2,'rigor_level':'EXACT_RATIONAL','M_lower':[['-2','0'],['0','1']],'M_upper':[['-3/2','0'],['0','3/2']],'witness':['1','0']}
 with tempfile.TemporaryDirectory() as td:
  td=Path(td);p=td/'ok.json';dump(p,base);ok,r=verify(p);assert ok and r['status']=='CERTIFIED_NEGATIVE'
  q=dict(base);q['rigor_level']='FLOAT64_ONLY';p2=td/'bad.json';dump(p2,q);ok2,r2=verify(p2);assert not ok2 and r2['status']=='REJECTED_NOT_RIGOROUS'
  z=dict(base);z['problem_id']='RH_WEIL_ZETA';p3=td/'zeta.json';dump(p3,z);ok3,r3=verify(p3);assert not ok3 and r3['status']=='REJECTED_MISSING_ZETA_PROVENANCE'
 print('synthetic_exact_negative=ACCEPTED')
 print('float_only_certificate=REJECTED')
 print('zeta_claim_without_provenance=REJECTED')
 print('status=PROTOCOL_SELFTEST_OK_NO_RH_WITNESS_PRESENT')
 print('RH_CLAIM=False')
if __name__=='__main__':main()
