#!/usr/bin/env python3
from pathlib import Path
import tempfile,shutil,json,subprocess,hashlib,os
ROOT=Path(__file__).resolve().parent

def h(p):
 x=hashlib.sha256();
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):x.update(b)
 return x.hexdigest()
def record_digest(root,directory,idx):
 prefix=directory.rstrip('/')+'/'
 rows=[rel+'\0'+dig for rel,dig in sorted(idx.items()) if rel.startswith(prefix)]
 return hashlib.sha256('\n'.join(rows).encode()).hexdigest()
def refresh(root):
 ip=root/'artifact_index.json';idx=json.loads(ip.read_text());
 # Add all security-sensitive files under records and root if needed.
 for p in root.rglob('*'):
  if p.is_file() and p.suffix in ('.py','.json'):
   rel=p.relative_to(root).as_posix()
   if rel not in idx.get('allowed_unindexed',[]) and rel!='artifact_index.json': idx['sha256'][rel]=h(p)
 mpath=root/'rh_certificate_manifest_v0.2.json'
 m=json.loads(mpath.read_text())
 # Manifest digest is refreshed after record digests.
 for r in m['records']: r['input_digest']=record_digest(root,r['directory'],idx['sha256'])
 mpath.write_text(json.dumps(m,ensure_ascii=False,indent=2));idx['sha256']['rh_certificate_manifest_v0.2.json']=h(mpath)
 # Refresh every currently indexed file after mutations.
 for rel in list(idx['sha256']):
  p=root/rel
  if p.is_file(): idx['sha256'][rel]=h(p)
 ip.write_text(json.dumps(idx,ensure_ascii=False,indent=2))
