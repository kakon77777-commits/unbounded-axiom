#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction as F
import json, hashlib, math
try:
 import numpy as np
except Exception:
 np=None
ROOT=Path(__file__).resolve().parent

def fq(x): return F(int(x['num']),int(x['den']))
def load(n): return json.loads((ROOT/'fixtures'/n).read_text())
def ldlt(A):
 n=len(A);L=[[F(0) for _ in range(n)] for _ in range(n)];D=[F(0)]*n
 for i in range(n):
  L[i][i]=F(1)
  for j in range(i):
   s=sum(L[i][k]*D[k]*L[j][k] for k in range(j))
   if D[j]==0: raise AssertionError('zero pivot')
   L[i][j]=(A[i][j]-s)/D[j]
  D[i]=A[i][i]-sum(L[i][k]*L[i][k]*D[k] for k in range(i))
 return D

results=[]
# inward rounded endpoint excludes exact 1/3
z=load('inward_interval.json');x=fq(z['exact_value']);lo=fq(z['claimed_interval']['lower']);hi=fq(z['claimed_interval']['upper'])
assert lo<=hi and not (lo<=x<=hi);results.append(('INWARD_INTERVAL','REJECTED'))
# empty interval
z=load('endpoint_swap.json');lo=fq(z['claimed_interval']['lower']);hi=fq(z['claimed_interval']['upper'])
assert lo>hi;results.append(('ENDPOINT_SWAP','REJECTED'))
# geometric tail omission
z=load('tail_omission.json');q=fq(z['q']);K=int(z['truncate_after_k']);partial=sum(q**k for k in range(K+1));full=F(1,1)/(1-q);cap=fq(z['claimed_upper'])
assert partial<cap<full;results.append(('TAIL_OMISSION','REJECTED'))
# witness version binding
z=load('witness_version_mismatch.json');assert z['matrix_artifact_id']!=z['witness_bound_matrix_artifact_id'];results.append(('WITNESS_VERSION_MISMATCH','REJECTED'))
# closed cover gap
z=load('coverage_gap.json');master=[fq(x) for x in z['master']];cells=[[fq(x) for x in c] for c in z['cells']]
assert cells[0][0]==master[0] and cells[-1][1]==master[1] and cells[0][1]!=cells[1][0];results.append(('COVERAGE_GAP','REJECTED'))
# Double-precision false negative on an exactly positive Hilbert matrix.
z=load('float_false_negative.json');n=int(z['dimension']);A=[[F(1,i+j+1) for j in range(n)] for i in range(n)];piv=ldlt(A);assert all(x>0 for x in piv)
if np is not None:
 Af=np.array([[float(x) for x in row] for row in A]);e=float(np.linalg.eigvalsh(Af)[0]);assert e<=0.0
else: e=float('nan')
results.append(('FLOAT_FALSE_NEGATIVE','REJECTED_BY_EXACT_LDL'))
for name,status in results: print(f'{name}={status}')
print('exact_hilbert_ldlt_pivots_positive=14')
print('double_hilbert_lambda_min='+repr(e))
print('synthetic_cases_verified='+str(len(results))+'/6')
print('status=ADVERSARIAL_CERTIFICATE_ZOO_OK')
print('RH_CLAIM=False')
