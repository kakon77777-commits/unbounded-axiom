#!/usr/bin/env python3
from pathlib import Path
import json, hashlib, subprocess, sys, csv
ROOT=Path(__file__).resolve().parent
PC=ROOT/'platform_case_0001'

def fail(msg):
    print('FAIL:',msg); raise SystemExit(1)
def load(name): return json.loads((PC/name).read_text(encoding='utf-8'))

def main():
    man=json.loads((ROOT/'batch01_release_manifest.json').read_text(encoding='utf-8'))
    if man['claim_firewall'].get('RH_CLAIM') is not False: fail('release RH claim firewall')
    case=load('case_manifest.json')
    nodes=load('research_nodes.json')['nodes']
    if len(nodes)!=20: fail('node count')
    expected=[f'RH-W-{i:02d}' for i in range(1,21)]
    if [n['node_id'] for n in nodes]!=expected: fail('node identity/order')
    for n in nodes:
        if n.get('rh_claim') is not False: fail('node RH claim '+n['node_id'])
    for fn in ['dependency_graph.json','timeline.json','certificate_index.json','claim_ledger.json','failure_and_revision_log.json','trust_boundary.json','handoff_batch_02.json','website_copy_zh_tw.json','references.json','artifact_catalog.json','platform_import_manifest.json']:
        d=load(fn)
        if d.get('rh_claim') is not False: fail(fn+' RH claim')
    # Research-relay DAG only; revision edges are metadata and may point backward.
    graph=load('dependency_graph.json')
    adj={x:[] for x in expected}
    for e in graph['edges']:
        if e['type']=='RESEARCH_RELAY': adj[e['from']].append(e['to'])
    seen=set(); active=set()
    def dfs(x):
        if x in active: fail('research relay cycle')
        if x in seen: return
        active.add(x)
        for y in adj[x]: dfs(y)
        active.remove(x); seen.add(x)
    for x in expected: dfs(x)
    claims=load('claim_ledger.json')['claims']
    if not claims or any(c.get('rh_claim') is not False for c in claims): fail('claim ledger')
    arts=load('artifact_catalog.json')['entries']
    internal=[a for a in arts if a['node_id']!='RH-W-20']
    if len(internal)!=19: fail('round package count')
    import zipfile
    for a in internal:
        ap=ROOT/a['file']
        if not ap.is_file(): fail('missing round package '+a['file'])
        if hashlib.sha256(ap.read_bytes()).hexdigest()!=a['sha256']: fail('round package hash '+a['node_id'])
        with zipfile.ZipFile(ap) as z:
            if z.testzip() is not None: fail('corrupt round package '+a['node_id'])
    certs=load('certificate_index.json')['entries']
    if len(certs)!=20: fail('certificate index count')
    sm={c['node_id']:c['status'] for c in certs}
    if sm.get('RH-W-06')!='LEGACY_INCOMPLETE': fail('W06 status inflation')
    if sm.get('RH-W-14')!='SUPERSEDED_RECERTIFIED': fail('W14 supersession loss')
    # Run backend and red team.
    p=subprocess.run([sys.executable,'rhcert.py','verify'],cwd=ROOT/'backend_v0.2',text=True,capture_output=True,timeout=180)
    if p.returncode or 'executed_records_passed=16/16' not in p.stdout or 'RH_CLAIM=False' not in p.stdout:
        print(p.stdout); print(p.stderr); fail('backend replay')
    q=subprocess.run([sys.executable,'redteam_zoo.py'],cwd=ROOT/'backend_v0.2',text=True,capture_output=True,timeout=180)
    if q.returncode or 'expected_rejections_confirmed=16/16' not in q.stdout or 'expected_survivals_confirmed=1/1' not in q.stdout:
        print(q.stdout); print(q.stderr); fail('redteam replay')
    # Release hashes exclude mutable verification outputs and hash file itself.
    sums=(ROOT/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines()
    for line in sums:
        h,rel=line.split('  ',1)
        pth=ROOT/rel
        if not pth.is_file(): fail('missing hashed file '+rel)
        got=hashlib.sha256(pth.read_bytes()).hexdigest()
        if got!=h: fail('hash mismatch '+rel)
    print('schema=RH-BATCH01-RELEASE-MANIFEST-v0.1')
    print('case_id=CASE-0001-RH-WEIL-BATCH01')
    print('research_nodes=20/20')
    print('backend_records=16/16')
    print('adversarial_expected_rejections=16/16')
    print('adversarial_expected_survivals=1/1')
    print('legacy_incomplete=RH-W-06')
    print('superseded_recertified=RH-W-14')
    print('offline_round_packages=19/19')
    print('platform_import_bundle=OK')
    print('status=BATCH01_RELEASE_VERIFIED')
    print('RH_CLAIM=False')
if __name__=='__main__': main()
