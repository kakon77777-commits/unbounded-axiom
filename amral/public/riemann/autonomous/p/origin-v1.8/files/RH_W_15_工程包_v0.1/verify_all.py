#!/usr/bin/env python3
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parent
steps=[['python','verify_cross_regularity.py'],['python','verify_interval_taylor_tube.py']]
if '--with-crosscheck' in sys.argv:steps.append(['python','crosscheck_w15_mpmath.py'])
out=[]
for cmd in steps:
 p=subprocess.run(cmd,cwd=root,text=True,capture_output=True)
 out.append(f'$ {" ".join(cmd)}\n{p.stdout}{p.stderr}')
 if p.returncode:raise SystemExit(''.join(out))
text='\n'.join(out)+'\nALL_CERTIFICATES_OK\nRH_CLAIM=False\n'
(root/'ALL_VERIFY.txt').write_text(text);print(text,end='')
