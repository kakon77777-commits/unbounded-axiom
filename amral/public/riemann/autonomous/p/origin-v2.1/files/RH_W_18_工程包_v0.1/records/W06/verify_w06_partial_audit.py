#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent

def fq(o):return F(int(o['num']),int(o['den']))
def iv(o):return fq(o['lower']),fq(o['upper'])
def main():
 d=json.loads((ROOT/'prime2_5x5_positive_certificate.json').read_text())
 assert d['schema']=='RH-W-06-prime2-5x5-positive-certificate-v0.1'
 assert d['status']=='CERTIFIED_POSITIVE_ON_THIS_5D_SUBSPACE'
 m=d['method'];delta=fq(m['midpoint_shift']);rr=fq(m['max_interval_row_radius']);margin=fq(m['uniform_min_eigenvalue_lower_bound'])
 assert delta-rr==margin and margin>0
 assert all(fq(x)>0 for x in m['exact_ldlt_pivots_of_C_minus_delta_I'])
 w=d['prime_stabilization_witness'];pf=iv(w['prime_free_quadratic']);p2=iv(w['prime2_contribution']);full=iv(w['full_quadratic'])
 assert pf[1]<0 and p2[0]>0 and full[0]>0
 assert d['activation_pattern_by_toeplitz_lag']==[False,False,True,True,True]
 assert not (ROOT/'weil_matrix_prime2_2x2_interval.json').exists()
 print('stored_5x5_internal_arithmetic=OK')
 print('prime_stabilization_sign_pattern=OK')
 print('missing_artifact=weil_matrix_prime2_2x2_interval.json')
 print('status=LEGACY_INCOMPLETE_PARTIAL_AUDIT_ONLY')
 print('RH_CLAIM=False')
if __name__=='__main__':main()
