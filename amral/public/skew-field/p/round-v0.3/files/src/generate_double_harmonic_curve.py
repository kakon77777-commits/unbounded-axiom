from pathlib import Path
import math
import numpy as np
from scipy.integrate import cumulative_trapezoid
a1,b1,a2,b2=(2.8910519514819617,1.2356729211268873,2.084611650923618,-0.5610840858996916)
s=np.linspace(0,1,5001)
g=a1*np.cos(2*math.pi*s)+b1*np.sin(2*math.pi*s)+a2*np.cos(4*math.pi*s)+b2*np.sin(4*math.pi*s)
r=np.exp(g); k=math.pi*r/np.trapezoid(r,s)
th=np.r_[0,cumulative_trapezoid(k,s)]; th*=math.pi/th[-1]
x=np.r_[0,cumulative_trapezoid(np.cos(th),s)]; y=np.r_[0,cumulative_trapezoid(np.sin(th),s)]
rd=x*np.cos(th)+y*np.sin(th)
out=np.c_[s,x,y,k,th,rd]
p=Path(__file__).resolve().parents[1]/'data/double_harmonic_curve_replayed.csv'
np.savetxt(p,out,delimiter=',',header='s,x,y,kappa,theta,radial_dot',comments='')
print(p)
print(k.max(),rd[1:].min())
