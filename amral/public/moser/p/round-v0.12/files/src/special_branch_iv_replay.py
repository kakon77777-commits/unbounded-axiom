import mpmath as mp,time,json
mp.mp.dps=90;iv=mp.iv;iv.dps=75
EPS=iv.mpf('0.037');W=iv.mpf('0.3361057714712081');BETA=iv.mpf('1.405382794839393');DELTA=iv.mpf('0.05204734906280986');CENTER=iv.mpf('0.5801781668857768')
SQ=iv.sqrt(iv.mpf(3));A=((3+4*SQ)/18)/iv.mpf('1.0048');B=((4+SQ)/6)/iv.mpf('1.0048');L0=1-2*W

def tanh(x):return 1-2/(iv.exp(2*x)+1)
def raw(u):return iv.mpf('.5')*(1-tanh((u-CENTER)/EPS))
r0=raw(iv.mpf(0));r1=raw(iv.mpf(1))
def theta(u):return BETA+DELTA*(raw(u)-r1)/(r0-r1)
def lo(x):return mp.mpf(x._mpi_[0])
def hi(x):return mp.mpf(x._mpi_[1])
N=65536;s1=iv.mpf(0);s2=iv.mpf(0);sq=iv.mpf(0);qa=2/SQ-1;qb=1/SQ;t=time.time()
for i in range(N):
 u=iv.mpf(2*i+1)/iv.mpf(2*N);th=theta(u);ss=iv.sin(th);cc=iv.cos(th);s1+=ss;s2+=cc;sq+=qa*ss-qb*cc
print('loop',time.time()-t)
# analytic errors scalar high precision
mp.mp.dps=90
Eps=mp.mpf('0.037');Delta=mp.mpf('0.05204734906280986');Center=mp.mpf('0.5801781668857768');
def rawmp(u):return mp.mpf('.5')*(1-mp.tanh((u-Center)/Eps))
r0m=rawmp(0);r1m=rawmp(1);C=Delta*mp.mpf('.5')/Eps/(r0m-r1m);M1=C;M2=2*C/Eps*2/(3*mp.sqrt(3));M=M1*M1+M2;Eq=mp.sqrt((2/mp.sqrt(3)-1)**2+(1/mp.sqrt(3))**2)*M/(24*N*N);Ec=M/(24*N*N)
I1=s1/iv.mpf(N)+iv.mpf([-Ec,Ec]);I2=s2/iv.mpf(N)+iv.mpf([-Ec,Ec]);Iq=sq/iv.mpf(N)+iv.mpf([-Eq,Eq]);s270=W*I1/A+(W*I2+L0)/B;diff=L0*(1/(2*A)-1/B)+(W/A)*Iq
print(json.dumps({'s270':[mp.nstr(lo(s270),60),mp.nstr(hi(s270),60)],'diff':[mp.nstr(lo(diff),60),mp.nstr(hi(diff),60)],'loop_seconds':time.time()-t},indent=2))
