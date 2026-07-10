import math, random, time

M = 48
pts = []
R = int(math.isqrt(M))
for x in range(-R, R+1):
    for y in range(-R, R+1):
        for z in range(-R, R+1):
            if x*x+y*y+z*z <= M:
                pts.append((x,y,z))
N = len(pts)
idx = {p:i for i,p in enumerate(pts)}
DIRS = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
nbrs = []
for (x,y,z) in pts:
    ns = []
    for d in DIRS:
        q = (x+d[0],y+d[1],z+d[2])
        if q in idx: ns.append(idx[q])
    nbrs.append(ns)
start = idx[(0,0,0)]

def posa(seed, deadline):
    rng = random.Random(seed)
    path = [start]
    pos = [-1]*N
    pos[start] = 0
    onpath = [False]*N; onpath[start]=True
    while time.time() < deadline:
        e = path[-1]
        ext = [w for w in nbrs[e] if not onpath[w]]
        if ext:
            # prefer low remaining-degree extension (Warnsdorff flavor)
            w = min(ext, key=lambda t: (sum(0 if onpath[u] else 1 for u in nbrs[t]), rng.random()))
            pos[w] = len(path); path.append(w); onpath[w]=True
            if len(path) == N:
                return path
        else:
            # Pósa rotation keeping fixed start at path[0]
            cands = [w for w in nbrs[e] if w != path[-2] and pos[w] > 0]
            if not cands: return None
            v = rng.choice(cands)
            i = pos[v]
            # reverse path[i+1:]
            seg = path[i+1:]
            seg.reverse()
            path[i+1:] = seg
            for j in range(i+1, len(path)):
                pos[path[j]] = j
    return None

t_end = time.time() + 150
found = None; seed = 0
while time.time() < t_end and not found:
    seed += 1
    found = posa(seed, min(time.time()+15, t_end))
if found:
    assert len(found)==N and len(set(found))==N and found[0]==start
    for a,b in zip(found, found[1:]):
        pa,pb = pts[a],pts[b]
        assert sum(abs(pa[k]-pb[k]) for k in range(3))==1
        assert sum(c*c for c in pa)<=M and sum(c*c for c in pb)<=M
    print("VERIFIED center-start Hamiltonian path on R^2=48 ball, N =", len(found), " (seed %d)"%seed)
    with open("ham48_path.txt","w") as f:
        for i in found: f.write("%d %d %d\n"%pts[i])
    print("endpoint:", pts[found[-1]])
else:
    print("not found")
