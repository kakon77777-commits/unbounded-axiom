import numpy as np, math, pandas as pd

m=1.7
omega0=1.3
Omega_obs=0.481
T=2*math.pi/omega0
N=4001
t=np.linspace(0,T,N)
dt=t[1]-t[0]
x0,y0,vx0,vy0=1.2,-0.45,0.35,1.05
c=np.cos(omega0*t); s=np.sin(omega0*t)
x=x0*c+(vx0/omega0)*s
vx=-x0*omega0*s+vx0*c
y=y0*c+(vy0/omega0)*s
vy=-y0*omega0*s+vy0*c
rI=np.column_stack([x,y]); vI=np.column_stack([vx,vy])
J=np.array([[0.,-1.],[1.,0.]])

def R(theta):
    c,s=np.cos(theta),np.sin(theta)
    return np.array([[c,-s],[s,c]])

E=.5*m*np.sum(vI*vI,axis=1)+.5*m*omega0**2*np.sum(rI*rI,axis=1)
L=m*(x*vy-y*vx)

rR=np.zeros_like(rI); vR=np.zeros_like(vI)
for i,ti in enumerate(t):
    Rt=R(-Omega_obs*ti)
    rR[i]=Rt@rI[i]
    vR[i]=Rt@vI[i]-Omega_obs*(J@rR[i])

vI_from_rot=vR+Omega_obs*(rR@J.T)
E_cov=.5*m*np.sum(vI_from_rot*vI_from_rot,axis=1)+.5*m*omega0**2*np.sum(rR*rR,axis=1)
E_naive=.5*m*np.sum(vR*vR,axis=1)+.5*m*omega0**2*np.sum(rR*rR,axis=1)

print("Global energy relative span:",(E.max()-E.min())/abs(E[0]))
print("Rotating naive energy relative span:",(E_naive.max()-E_naive.min())/abs(E[0]))
print("Rotating covariant energy relative span:",(E_cov.max()-E_cov.min())/abs(E[0]))
print("Relative holonomy angle (deg):",math.degrees(((-Omega_obs*T+math.pi)%(2*math.pi))-math.pi))
