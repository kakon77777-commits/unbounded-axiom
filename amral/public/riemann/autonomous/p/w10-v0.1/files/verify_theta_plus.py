#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import json
GRID=10**32

def frac(o):return F(int(o['num']),int(o['den']))
def interval(o):return frac(o['lower']),frac(o['upper'])
def grid_center(lo,hi):
 m=(lo+hi)/2;q=m.numerator*GRID//m.denominator
 l=F(q,GRID);r=F(q+1,GRID)
 return l if abs(m-l)<=abs(r-m) else r

def ldlt(A):
 n=len(A);L=[[F(0) for _ in range(n)] for _ in range(n)];p=[]
 for i in range(n):
  L[i][i]=F(1);x=A[i][i]-sum(L[i][k]*L[i][k]*p[k] for k in range(i))
  if x<=0:return False,p+[x]
  p.append(x)
  for j in range(i+1,n):
   L[j][i]=(A[j][i]-sum(L[j][k]*L[i][k]*p[k] for k in range(i)))/x
 return True,p

def main():
 d=json.loads(Path(__file__).with_name('theta_plus_15x15_interval.json').read_text(encoding='utf-8'))
 assert d['schema']=='RH-W-10-theta-plus-certificate-v0.1'
 assert d['status']=='CERTIFIED_POSITIVE_GENERALIZED_MARGIN'
 assert d['rigor_contract']['floating_point_in_proof_path'] is False
 assert frac(d['basis']['h'])==F(87,400)
 assert frac(d['basis']['spacing'])==F(117,512)+F(1,5000)
 gaplo,gaphi=interval(d['activation_boundary']['positive_gap_boundary_minus_log3'])
 assert gaplo>0 and d['activation_boundary']['n3_at_negative_sample_is_active'] is True
 M=[[interval(x) for x in row] for row in d['matrix']]
 G=[[frac(x) for x in row] for row in d['gram']];n=len(M);assert n==15
 C=[[grid_center(*M[i][j]) for j in range(n)] for i in range(n)]
 rr=max(sum(max(abs(C[i][j]-M[i][j][0]),abs(M[i][j][1]-C[i][j])) for j in range(n)) for i in range(n))
 cert=d['certificate'];assert rr==frac(cert['row_radius']);delta=frac(cert['delta']);assert delta==F(1,10**9)
 A=[[C[i][j]-delta*G[i][j]-(rr if i==j else F(0)) for j in range(n)] for i in range(n)]
 ok,p=ldlt(A);assert ok and p==[frac(x) for x in cert['pivots']]
 print('schema=OK');print('dimension=15');print('lag1_prime3=ACTIVE_CERTIFIED')
 print(f'boundary_inside_gap={gaplo}')
 print(f'row_radius={rr}');print(f'generalized_margin_delta={delta}')
 print(f'ldlt_pivots_positive={len(p)}');print('status=CERTIFIED_POSITIVE_GENERALIZED_MARGIN');print('RH_CLAIM=False')
if __name__=='__main__':main()
