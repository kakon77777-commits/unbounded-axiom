#!/usr/bin/env python3
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parent
checks=[('exact',[sys.executable,str(root/'verify_three_parameter_tube.py')])]
lines=[]
for name,cmd in checks:
 p=subprocess.run(cmd,cwd=root,text=True,capture_output=True)
 lines.append(f'[{name}] returncode={p.returncode}\n{p.stdout}{p.stderr}')
 if p.returncode:raise SystemExit('\n'.join(lines))
text='\n'.join(lines)+'\nALL_CERTIFICATES_OK\n';(root/'ALL_VERIFY.txt').write_text(text);print(text,end='')
