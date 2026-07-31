"""Moser Skew Lab v0.11 core verifier.

This script reproduces the two strongest scalar enclosures:

1. the 270-degree smooth-candidate scale;
2. the difference s120 - s270.

It uses a composite midpoint rule plus an analytic global second-derivative
bound. The implementation adds an explicit floating-point padding, but it is
not a directed-rounding formal proof.
"""
import math
import numpy as np

EPS=0.037
W=0.3361057714712081
BETA=1.405382794839393
DELTA=0.05204734906280986
CENTER=0.5801781668857768
L0=1-2*W
N=262144

SQRT3=math.sqrt(3.0)
A=((3+4*SQRT3)/18)/1.0048
B=((4+SQRT3)/6)/1.0048

def raw(u):
    return 0.5*(1-np.tanh((u-CENTER)/EPS))

r0=float(raw(0.0))
r1=float(raw(1.0))

def theta(u):
    return BETA+DELTA*(raw(u)-r1)/(r0-r1)

C=DELTA*0.5/EPS/(r0-r1)
M_THETA_1=C
M_THETA_2=2*C/EPS*2/(3*SQRT3)
M_COORD_2=M_THETA_1**2+M_THETA_2

h=1/N
u=(np.arange(N)+0.5)*h
th=theta(u)
Icos=float(np.sum(np.cos(th),dtype=np.longdouble)*np.longdouble(h))
Isin=float(np.sum(np.sin(th),dtype=np.longdouble)*np.longdouble(h))

E_xy=M_COORD_2/(24*N*N)+2e-15
s270=W*Isin/A+(W*Icos+L0)/B
s270_err=W*E_xy*(1/A+1/B)+2e-14

qa=2/SQRT3-1
qb=1/SQRT3
q=qa*np.sin(th)-qb*np.cos(th)
Iq=float(np.sum(q,dtype=np.longdouble)*np.longdouble(h))
M_q=math.hypot(qa,qb)
E_q=M_q*(M_THETA_1**2+M_THETA_2)/(24*N*N)+2e-15
difference=L0*(1/(2*A)-1/B)+(W/A)*Iq
difference_err=(W/A)*E_q+2e-14

print("s270 interval =", (s270-s270_err,s270+s270_err))
print("s120-s270 interval =", (difference-difference_err,difference+difference_err))
