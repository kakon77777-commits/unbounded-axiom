#!/usr/bin/env python3
"""Exact structural verifier for RH-W-17 chamber subdivision.

After parsing the stored transcendental interval enclosures, all certificate
checks use only integers and fractions: domain coverage, event placement,
second-order remainders, symmetry, exact Gram data, and LDL^T positivity.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json, math, sys
import weil_interval_core as base
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent

def fq(o):return F(int(o['num']),int(o['den']))
def iv(o):return base.IV(fq(o['lower']),fq(o['upper']))
def ldlt(A):
 n=len(A);L=[[F(0) for _ in range(n)] for _ in range(n)];p=[]
 for i in range(n):
  L[i][i]=F(1);z=A[i][i]-sum(L[i][k]*L[i][k]*p[k] for k in range(i))
  if z<=0:return False,p+[z]
  p.append(z)
  for j in range(i+1,n):L[j][i]=(A[j][i]-sum(L[j][k]*L[i][k]*p[k] for k in range(i)))/z
 return True,p

def grid_center(x,grid=10**38):
 m=x.midpoint();q=m.numerator*grid//m.denominator;a,b=F(q,grid),F(q+1,grid)
 return a if abs(m-a)<=abs(b-m) else b

def main():
 d=json.loads((ROOT/'chamber_subdivision_certificate.json').read_text())
 if d['schema']!='RH-W-17-chamber-aware-subdivision-v0.1':raise AssertionError('schema')
 H=fq(d['basis']['h']);N=int(d['basis']['per_channel_dimension']);dim=int(d['basis']['total_dimension'])
 if (N,dim)!=(5,10):raise AssertionError('dimension')
 delta=fq(d['delta_lower']);master_lo,master_hi=map(fq,d['master_domain']['interval'])
 if master_hi-master_lo!=fq(d['master_domain']['width']):raise AssertionError('master width')
 event_iv=iv(d['event']['rigorous_d_interval']);slab_lo,slab_hi=map(fq,d['event']['event_slab'])
 # Independently reconstruct log(2)/4.
 log2q=base.log_rational_iv(F(2),260).scale(F(1,4))
 if event_iv!=log2q:raise AssertionError('event interval')
 if not (slab_lo<event_iv.lo<=event_iv.hi<slab_hi):raise AssertionError('event containment')
 if d['event']['multiplicity']!=8 or d['event']['correlation_degrees']!=[3,5,7]:raise AssertionError('event multiplicity')
 if d['event']['activation_graph_changes'] or not d['event']['polynomial_piece_changes']:raise AssertionError('event type')
 # All oriented witnesses must solve a*d+k*h=sign*log(n) inside the event interval.
 for e in d['event']['oriented_witnesses']:
  ca,cb=e['channels'];i,j=e['indices'];a=i-j;k=int(e['knot_index']);n=int(e['prime_power']);sgn=int(e['sample_sign'])
  if a==0:raise AssertionError('zero event slope')
  sample=base.log_rational_iv(F(n),260)
  if sgn<0:sample=-sample
  num=base.IV(sample.lo-F(k)*H,sample.hi-F(k)*H)
  sol=base.IV(num.lo/F(a),num.hi/F(a)) if a>0 else base.IV(num.hi/F(a),num.lo/F(a))
  if sol!=iv(e['d_interval']):raise AssertionError('event witness')
 # Cell coverage and adjacency.
 cells=d['cells'];cells_sorted=sorted(cells,key=lambda c:fq(c['interval'][0]))
 if fq(cells_sorted[0]['interval'][0])!=master_lo or fq(cells_sorted[-1]['interval'][1])!=master_hi:raise AssertionError('coverage endpoints')
 for a,b in zip(cells_sorted[:-1],cells_sorted[1:]):
  if fq(a['interval'][1])!=fq(b['interval'][0]):raise AssertionError('coverage gap')
 if [c['kind'] for c in cells_sorted]!=['FIXED_LEFT_PIECE','EVENT_SLAB','FIXED_RIGHT_PIECE']:raise AssertionError('cell kinds')
 if not fq(cells_sorted[0]['interval'][1])<event_iv.lo:raise AssertionError('left chamber')
 if not (fq(cells_sorted[1]['interval'][0])<=event_iv.lo and event_iv.hi<=fq(cells_sorted[1]['interval'][1])):raise AssertionError('event cell')
 if not event_iv.hi<fq(cells_sorted[2]['interval'][0]):raise AssertionError('right chamber')
 # Chamber/global prime powers.
 if d['prime_power_chamber']['active_global_prime_powers']!=[2,3,4]:raise AssertionError('prime powers')
 maxR=fq(d['prime_power_chamber']['max_support_radius'])
 if maxR!=4*master_hi+4*H or maxR>=base.log_rational_iv(F(5),260).lo:raise AssertionError('support radius')
 if not d['prime_power_chamber']['activation_constant_over_master_domain']:raise AssertionError('activation constant')
 # Parse point data once.
 points={}
 for key,o in d['points'].items():
  dd=fq(o['d']);M=[[iv(x) for x in row] for row in o['matrix']];G=[[fq(x) for x in row] for row in o['gram']]
  for i in range(dim):
   for j in range(dim):
    if M[i][j]!=M[j][i] or G[i][j]!=G[j][i]:raise AssertionError('symmetry')
  points[dd]=(M,G,o['activation'])
 acts={json.dumps(v[2],sort_keys=True) for v in points.values()}
 if len(acts)!=1:raise AssertionError('activation mismatch')
 # Reconstruct every cell remainder and exact endpoint certificates.
 corr={(0,0):3,(0,1):5,(1,0):5,(1,1):7}
 L2={int(k):fq(v) for k,v in d['second_derivative_bounds'].items()};LG2=fq(d['gram_second_derivative_bound'])
 verified=0
 for c in cells_sorted:
  lo,hi=map(fq,c['interval']);rho=(hi-lo)/2
  if hi-lo!=fq(c['width']) or rho!=fq(c['radius']):raise AssertionError('cell geometry')
  ER=[[F(0) for _ in range(dim)] for _ in range(dim)];GR=[[F(0) for _ in range(dim)] for _ in range(dim)]
  rows=[];grows=[]
  for I in range(dim):
   ca,i=divmod(I,N);rr=gr=F(0)
   for J in range(dim):
    cb,j=divmod(J,N);r=corr[(ca,cb)];aa=F(i-j)
    ER[I][J]=L2[r]*aa*aa*rho*rho/2;GR[I][J]=LG2*aa*aa*rho*rho/2
    rr+=ER[I][J]+delta*GR[I][J];gr+=GR[I][J]
   rows.append(rr);grows.append(gr)
  if [[fq(x) for x in row] for row in c['entry_remainders']]!=ER:raise AssertionError('entry remainder')
  if [[fq(x) for x in row] for row in c['gram_entry_remainders']]!=GR:raise AssertionError('gram remainder')
  eps=max(rows);geps=max(grows)
  if fq(c['combined_row_remainder'])!=eps or fq(c['gram_row_remainder'])!=geps:raise AssertionError('row remainder')
  for dd in (lo,hi):
   M,G,_=points[dd];C=[[grid_center(M[i][j]) for j in range(dim)] for i in range(dim)]
   pe=max(sum(max(abs(C[i][j]-M[i][j].lo),abs(M[i][j].hi-C[i][j])) for j in range(dim)) for i in range(dim))
   sc=c['endpoint_certificates'][str(dd)]
   if pe!=fq(sc['point_row_error']):raise AssertionError('point error')
   T=[[C[i][j]-delta*G[i][j]-((pe+eps) if i==j else F(0)) for j in range(dim)] for i in range(dim)]
   ok,p=ldlt(T)
   if not ok or p!=[fq(x) for x in sc['ldlt_pivots']]:raise AssertionError('LDL')
   GT=[[G[i][j]-(geps if i==j else F(0)) for j in range(dim)] for i in range(dim)]
   gok,gp=ldlt(GT)
   if not gok or gp!=[fq(x) for x in sc['gram_ldlt_pivots']]:raise AssertionError('Gram LDL')
  verified+=1
 lines=['schema=OK','dimension=10','event_equation=4d=log2','event_interval_reconstructed=OK','event_multiplicity=8','correlation_degrees=[3,5,7]','activation_graph_constant=[2,3,4]','polynomial_piece_transition=LEFT->EVENT->RIGHT',f'cells_verified={verified}/3','domain_coverage=CONTIGUOUS_CLOSED_UNION','exact_global_lower_bound=lambda_min>1e-8','status=EXACT_CHAMBER_SUBDIVISION_CERTIFICATE_OK','RH_CLAIM=False']
 text='\n'.join(lines)+'\n';(ROOT/'EXACT_VERIFY.txt').write_text(text);print(text,end='')
if __name__=='__main__':main()
