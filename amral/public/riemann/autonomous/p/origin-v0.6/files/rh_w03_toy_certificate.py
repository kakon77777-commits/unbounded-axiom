#!/usr/bin/env python3
"""Synthetic interface test only. It uses invented zeros and is not evidence about RH."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh

A=4.0
SIGMA=1.2
CENTERS=np.linspace(-2.4,2.4,5)
TAUS=np.linspace(-3.0,3.0,7)
PARAMS=[(float(c),float(t)) for c in CENTERS for t in TAUS]

def bump(q: float) -> float:
    if abs(q)>=1.0:
        return 0.0
    return math.exp(-1.0/(1.0-q*q))

def transform(param, z: complex) -> complex:
    c,tau=param
    lo=max(-A,c-SIGMA); hi=min(A,c+SIGMA)
    def val(u):
        return bump((u-c)/SIGMA)*np.exp(1j*(tau+z)*u)
    re=quad(lambda u: float(np.real(val(u))),lo,hi,epsabs=1e-10,epsrel=1e-10,limit=150)[0]
    im=quad(lambda u: float(np.imag(val(u))),lo,hi,epsabs=1e-10,epsrel=1e-10,limit=150)[0]
    return re+1j*im

def l2_gram():
    grid=np.linspace(-A,A,5001)
    B=np.zeros((len(grid),len(PARAMS)),dtype=complex)
    for j,(c,tau) in enumerate(PARAMS):
        q=(grid-c)/SIGMA
        b=np.array([bump(float(x)) for x in q])
        B[:,j]=b*np.exp(1j*tau*grid)
    G=np.trapezoid(B[:,:,None]*np.conj(B[:,None,:]),grid,axis=0)
    return (G+G.conj().T)/2

def weil_matrix(gammas):
    F=np.array([[transform(p,z) for p in PARAMS] for z in gammas],dtype=complex)
    M=np.zeros((len(PARAMS),len(PARAMS)),dtype=complex)
    for k,z in enumerate(gammas):
        kb=min(range(len(gammas)),key=lambda j: abs(gammas[j]-np.conj(z)))
        M += np.outer(F[k],np.conj(F[kb]))
    return (M+M.conj().T)/2

def minimum_generalized(M,G):
    vals,U=np.linalg.eigh(G)
    keep=vals>1e-8
    T=U[:,keep]@np.diag(1.0/np.sqrt(vals[keep]))
    R=(T.conj().T@M@T)
    R=(R+R.conj().T)/2
    return float(np.linalg.eigvalsh(R)[0])

def main():
    G=l2_gram()
    real_spectrum=[-3.2,-1.1,1.1,3.2]
    z0=2.0+0.55j
    off_axis=[z0,np.conj(z0),-z0,-np.conj(z0),*real_spectrum]
    lam_real=minimum_generalized(weil_matrix(real_spectrum),G)
    lam_off=minimum_generalized(weil_matrix(off_axis),G)
    print('SYNTHETIC_MODEL_ONLY')
    print(f'real_spectrum_min={lam_real:.12e}')
    print(f'off_axis_min={lam_off:.12e}')
    assert lam_real>-1e-6, 'real synthetic spectrum should be PSD up to quadrature error'
    assert lam_off<-1e-2, 'off-axis synthetic spectrum should expose a negative direction'
    print('TOY_SEPARATION_OK')

if __name__=='__main__':
    main()
