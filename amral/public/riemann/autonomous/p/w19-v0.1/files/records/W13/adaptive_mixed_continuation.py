import math, time
import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh
from scipy.optimize import differential_evolution, minimize
N=5

def beta(deg,z):
    half=(deg+1)/2;s=0.0
    for k in range(deg+2):
        y=z+half-k
        if y>0:s += (-1)**k*math.comb(deg+1,k)*y**deg
    return s/math.factorial(deg)

def pp_base(n):
    for p in range(2,n+1):
        if any(p%q==0 for q in range(2,math.isqrt(p)+1)):continue
        v=p
        while v<n:v*=p
        if v==n:return p
    return None

def entry(deg,h,center):
    radius=(deg+1)/2*h; left,right=center-radius,center+radius
    f=lambda x:beta(deg,(x-center)/h)
    f0=f(0.0);pts=[left+k*h for k in range(deg+2)]
    endpoint=sum(quad(lambda x:f(x)*(math.exp(x/2)+math.exp(-x/2)),a,b,epsabs=2e-12,epsrel=2e-12,limit=100)[0] for a,b in zip(pts[:-1],pts[1:]))
    const=-(math.log(4*math.pi)+0.5772156649015328606)*f0
    R=max(abs(left),abs(right));split={0.0,R}
    for q in pts:
        if 0<q<R:split.add(q)
        if 0<-q<R:split.add(-q)
    sp=sorted(split)
    def integrand(x):
        if x<1e-7:return f0/2
        den=2*math.sinh(x);ss=f(x)+f(-x)
        return (ss*math.expm1(x/2)+(ss-2*f0))/den
    local=sum(quad(integrand,a,b,epsabs=2e-12,epsrel=2e-12,limit=100)[0] for a,b in zip(sp[:-1],sp[1:]))
    arch=-local+2*f0*np.arctanh(math.exp(-R))
    prime=0.0
    for n in range(2,max(2,math.ceil(math.exp(R))+1)):
        p=pp_base(n)
        if p is None:continue
        x=math.log(n);prime-=math.log(p)/math.sqrt(n)*(f(x)+f(-x))
    return endpoint+const+arch+prime

def matrices(params):
    # coherent quantization for reproducible exploration
    h,d,s=[round(float(x),9) for x in params]
    shifts=np.array([(j-2)*d for j in range(N)])
    ts=[shifts-s/2,shifts+s/2];degs=[1,3];corr={(1,1):3,(1,3):5,(3,3):7}
    M=np.zeros((10,10));G=np.zeros((10,10));cache={}
    for ca,a in enumerate(degs):
      for cb,b in enumerate(degs):
       r=corr[tuple(sorted((a,b)))]
       for i in range(N):
        for j in range(N):
         I=ca*N+i;J=cb*N+j;c=round(float(ts[ca][i]-ts[cb][j]),12)
         key=(r,round(abs(c),12)) # W and beta are even in center
         if key not in cache:cache[key]=entry(r,h,abs(c))
         M[I,J]=cache[key]
         G[I,J]=beta(r,-c/h)
    M=(M+M.T)/2;G=(G+G.T)/2
    return M,G,(h,d,s)

def evalp(params,full=False):
    h,d,s=params
    if not(.10<h<.23 and .13<d<.34 and abs(s)<.20):return 1e3
    try:
      M,G,p=matrices(params);ge=np.linalg.eigvalsh(G)
      if ge[0]<2e-5:return 10+(2e-5-ge[0])*1e5
      vals,vec=eigh(M,G)
      return (vals,vec,G,M,ge,p) if full else vals[0]
    except Exception:return 1e3

if __name__=='__main__':
 print('base',evalp((.15,.225,0),True)[0][:3])
 print('false candidate corrected',evalp((.17919521,.17823161,.01146941),True)[0][:3])
 t=time.time()
 res=differential_evolution(evalp,[(.11,.21),(.15,.31),(-.17,.17)],popsize=10,maxiter=30,tol=1e-7,polish=False,seed=13,workers=1)
 print('DE',res.fun,res.x,time.time()-t)
 res2=minimize(evalp,res.x,method='Nelder-Mead',options={'maxiter':400,'xatol':2e-8,'fatol':1e-12})
 print('NM',res2.fun,res2.x,res2.success)
 vals,vec,G,M,ge,p=evalp(res2.x,True)
 print('actual p',p,'vals',vals[:5],'Gminmax',ge[[0,-1]],'cond',ge[-1]/ge[0])
 print('v',vec[:,0])
 # local scan sigma at optimum h,d
 for ss in np.linspace(p[2]-.03,p[2]+.03,13):
  print('S',ss,evalp((p[0],p[1],ss)))
