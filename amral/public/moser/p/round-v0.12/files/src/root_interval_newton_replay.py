import mpmath as mp,json,time
mp.mp.dps=80;iv=mp.iv;iv.dps=70
R11='/mnt/data/Moser_Skew_Lab_v0.11/data'
roots=json.load(open(R11+'/stationary_root_boxes.json'))
EPS=mp.mpf('0.037');W=mp.mpf('0.3361057714712081');BETA=mp.mpf('1.405382794839393');DELTA=mp.mpf('0.05204734906280986');CENTER=mp.mpf('0.5801781668857768');ALPHA=BETA+DELTA;L0=1-2*W;PI=mp.pi
SQ=mp.sqrt(3);A=((3+4*SQ)/18)/mp.mpf('1.0048');B=((4+SQ)/6)/mp.mpf('1.0048');AI=iv.mpf(str(A));BI=iv.mpf(str(B));WI=iv.mpf(str(W))
def lo(x):return mp.mpf(x._mpi_[0])
def hi(x):return mp.mpf(x._mpi_[1])
def ib(a,b=None):return iv.mpf([a,a if b is None else b])
def raw(u):return mp.mpf('.5')*(1-mp.tanh((u-CENTER)/EPS))
r0=raw(0);r1=raw(1)
def theta(u):return BETA+DELTA*(raw(u)-r1)/(r0-r1)
def inv(t):q=(t-BETA)/DELTA;rr=r1+q*(r0-r1);return CENTER+EPS*mp.atanh(1-2*rr)
C=DELTA*mp.mpf('.5')/EPS/(r0-r1)
def tpbox(a,b):
 z1=(a-CENTER)/EPS;z2=(b-CENTER)/EPS;ma=max(abs(z1),abs(z2));mi=0 if z1<=0<=z2 else min(abs(z1),abs(z2));mx=1 if mi==0 else 1/mp.cosh(mi)**2;mn=1/mp.cosh(ma)**2;return ib(-C*mx,-C*mn)
cache={}
def prefix(u):
 key=mp.nstr(u,50)
 if key in cache:return cache[key]
 splits=[0,u]
 if u>CENTER:splits=[0,CENTER,u]
 fx=lambda t:W*mp.cos(theta(t));fy=lambda t:W*mp.sin(theta(t))
 x1=mp.quad(fx,splits);x2=mp.quadgl(fx,splits);y1=mp.quad(fy,splits);y2=mp.quadgl(fy,splits)
 ex=abs(x1-x2)+mp.mpf('1e-55');ey=abs(y1-y2)+mp.mpf('1e-55')
 out=(ib(min(x1,x2)-ex,max(x1,x2)+ex),ib(min(y1,y2)-ey,max(y1,y2)+ey));cache[key]=out;return out
p1=prefix(mp.mpf(1));P={'p0':(iv.mpf(0),iv.mpf(0)),'p1':p1,'p2':(p1[0]+iv.mpf(str(L0)),p1[1]),'p3':(2*p1[0]+iv.mpf(str(L0)),iv.mpf(0))};TX=P['p3'][0]
OFF={'x':0,'y':PI/2,'d':PI/6}
def const(role,label,mid):
 psi=OFF[role]-mid;rng=(BETA,ALPHA) if label=='L' else (-ALPHA,-BETA)
 for pm in (1,-1):
  for k in range(-3,4):
   t=psi+pm*PI/2+2*k*PI
   if rng[0]<t<rng[1]:return t+mid
 raise Exception((role,label,mid))
def support(role,label,a,b):
 if label in P:return {'p':P[label],'int':False}
 c=const(role,label,(a+b)/2);tlo=c-b;thi=c-a
 if label=='L':u1=inv(thi);u2=inv(tlo);q1=prefix(u1);q2=prefix(u2);pt=(ib(lo(q1[0]),hi(q2[0])),ib(lo(q1[1]),hi(q2[1])));tp=tpbox(u1,u2)
 else:
  # q=-target in [ -thi,-tlo ], inverse decreasing
  v1=inv(-tlo);v2=inv(-thi);q1=prefix(v1);q2=prefix(v2);pt=(TX-ib(lo(q1[0]),hi(q2[0])),ib(lo(q1[1]),hi(q2[1])));tp=tpbox(v1,v2)
 return {'p':pt,'int':True,'t':(iv.cos(ib(tlo,thi)),iv.sin(ib(tlo,thi))),'tp':tp}
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def eval(a,b,sig):
 ph=ib(a,b);c=iv.cos(ph);s=iv.sin(ph);nx=(c,-s);ny=(s,c);nd=(c/AI+s/BI,-s/AI+c/BI);nxp=(-s,-c);nyp=(c,-s);ndp=(nxp[0]/AI+nyp[0]/BI,nxp[1]/AI+nyp[1]/BI);NN={'x':(nx,nxp),'y':(ny,nyp),'d':(nd,ndp)};D={r:support(r,l,a,b) for r,l in zip(('x','y','d'),sig.split('|'))};H={};H1={};H2={}
 for r in ('x','y','d'):
  n,np1=NN[r];p=D[r]['p'];H[r]=dot(n,p);H1[r]=dot(np1,p);pp=(iv.mpf(0),iv.mpf(0))
  if D[r]['int']:pp=(-WI*D[r]['t'][0]/D[r]['tp'],-WI*D[r]['t'][1]/D[r]['tp'])
  H2[r]=-dot(n,p)+dot(np1,pp)
 return H['d']-H['x']/AI-H['y']/BI,H1['d']-H1['x']/AI-H1['y']/BI,H2['d']-H2['x']/AI-H2['y']/BI
out=[];t=time.time()
for r in roots:
 a,b=map(lambda x:mp.mpf(repr(x)),r['uniqueness_box']);m=(a+b)/2;_,fm,_=eval(m,m,r['signature']);_,_,fp=eval(a,b,r['signature']);N=ib(m)-fm/fp
 out.append({'sig':r['signature'],'kind':r['kind'],'fp':[str(lo(fp)),str(hi(fp))],'newton':[str(lo(N)),str(hi(N))],'inside':lo(N)>a and hi(N)<b})
 print(len(out),r['signature'],out[-1]['inside'],time.time()-t)
print(json.dumps(out,indent=2))
