#!/usr/bin/env python3
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parent
steps=[('exact','verify_chamber_subdivision.py')]
lines=[]
for name,script in steps:
 p=subprocess.run([sys.executable,str(root/script)],cwd=root,text=True,capture_output=True)
 lines.append(f'[{name}] returncode={p.returncode}\n{p.stdout}{p.stderr}')
 if p.returncode:raise SystemExit(p.returncode)
lines.append('status=ALL_EXACT_CHECKS_OK\nCROSSCHECK_OPTIONAL=python crosscheck_w17_mpmath.py\nRH_CLAIM=False')
text='\n'.join(lines)+'\n';(root/'ALL_VERIFY.txt').write_text(text);print(text,end='')
