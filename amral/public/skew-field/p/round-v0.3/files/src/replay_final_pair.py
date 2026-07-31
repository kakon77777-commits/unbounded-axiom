from pathlib import Path
import json,math,numpy as np
from scipy.spatial import ConvexHull
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'data/round03_summary.json').read_text())
rho=d['parameters']['rho']
a=np.loadtxt(R/'data/constant_curve.csv',delimiter=',',skiprows=1)[:,1:3]
b=np.loadtxt(R/'data/double_harmonic_reflected_placed.csv',delimiter=',',skiprows=1)
p=np.vstack([a,b]); h=ConvexHull(p); poly=p[h.vertices]; x,y=poly[:,0],poly[:,1]
A=.5*abs(np.dot(x,np.roll(y,-1))-np.dot(y,np.roll(x,-1)))
P=np.sum(np.hypot(np.diff(np.r_[x,x[0]]),np.diff(np.r_[y,y[0]])))
T=A+rho*P+math.pi*rho*rho
print(A,P,T,d['final_pair_container']['convex_thick_area'],T-d['final_pair_container']['convex_thick_area'])
