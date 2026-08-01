#!/usr/bin/env python3
from pathlib import Path
import tempfile,shutil,json,subprocess,hashlib,os
ROOT=Path(__file__).resolve().parent

def h(p):
 x=hashlib.sha256();x.update(p.read_bytes());return x.hexdigest()
def reindex(root):
 idx=json.loads((root/'artifact_index.json').read_text());idx['sha256']={k:h(root/k) for k in idx['sha256']};(root/'artifact_index.json').write_text(json.dumps(idx,indent=2))
def run(root,*args):return subprocess.run(['python','rhcert.py',*args],cwd=root,text=True,capture_output=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
def main():
 # Hash mutation must fail before verifier execution.
 with tempfile.TemporaryDirectory() as td:
  t=Path(td)/'pkg';shutil.copytree(ROOT,t);p=t/'records/W17/chamber_subdivision_certificate.json';p.write_text(p.read_text()+'\n ')
  c=run(t,'verify','--integrity-only');assert c.returncode==2 and 'INTEGRITY_FAILURE' in c.stdout
 # Semantic parameter mutation with a recomputed hash must still fail the native verifier.
 with tempfile.TemporaryDirectory() as td:
  t=Path(td)/'pkg';shutil.copytree(ROOT,t);p=t/'records/W16/three_parameter_tube_certificate.json';d=json.loads(p.read_text());d['basis']['h_center']['num']=str(int(d['basis']['h_center']['num'])+1);p.write_text(json.dumps(d));reindex(t)
  c=run(t,'verify','--record','RH-W-16');assert c.returncode==1 and '[FAIL]' in c.stdout
 # RH claim mutation is rejected by manifest validation even after reindexing.
 with tempfile.TemporaryDirectory() as td:
  t=Path(td)/'pkg';shutil.copytree(ROOT,t);p=t/'rh_certificate_manifest_v0.1.json';d=json.loads(p.read_text());d['claim_firewall']['RH_CLAIM']=True;p.write_text(json.dumps(d));reindex(t)
  c=run(t,'verify','--integrity-only');assert c.returncode!=0
 print('hash_tamper=REJECTED')
 print('semantic_parameter_mismatch=REJECTED')
 print('RH_claim_escalation=REJECTED')
 print('status=BACKEND_REDTEAM_OK')
 print('RH_CLAIM=False')
if __name__=='__main__':main()
