"""Pure mpmath verifier for the v0.9 270-degree cusp."""
import mpmath as mp
mp.mp.dps=100
eps=mp.mpf("0.037"); w=mp.mpf("0.3361057714712081")
beta=mp.mpf("1.405382794839393"); delta=mp.mpf("0.05204734906280986")
center=mp.mpf("0.5801781668857768")
rt3=mp.sqrt(3); A=((3+4*rt3)/18)/mp.mpf("1.0048"); B=((4+rt3)/6)/mp.mpf("1.0048")
l0=1-2*w
def raw(u): return mp.mpf("0.5")*(1-mp.tanh((u-center)/eps))
r0,r1=raw(0),raw(1)
def theta(u): return beta+delta*(raw(u)-r1)/(r0-r1)
splits=sorted(set([mp.mpf(0),center-8*eps,center-4*eps,center,center+4*eps,center+8*eps,mp.mpf(1)]))
def integ(method,f): return mp.fsum(method(f,[a,b]) for a,b in zip(splits[:-1],splits[1:]) if b>a)
def cusp(method):
    ix=integ(method,lambda u:mp.cos(theta(u)));iy=integ(method,lambda u:mp.sin(theta(u)))
    return w*iy/A+(w*ix+l0)/B
print("quad  ",mp.nstr(cusp(mp.quad),100))
print("quadgl",mp.nstr(cusp(mp.quadgl),100))
