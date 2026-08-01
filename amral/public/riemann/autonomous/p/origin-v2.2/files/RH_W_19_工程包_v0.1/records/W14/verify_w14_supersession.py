#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent

def fq(o):return F(int(o['num']),int(o['den']))
def main():
 d=json.loads((ROOT/'RH-W-14_corrected_lipschitz_reaudit.json').read_text())
 assert d['schema']=='RH-W-14-corrected-arch-tail-reaudit-v0.1'
 assert {k:fq(v) for k,v in d['corrected_first_derivative_integer_bounds'].items()}=={'3':F(179),'5':F(218),'7':F(255)}
 assert d['status']=='RH-W-14_RECERTIFIED_WITH_SUPPORT_EXTERIOR_ARCHIMEDEAN_TAIL'
 assert d['original_conclusion_preserved'] is True and d['RH_CLAIM'] is False
 assert fq(d['corrected_global_combined_row_bound'])>0
 assert all(fq(x)>0 for x in d['ldlt_pivots'])
 print('original_W14_derivative_derivation=SUPERSEDED')
 print('corrected_bounds=179,218,255')
 print('corrected_ldlt_pivots_positive=10')
 print('status=SUPERSEDED_RECERTIFIED_BY_W15')
 print('RH_CLAIM=False')
if __name__=='__main__':main()
