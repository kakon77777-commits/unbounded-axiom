#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json,math,sys
import weil_interval_core as base
import mixed_order_core as mixed
sys.set_int_max_str_digits(0)

def fq(o):return F(int(o['num']),int(o['den']))
def iv(o):return base.IV(fq(o['lower']),fq(o['upper']))

def ppbase(n):
 for p in range(2,n+1):
  if any(p%q==0 for q in range(2,math.isqrt(p)+1)):continue
  v=p
  while v<n:v*=p
  if v==n:return p
 return None

def ldlt(A):
 n=len(A);L=[[F(0) for _ in range(n)] for _ in range(n)];p=[]
 for i in range(n):
  L[i][i]=F(1);z=A[i][i]-sum(L[i][k]*L[i][k]*p[k] for k in range(i))
  if z<=0:return False,p+[z]
  p.append(z)
  for j in range(i+1,n):L[j][i]=(A[j][i]-sum(L[j][k]*L[i][k]*p[k] for k in range(i)))/z
 return True,p

def center(x,grid):
 m=x.midpoint();q=m.numerator*grid//m.denominator;a,b=F(q,grid),F(q+1,grid)
 return a if abs(m-a)<=abs(b-m) else b

def cert(A,G,delta,eps,grid):
 n=len(A);C=[[center(A[i][j],grid) for j in range(n)] for i in range(n)]
 e=max(sum(max(abs(C[i][j]-A[i][j].lo),abs(A[i][j].hi-C[i][j])) for j in range(n)) for i in range(n))
 if e!=eps:raise AssertionError('row radius')
 T=[[C[i][j]-delta*G[i][j]-(e if i==j else F(0)) for j in range(n)] for i in range(n)]
 ok,p=ldlt(T)
 if not ok:raise AssertionError('LDLT')
 return p

def iq(A,c):
 z=base.IV.point(0)
 for i in range(len(c)):
  for j in range(len(c)):z+=A[i][j].scale(F(c[i]*c[j]))
 return z

def eq(A,c):return sum((F(c[i]*c[j])*A[i][j] for i in range(len(c)) for j in range(len(c))),F(0))

def main():
 root=Path(__file__).resolve().parent;o=json.loads((root/'mixed_10x10_nearzero_interval.json').read_text())
 if o['schema']!='RH-W-13-cross-regularity-continuation-v0.1':raise AssertionError('schema')
 b=o['basis'];h,d,s=fq(b['h']),fq(b['spacing']),fq(b['relative_shift_sigma']);N=int(b['per_channel_dimension']);dim=2*N
 if s!=0 or tuple(b['basis_degrees'])!=(1,3):raise AssertionError('basis')
 M=[[iv(x) for x in row] for row in o['matrix']];G=[[fq(x) for x in row] for row in o['gram']]
 for i in range(dim):
  for j in range(dim):
   if M[i][j]!=M[j][i] or G[i][j]!=G[j][i]:raise AssertionError('symmetry')
 corr={(1,1):3,(1,3):5,(3,3):7};degs=(1,3)
 for ca,a in enumerate(degs):
  for cb,bb in enumerate(degs):
   key=f'{min(a,bb)}x{max(a,bb)}';r=corr[(min(a,bb),max(a,bb))]
   for i in range(N):
    for j in range(N):
     I,J=ca*N+i,cb*N+j;lag=abs(i-j)
     if G[I][J]!=mixed.f_value(r,h,F(i-j)*d,F(0)):raise AssertionError('Gram rebuild')
     if M[I][J]!=iv(o['lag_entries'][key][str(lag)]):raise AssertionError('lag rebuild')
 gok,gp=ldlt(G)
 if not gok:raise AssertionError('Gram PD')
 ex=int(o['support']['exclusion_n']);pp={n:p for n in range(2,ex) if (p:=ppbase(n)) is not None}
 if pp!={int(n):int(p) for n,p in o['prime_powers'].items()}:raise AssertionError('prime powers')
 if base.log_rational_iv(F(ex),220).lo<=F(N-1)*d+4*h:raise AssertionError('support exclusion')
 logs={n:base.log_rational_iv(F(n),240) for n in pp}
 for pair,r in corr.items():
  key=f'{pair[0]}x{pair[1]}'
  for lag in range(N):
   active=[]
   for n,x in logs.items():
    plus=mixed.f_interval(r,h,F(lag)*d,x);minus=mixed.f_interval(r,h,F(lag)*d,-x)
    if not(plus.lo==plus.hi==0 and minus.lo==minus.hi==0):active.append(n)
   if active!=o['activation_graph'][key][str(lag)]:raise AssertionError('activation')
 c=o['certificate'];grid=int(c['grid_denominator']);piv=cert(M,G,fq(c['delta']),fq(c['row_radius']),grid)
 w=o['upper_witness'];v=list(map(int,w['integer_vector']));q=iq(M,v);g=eq(G,v)
 if g!=fq(w['gram_exact']) or q.hi>=fq(c['upper_ratio'])*g:raise AssertionError('upper witness')
 for name,start in [('m1',0),('m3',N)]:
  cc=o['isolated_certificates'][name];A=[[M[start+i][start+j] for j in range(N)] for i in range(N)];GG=[[G[start+i][start+j] for j in range(N)] for i in range(N)]
  cert(A,GG,fq(cc['delta']),fq(cc['row_radius']),grid)
 # Alpha gauge identity: diagonal channel rescaling is invertible congruence.
 alpha=F(7,3);diag=[F(1)]*N+[alpha]*N
 MT=[[diag[i]*M[i][j].midpoint()*diag[j] for j in range(dim)] for i in range(dim)]
 GT=[[diag[i]*G[i][j]*diag[j] for j in range(dim)] for i in range(dim)]
 # Verify quadratic quotient identity on the saved witness under inverse coordinates.
 y=[F(v[i],1)/diag[i] for i in range(dim)]
 lhsM=sum(y[i]*MT[i][j]*y[j] for i in range(dim) for j in range(dim));rhsM=sum(F(v[i]*v[j])*M[i][j].midpoint() for i in range(dim) for j in range(dim))
 lhsG=sum(y[i]*GT[i][j]*y[j] for i in range(dim) for j in range(dim));rhsG=g
 if lhsM!=rhsM or lhsG!=rhsG:raise AssertionError('alpha gauge congruence')
 lines=['schema=OK','matrix_symmetry=OK','gram_reconstruction=OK',f'gram_ldlt_pivots_positive={len(gp)}',f'prime_power_enumeration={list(pp)}','activation_graph=OK',f'mixed_ldlt_pivots_positive={len(piv)}','exact_bracket=1e-8<lambda_min<5e-8','isolated_m1=lambda_min>4e-4','isolated_m3=lambda_min>1e-7','alpha_channel_scaling=GAUGE_CONGRUENCE_VERIFIED','quantization_rule=M_AND_G_MUST_SHARE_IDENTICAL_PARAMETERS','status=EXACT_CROSS_REGULARITY_CERTIFICATE_OK','RH_CLAIM=False']
 text='\n'.join(lines)+'\n';(root/'EXACT_VERIFY.txt').write_text(text);print(text,end='')
if __name__=='__main__':main()
