#!/usr/bin/env python3
from pathlib import Path
import hashlib, difflib, json, re, sys
ROOT = Path(__file__).resolve().parents[1]

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def fail(msg):
    print('FAIL:', msg); sys.exit(1)

def display_blocks(text):
    return re.findall(r'\$\$(.*?)\$\$', text, flags=re.S)

def strip_display(text):
    return re.sub(r'\$\$.*?\$\$', '', text, flags=re.S)

def inline_spans(text):
    return re.findall(r'(?<!\$)\$(?!\$)([^\n$]+?)(?<!\$)\$(?!\$)', strip_display(text))

def norm_math(s):
    return ' '.join(s.split())

def artifact_math(path: Path, rel: str):
    text = path.read_text(encoding='utf-8')
    db = display_blocks(text); ins = inline_spans(text)
    return {
      'path': rel,
      'sha256': sha256(path),
      'display_math_blocks': len(db),
      'inline_math_spans': len(ins),
      'display_blocks': [
        {'index':i+1,
         'raw_sha256':hashlib.sha256(b.encode('utf-8')).hexdigest(),
         'normalized_whitespace_sha256':hashlib.sha256(norm_math(b).encode('utf-8')).hexdigest()}
        for i,b in enumerate(db)
      ]
    }, db

# 1) Checksums.
for raw_line in (ROOT/'CHECKSUMS.sha256').read_text(encoding='utf-8').splitlines():
    if not raw_line.strip(): continue
    expected, rel = raw_line.split('  ',1); p=ROOT/rel
    if not p.is_file(): fail(f'missing file: {rel}')
    actual=sha256(p)
    if actual != expected: fail(f'checksum mismatch: {rel}: {actual} != {expected}')

# 2) Normalization evidence.
nm=json.loads((ROOT/'provenance/normalization_manifest.json').read_text(encoding='utf-8'))
up=ROOT/nm['upstream_artifact']; rd=ROOT/nm['readable_artifact']; dp=ROOT/nm['evidence_artifact']
if sha256(up)!=nm['upstream_sha256']: fail('upstream normalization hash mismatch')
if sha256(rd)!=nm['readable_sha256']: fail('readable normalization hash mismatch')
if sha256(dp)!=nm['diff_sha256']: fail('stored normalization.diff hash mismatch')
a=up.read_text(encoding='utf-8'); b=rd.read_text(encoding='utf-8')
regen=''.join(difflib.unified_diff(a.splitlines(keepends=True),b.splitlines(keepends=True),
                                  fromfile='provenance/sssp_export_raw.md',tofile='paper.md',lineterm='\n'))
if regen != dp.read_text(encoding='utf-8'): fail('normalization.diff is not mechanically reproducible')

# 3) Rebuild math inventory.
upinfo, upblocks = artifact_math(up,'provenance/sssp_export_raw.md')
rdinfo, rdblocks = artifact_math(rd,'paper.md')
mi_regen={
  'schema':'EveMissLab-Math-Inventory/1.0',
  'method':{
    'display_extraction':'non-greedy $$...$$ over UTF-8 text',
    'inline_extraction':'single-line $...$ after display blocks are removed',
    'display_correspondence_normalization':'trim and collapse all whitespace runs to one ASCII space',
    'renderer_semantics_claimed':False
  },
  'artifacts':{'upstream':upinfo,'readable':rdinfo},
  'display_math_correspondence':{
    'ordered_normalized_blocks_equal':[norm_math(x) for x in upblocks]==[norm_math(x) for x in rdblocks],
    'upstream_count':len(upblocks),'readable_count':len(rdblocks)
  }
}
mi_stored=json.loads((ROOT/'provenance/math_inventory.json').read_text(encoding='utf-8'))
if mi_regen != mi_stored: fail('math_inventory.json is not mechanically reproducible')

# 4) Cross-check validation namespaces against mechanically counted artifacts.
v=json.loads((ROOT/'validation.json').read_text(encoding='utf-8'))
if v['artifact_validation']['display_math_blocks_detected'] != rdinfo['display_math_blocks']:
    fail('artifact display-math count disagrees with paper.md')
if v['artifact_validation']['inline_math_spans_detected'] != rdinfo['inline_math_spans']:
    fail('artifact inline-math count disagrees with paper.md')
if v['canonical_validation']['math_blocks_render_checked'] != upinfo['display_math_blocks']:
    fail('canonical math render-check count disagrees with upstream SSSP display blocks')
if not mi_regen['display_math_correspondence']['ordered_normalized_blocks_equal']:
    fail('readable display math does not correspond to upstream display math in order')
if rd.read_text(encoding='utf-8').count('$$') % 2 != 0:
    fail('unbalanced display-math delimiters in paper.md')

print('PASS: checksums verified')
print('PASS: normalization.diff reproduced byte-for-byte')
print('PASS: math_inventory.json reproduced exactly')
print(f"PASS: canonical math blocks checked = {v['canonical_validation']['math_blocks_render_checked']}")
print(f"PASS: paper.md display math blocks = {rdinfo['display_math_blocks']}")
print(f"PASS: paper.md inline math spans = {rdinfo['inline_math_spans']}")
print('PASS: display math corresponds to upstream canonical export in order')
