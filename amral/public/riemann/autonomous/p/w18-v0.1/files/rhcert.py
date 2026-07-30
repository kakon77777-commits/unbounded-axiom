#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse,hashlib,json,subprocess,tempfile,shutil,sys,os,time
ROOT=Path(__file__).resolve().parent

def sha256(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()

def load():return json.loads((ROOT/'rh_certificate_manifest_v0.1.json').read_text())
def integrity():
 idx=json.loads((ROOT/'artifact_index.json').read_text());bad=[]
 for rel,exp in idx['sha256'].items():
  p=ROOT/rel
  if not p.is_file():bad.append({'file':rel,'reason':'MISSING'})
  else:
   got=sha256(p)
   if got!=exp:bad.append({'file':rel,'reason':'HASH_MISMATCH','expected':exp,'actual':got})
 return bad

def validate_manifest(m):
 assert m['schema']=='RH-CERT-BACKEND-MANIFEST-v0.1'
 assert m['claim_firewall']['RH_CLAIM'] is False
 ids=[r['id'] for r in m['records']];assert len(ids)==len(set(ids))
 pos={x:i for i,x in enumerate(ids)}
 for r in m['records']:
  assert r['status'] in m['status_vocabulary']
  for d in r['dependencies']:
   assert d in pos and d!=r['id']
  assert r['claim'].get('RH_CLAIM',False) is False
 return ids

def run_record(r):
 src=ROOT/r['directory']
 if not r['command']:return {'id':r['id'],'declared_status':r['status'],'execution':'SKIPPED','ok':True}
 with tempfile.TemporaryDirectory(prefix='rhcert-') as td:
  dst=Path(td)/r['id'];shutil.copytree(src,dst)
  cp=subprocess.run(r['command'],cwd=dst,text=True,capture_output=True,timeout=90,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
  out=(cp.stdout or '')+(cp.stderr or '')
  ok=cp.returncode==0 and r['expected_token'] in out and 'RH_CLAIM=False' in out
  return {'id':r['id'],'kind':r['kind'],'declared_status':r['status'],'execution':'PASS' if ok else 'FAIL','returncode':cp.returncode,'expected_token':r['expected_token'],'output':out[-12000:],'ok':ok}

def main():
 ap=argparse.ArgumentParser(description='RH Batch-01 unified certificate backend')
 ap.add_argument('action',choices=['verify','list'])
 ap.add_argument('--record')
 ap.add_argument('--integrity-only',action='store_true')
 a=ap.parse_args();m=load();validate_manifest(m)
 if a.action=='list':
  for r in m['records']:print(f"{r['id']}\t{r['kind']}\t{r['status']}")
  return 0
 bad=integrity()
 if bad:
  print(json.dumps({'status':'INTEGRITY_FAILURE','failures':bad},ensure_ascii=False,indent=2));return 2
 if a.integrity_only:
  print('artifact_integrity=OK');print('RH_CLAIM=False');return 0
 selected=[r for r in m['records'] if not a.record or r['id']==a.record]
 if not selected:print('unknown record',file=sys.stderr);return 2
 results=[]
 for r in selected:
  z=run_record(r);results.append(z);print(f"[{z['execution']}] {r['id']} {r['status']}")
  if z.get('output'):print(z['output'].rstrip())
 hard=[x for x in results if not x['ok']]
 counts={}
 for r in selected:counts[r['status']]=counts.get(r['status'],0)+1
 overall='PASS_WITH_DECLARED_LIMITATIONS' if not hard else 'FAIL'
 report={'schema':'RH-CERT-BACKEND-RUN-v0.1','overall':overall,'counts':counts,'results':results,'RH_CLAIM':False}
 (ROOT/'BACKEND_VERIFY.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
 print('---')
 print(f'overall={overall}')
 print('executed_records_passed='+str(sum(x['ok'] for x in results))+'/'+str(len(results)))
 print('claim_firewall=RH_CLAIM_FALSE')
 print('RH_CLAIM=False')
 return 0 if not hard else 1
if __name__=='__main__':raise SystemExit(main())
