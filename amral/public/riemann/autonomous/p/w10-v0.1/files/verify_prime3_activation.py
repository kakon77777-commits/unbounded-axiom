#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import json, math

def frac(x):return F(int(x['num']),int(x['den']))
def iv(x):return frac(x['lower']),frac(x['upper'])

def main():
 p=Path(__file__).with_name('prime3_soft_activation_certificate.json')
 d=json.loads(p.read_text(encoding='utf-8'))
 assert d['schema']=='RH-W-10-prime3-soft-activation-v0.1'
 assert frac(d['basis']['h'])==F(87,400)
 mlo,mhi=iv(d['theta_minus']['mu_d_plus_4h_minus_log3'])
 assert mhi<0 and d['theta_minus']['state']=='INACTIVE'
 plo,phi=iv(d['theta_minus']['prime3_lag1_entry']);assert plo==phi==0
 z=d['theta_zero'];assert z['prime3_lag1_entry']=='0'
 ulo,uhi=iv(d['theta_plus']['mu_d_plus_4h_minus_log3'])
 assert 0<ulo<=uhi<F(87,400)
 qlo,qhi=iv(d['theta_plus']['prime3_lag1_entry'])
 assert qlo<=qhi<0
 glo,ghi=iv(d['theta_plus']['positive_log3_sample_outside_gap']);assert glo>0
 assert d['boundary']['regularity']=='C^6 but not C^7 at mu=0'
 print('schema=OK')
 print('theta_minus=INACTIVE_CERTIFIED')
 print('theta_zero=BOUNDARY_ZERO_SYMBOLIC')
 print('theta_plus=ACTIVE_FIRST_SPLINE_PIECE_CERTIFIED')
 print(f'theta_plus_mu=[{ulo},{uhi}]')
 print(f'theta_plus_prime3_entry=[{qlo},{qhi}]')
 print('regularity=C6_NOT_C7')
 print('RH_CLAIM=False')
if __name__=='__main__':main()