def run(root,*args):return subprocess.run(['python','rhcert.py',*args],cwd=root,text=True,capture_output=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
def expect(name,cond,detail,out):
 if not cond: raise AssertionError(name+' failed\n'+out)
 print(f'{name}={detail}')

def main():
 rejected=0; survived=0
 # Z01 raw hash mutation.
 with tempfile.TemporaryDirectory() as td:
  t=Path(td)/'pkg';shutil.copytree(ROOT,t);p=t/'records/W17/chamber_subdivision_certificate.json';p.write_text(p.read_text()+'\n ')
  c=run(t,'verify','--integrity-only');expect('HASH_TAMPER',c.returncode==2 and 'HASH_MISMATCH' in c.stdout,'REJECTED',c.stdout+c.stderr);rejected+=1
 # Z02 unindexed code injection.
 with tempfile.TemporaryDirectory() as td:
  t=Path(td)/'pkg';shutil.copytree(ROOT,t);(t/'records/W17/injected.py').write_text("print('x')")
  c=run(t,'verify','--integrity-only');expect('UNINDEXED_SECURITY_FILE',c.returncode==2 and 'UNINDEXED_SECURITY_FILE' in c.stdout,'REJECTED',c.stdout+c.stderr);rejected+=1
 # Z03 W16 rehashed parameter mismatch.
 with tempfile.TemporaryDirectory() as td:
  t=Path(td)/'pkg';shutil.copytree(ROOT,t);p=t/'records/W16/three_parameter_tube_certificate.json';d=json.loads(p.read_text());d['basis']['h_center']['num']=str(int(d['basis']['h_center']['num'])+1);p.write_text(json.dumps(d));refresh(t)
  c=run(t,'verify','--record','RH-W-16');expect('REHASHED_PARAMETER_MISMATCH',c.returncode==1 and '[FAIL]' in c.stdout,'REJECTED',c.stdout+c.stderr);rejected+=1
 # Z04 omitted prime power.
 with tempfile.TemporaryDirectory() as td:
  t=Path(td)/'pkg';shutil.copytree(ROOT,t);p=t/'records/W13/mixed_10x10_nearzero_interval.json';d=json.loads(p.read_text());d['prime_powers'].pop('4');p.write_text(json.dumps(d));refresh(t)
  c=run(t,'verify','--record','RH-W-13');expect('OMITTED_PRIME_POWER',c.returncode==1 and '[FAIL]' in c.stdout,'REJECTED',c.stdout+c.stderr);rejected+=1
 # Z05 event type mislabel.
 with tempfile.TemporaryDirectory() as td:
  t=Path(td)/'pkg';shutil.copytree(ROOT,t);p=t/'records/W17/chamber_subdivision_certificate.json';d=json.loads(p.read_text());d['event']['polynomial_piece_changes']=False;p.write_text(json.dumps(d));refresh(t)
  c=run(t,'verify','--record','RH-W-17');expect('POLYNOMIAL_PIECE_MISLABEL',c.returncode==1 and '[FAIL]' in c.stdout,'REJECTED',c.stdout+c.stderr);rejected+=1
 # Z06 coverage gap.
 with tempfile.TemporaryDirectory() as td:
  t=Path(td)/'pkg';shutil.copytree(ROOT,t);p=t/'records/W17/chamber_subdivision_certificate.json';d=json.loads(p.read_text());d['cells'][1]['interval'][0]['num']=str(int(d['cells'][1]['interval'][0]['num'])+1);p.write_text(json.dumps(d));refresh(t)
  c=run(t,'verify','--record','RH-W-17');expect('COVERAGE_GAP',c.returncode==1 and '[FAIL]' in c.stdout,'REJECTED',c.stdout+c.stderr);rejected+=1
 # Z07 historical M/G parameter identity mismatch.
 with tempfile.TemporaryDirectory() as td:
  t=Path(td)/'pkg';shutil.copytree(ROOT,t);p=t/'records/W13/mixed_10x10_nearzero_interval.json';d=json.loads(p.read_text());d['basis']['spacing']['num']=str(int(d['basis']['spacing']['num'])+1);p.write_text(json.dumps(d));refresh(t)
  c=run(t,'verify','--record','RH-W-13');expect('M_G_PARAMETER_IDENTITY_MISMATCH',c.returncode==1 and '[FAIL]' in c.stdout,'REJECTED',c.stdout+c.stderr);rejected+=1
 # Z08 RH claim escalation.
 with tempfile.TemporaryDirectory() as td:
  t=Path(td)/'pkg';shutil.copytree(ROOT,t);p=t/'rh_certificate_manifest_v0.2.json';d=json.loads(p.read_text());d['claim_firewall']['RH_CLAIM']=True;p.write_text(json.dumps(d));refresh(t)
  c=run(t,'verify','--integrity-only');expect('RH_CLAIM_ESCALATION',c.returncode==3 and 'MANIFEST_REJECTED' in c.stdout,'REJECTED',c.stdout+c.stderr);rejected+=1
 # Z09 dependency cycle W16<->W17.
 with tempfile.TemporaryDirectory() as td:
  t=Path(td)/'pkg';shutil.copytree(ROOT,t);p=t/'rh_certificate_manifest_v0.2.json';d=json.loads(p.read_text());next(r for r in d['records'] if r['id']=='RH-W-16')['dependencies'].append('RH-W-17');p.write_text(json.dumps(d));refresh(t)
  c=run(t,'verify','--integrity-only');expect('DEPENDENCY_CYCLE',c.returncode==3 and 'dependency cycle' in c.stdout,'REJECTED',c.stdout+c.stderr);rejected+=1
 # Z10 path traversal.
 with tempfile.TemporaryDirectory() as td:
  t=Path(td)/'pkg';shutil.copytree(ROOT,t);p=t/'rh_certificate_manifest_v0.2.json';d=json.loads(p.read_text());next(r for r in d['records'] if r['id']=='RH-W-18')['command']=['python','../escape.py'];p.write_text(json.dumps(d));refresh(t)
  c=run(t,'verify','--integrity-only');expect('COMMAND_PATH_TRAVERSAL',c.returncode==3 and 'unsafe command' in c.stdout,'REJECTED',c.stdout+c.stderr);rejected+=1
 # Z11 status inflation of W06.
 with tempfile.TemporaryDirectory() as td:
  t=Path(td)/'pkg';shutil.copytree(ROOT,t);p=t/'rh_certificate_manifest_v0.2.json';d=json.loads(p.read_text());next(r for r in d['records'] if r['id']=='RH-W-06')['status']='VERIFIED';p.write_text(json.dumps(d));refresh(t)
  c=run(t,'verify','--integrity-only');expect('STATUS_INFLATION',c.returncode==3 and 'status inflation' in c.stdout,'REJECTED',c.stdout+c.stderr);rejected+=1
 # Z12-Z16 are exact synthetic cases, verified as a normal record.
 c=run(ROOT,'verify','--record','RH-W-19');expect('SYNTHETIC_ZOO',c.returncode==0 and 'ADVERSARIAL_CERTIFICATE_ZOO_OK' in c.stdout,'5_CLASSES_REJECTED_PLUS_FLOAT_EXACT_AUDIT',c.stdout+c.stderr);rejected+=5
 # Z17: colluding verifier + manifest + hashes. It passes internally by design.
 with tempfile.TemporaryDirectory() as td:
  t=Path(td)/'pkg';shutil.copytree(ROOT,t);fake=t/'records/FAKE';fake.mkdir();(fake/'fake.py').write_text("print('FAKE_CERTIFICATE_OK')\nprint('RH_CLAIM=False')\n")
  p=t/'rh_certificate_manifest_v0.2.json';d=json.loads(p.read_text());d['records'].append({'id':'RH-W-FAKE','kind':'NUMERICAL_MATRIX','status':'VERIFIED','directory':'records/FAKE','command':['python','fake.py'],'expected_token':'FAKE_CERTIFICATE_OK','claim':{'RH_CLAIM':False},'dependencies':[],'notes':['intentional collusion specimen'],'timeout_seconds':10,'input_digest':''});p.write_text(json.dumps(d));refresh(t)
  c=run(t,'verify','--record','RH-W-FAKE');expect('TOKEN_ONLY_COLLUDING_VERIFIER',c.returncode==0 and '[PASS]' in c.stdout,'EXPECTED_SURVIVAL_EXTERNAL_TRUST_REQUIRED',c.stdout+c.stderr);survived+=1
 print('---')
 print(f'expected_rejections_confirmed={rejected}/16')
 print(f'expected_survivals_confirmed={survived}/1')
 print('external_trust_gap=SIGNED_RELEASE_OR_INDEPENDENT_VERIFIER_REQUIRED')
 print('status=ADVERSARIAL_REPRODUCIBILITY_AUDIT_OK')
 print('RH_CLAIM=False')
if __name__=='__main__':main()
