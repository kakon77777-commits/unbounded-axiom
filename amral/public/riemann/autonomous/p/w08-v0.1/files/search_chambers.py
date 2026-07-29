import math, time, json
import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh
from scipy.special import comb
from functools import lru_cache

DEG=7; FACT=math.factorial(7)

def beta7(z):
    if z <= -4 or z >= 4: return 0.0
    s=0.0
    for k in range(9):
        y=z+4-k
        if y>0: s += ((-1)**k)*comb(8,k,exact=True)*y**7/FACT
    return s

def vm(n):
    for p in range(2,n+1):
        if any(p%d==0 for d in range(2,int(math.sqrt(p))+1)): continue
        q=p
        while q<n: q*=p
        if q==n: return math.log(p)
    return 0.0
VM={n:vm(n) for n in range(2,101)}

def entry(center,h):
    def f(x): return beta7((x-center)/h)
    L=center-4*h; R=center+4*h; r=max(abs(L),abs(R))
    knots=[center+h*k for k in range(-4,5)]
    endpoint=0.0
    for a,b in zip(knots[:-1],knots[1:]):
        endpoint+=quad(lambda x:f(x)*(math.exp(x/2)+math.exp(-x/2)),a,b,epsabs=2e-10,epsrel=2e-10,limit=100)[0]
    f0=f(0.0); F0=2*f0
    const=-(math.log(4*math.pi)+0.5772156649015329)*f0
    def F(x): return f(x)+f(-x)
    def integrand(x):
        den=-math.expm1(-2*x)
        if x==0: return F0/4 # adequate for quad endpoint; F even
        return (F(x)*math.exp(-x/2)-F0*math.exp(-x))/den
    pts=sorted(set([0.0,r]+[q for q in knots if 0<q<r]+[-q for q in knots if 0<-q<r]))
    integ=0.0
    for a,b in zip(pts[:-1],pts[1:]):
        integ+=quad(integrand,a,b,epsabs=2e-10,epsrel=2e-10,limit=100)[0]
    arch=-(integ-F0*math.atanh(math.exp(-r)))
    prime=0.0
    nmax=min(100,int(math.exp(r))+1)
    for n in range(2,nmax+1):
        lam=VM.get(n,0.0)
        if lam:
            x=math.log(n)
            prime-=lam/math.sqrt(n)*(f(x)+f(-x))
    return endpoint+const+arch+prime

def chamber(h,d,N):
    lags=[entry(-k*d,h) for k in range(N)]
    M=np.array([[lags[abs(i-j)] for j in range(N)] for i in range(N)])
    glags=[beta7((k*d)/h) for k in range(N)]
    G=np.array([[glags[abs(i-j)] for j in range(N)] for i in range(N)])
    ge=np.linalg.eigvalsh(G)
    if ge[0]<1e-8: return None
    ev=eigh(M,G,eigvals_only=True)
    return float(ev[0]),float(ev[-1]),float(ge[0]),lags

hs=[0.06,0.08,0.10,0.12,0.15]
ratios=[1.5,2.0,2.5,3.0,3.5,4.0]
Ns=[5,7,9,11,13]
rows=[]; t=time.time()
for h in hs:
  for ratio in ratios:
    d=h*ratio
    for N in Ns:
      maxr=(N-1)*d+4*h
      if maxr>3.8: continue
      try:
        r=chamber(h,d,N)
      except Exception as e:
        print('ERR',h,d,N,e); continue
      if r:
        mn,mx,gmin,lags=r
        rows.append({'h':h,'d':d,'ratio':ratio,'N':N,'max_radius':maxr,'lambda_min':mn,'lambda_max':mx,'gram_min':gmin})
        print(len(rows),h,ratio,N,mn)
rows.sort(key=lambda x:x['lambda_min'])
print('TIME',time.time()-t,'count',len(rows))
print('TOP')
for x in rows[:20]:print(x)

from pathlib import Path
out_path=Path(__file__).with_name('chamber_search_results_recomputed.json')
json.dump(rows,open(out_path,'w',encoding='utf-8'),indent=2)
print('OUTPUT',out_path)
