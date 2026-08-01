#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse,hashlib,json,subprocess,tempfile,shutil,sys,os
ROOT=Path(__file__).resolve().parent
SECURITY_SUFFIXES={'.py','.json'}

def sha256(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''): h.update(b)
 return h.hexdigest()
def load(): return json.loads((ROOT/'rh_certificate_manifest_v0.2.json').read_text())
def record_digest(directory, indexed):
 prefix=directory.rstrip('/')+'/'
 rows=[]
 for rel,dig in sorted(indexed.items()):
  if rel.startswith(prefix): rows.append(rel+'\0'+dig)
 return hashlib.sha256('\n'.join(rows).encode()).hexdigest()
def integrity():
 idx=json.loads((ROOT/'artifact_index.json').read_text()); expected=idx['sha256'];bad=[]
 for rel,exp in expected.items():
  p=ROOT/rel
  if not p.is_file(): bad.append({'file':rel,'reason':'MISSING'})
  else:
   got=sha256(p)
   if got!=exp: bad.append({'file':rel,'reason':'HASH_MISMATCH','expected':exp,'actual':got})
 allowed=set(idx.get('allowed_unindexed',[]))|{'artifact_index.json'}
 for p in ROOT.rglob('*'):
  if p.is_file() and p.suffix in SECURITY_SUFFIXES:
   rel=p.relative_to(ROOT).as_posix()
   if rel not in expected and rel not in allowed: bad.append({'file':rel,'reason':'UNINDEXED_SECURITY_FILE'})
 return bad

def safe_command(cmd,directory):
 if not isinstance(cmd,list) or len(cmd)<2 or cmd[0] not in ('python','python3'): return False
 for x in cmd[1:]:
  if not isinstance(x,str) or '\x00' in x: return False
  q=Path(x)
  if q.is_absolute() or '..' in q.parts: return False
 script=ROOT/directory/cmd[1]
 return script.is_file() and script.suffix=='.py'

def validate_manifest(m):
 if m['schema']!='RH-CERT-BACKEND-MANIFEST-v0.2': raise AssertionError('schema')
 if m['claim_firewall']['RH_CLAIM'] is not False: raise AssertionError('RH firewall')
 idx=json.loads((ROOT/'artifact_index.json').read_text())['sha256']
 ids=[r['id'] for r in m['records']]
 if len(ids)!=len(set(ids)): raise AssertionError('duplicate id')
 by={r['id']:r for r in m['records']}
 for r in m['records']:
  if r['status'] not in m['status_vocabulary']: raise AssertionError('status')
  if r['claim'].get('RH_CLAIM',False) is not False: raise AssertionError('record RH claim')
  if not safe_command(r['command'],r['directory']): raise AssertionError('unsafe command')
  for d in r['dependencies']:
   if d not in by or d==r['id']: raise AssertionError('dependency')
  got=record_digest(r['directory'],idx)
  if got!=r['input_digest']: raise AssertionError('record digest')
  tok=r['expected_token']
  if r['status']=='VERIFIED' and ('INCOMPLETE' in tok or 'PROTOCOL' in tok): raise AssertionError('status inflation')
  if r['status']=='LEGACY_INCOMPLETE' and 'INCOMPLETE' not in tok: raise AssertionError('incomplete token')
 # DAG check independent of manifest ordering.
 color={x:0 for x in ids}
 def dfs(u):
  if color[u]==1: raise AssertionError('dependency cycle')
  if color[u]==2:return
  color[u]=1
  for v in by[u]['dependencies']: dfs(v)
  color[u]=2
 for u in ids: dfs(u)
 return ids

def run_record(r):
 src=ROOT/r['directory']
 with tempfile.TemporaryDirectory(prefix='rhcert-') as td:
  dst=Path(td)/r['id'];shutil.copytree(src,dst)
  cp=subprocess.run(r['command'],cwd=dst,text=True,capture_output=True,timeout=r.get('timeout_seconds',90),env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
  out=(cp.stdout or '')+(cp.stderr or '')
  ok=cp.returncode==0 and r['expected_token'] in out and 'RH_CLAIM=False' in out and 'RH_CLAIM=True' not in out
  return {'id':r['id'],'kind':r['kind'],'declared_status':r['status'],'execution':'PASS' if ok else 'FAIL','returncode':cp.returncode,'expected_token':r['expected_token'],'input_digest':r['input_digest'],'output':out[-16000:],'ok':ok}

def main():
 ap=argparse.ArgumentParser(description='RH Batch-01 certificate backend v0.2')
 ap.add_argument('action',choices=['verify','list']);ap.add_argument('--record');ap.add_argument('--integrity-only',action='store_true');a=ap.parse_args()
 try:
  m=load();validate_manifest(m)
 except Exception as e:
  print(json.dumps({'status':'MANIFEST_REJECTED','reason':type(e).__name__+': '+str(e)},ensure_ascii=False,indent=2));return 3
 bad=integrity()
 if bad:
  print(json.dumps({'status':'INTEGRITY_FAILURE','failures':bad},ensure_ascii=False,indent=2));return 2
 if a.action=='list':
  for r in m['records']:print(f"{r['id']}\t{r['kind']}\t{r['status']}\t{r['input_digest'][:16]}")
  return 0
 if a.integrity_only:
  print('artifact_integrity=OK');print('manifest_dag=OK');print('command_policy=OK');print('RH_CLAIM=False');return 0
 selected=[r for r in m['records'] if not a.record or r['id']==a.record]
 if not selected: print('unknown record',file=sys.stderr);return 2
 results=[]
 for r in selected:
  z=run_record(r);results.append(z);print(f"[{z['execution']}] {r['id']} {r['status']} digest={z['input_digest'][:16]}")
  if z.get('output'):print(z['output'].rstrip())
 hard=[x for x in results if not x['ok']];counts={}
 for r in selected:counts[r['status']]=counts.get(r['status'],0)+1
 overall='PASS_WITH_DECLARED_LIMITATIONS' if not hard else 'FAIL'
 report={'schema':'RH-CERT-BACKEND-RUN-v0.2','overall':overall,'counts':counts,'results':results,'trust_root':'SELF_AUTHENTICATED_PACKAGE_ONLY','RH_CLAIM':False}
 (ROOT/'BACKEND_VERIFY.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
 print('---');print(f'overall={overall}');print('executed_records_passed='+str(sum(x['ok'] for x in results))+'/'+str(len(results)));print('trust_root=SELF_AUTHENTICATED_PACKAGE_ONLY');print('claim_firewall=RH_CLAIM_FALSE');print('RH_CLAIM=False')
 return 0 if not hard else 1
if __name__=='__main__':raise SystemExit(main())
