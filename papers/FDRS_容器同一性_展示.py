#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FDRS 容器同一性展示 — 連接算子 R（表示轉換算子 / 容器同一性算子）

  一個底層容器 C_*(H)（精確整數魔方塊模型），三個觀察模式：
    [1] 立體模式   STEREO   — 高維幾何嵌入（四元數投影 3D）
    [2] 展平模式   FLAT     — FCSR 展平色位圖（6×9，3D→2D 攤平）
    [3] 譜模式     SPECTRAL — 貼面鄰接圖；同色連通分量 = β0-類比 = mult(0;L)

  核心鐵律（定義 3.4）：切換模式 = 套用算子 R。
  R 的作用域是「觀察者 m」，不是「被觀察的容器 C_*(H)」。
  容器指紋在 R 下嚴格不變，D(R)=0；只有 Φ（轉層）會改變容器。

  控制：
    1 / 2 / 3            切換觀察模式（套用 R）
    u d l r f b          順時針轉層（Φ）；大寫 U D L R F B 為逆時針
    方向鍵               立體模式下旋轉視角（僅觀察角度，非 R 非 Φ）
    + / -                立體模式縮放
    x  打亂      c  還原      q / ESC  離開

  作者語境：EveMissLab / Neo.K — FDRS 展示版。終端磷光風。
"""
import curses, math, time, random, sys, os

if sys.platform == "win32":
    os.system("")

# ============================================================
#  容器 C_*(H)：精確整數魔方塊模型（零浮點漂移）
# ============================================================
COLOR_RGB  = [(245,245,245),(240,215,40),(40,200,90),(45,95,220),(235,130,20),(220,45,45)]
COLOR_CHAR = ['白','黃','綠','藍','橙','紅']
NORMALS = {'U':(0,1,0),'D':(0,-1,0),'R':(1,0,0),'L':(-1,0,0),'F':(0,0,1),'B':(0,0,-1)}
SOLVED  = {'U':0,'D':1,'F':2,'B':3,'L':4,'R':5}
FACE_ORDER = 'UDFBLR'
FACE_BASIS = {  # (right=+col, down=+row) in cube space, looking at the face from outside
    'U':((1,0,0),(0,0,1)),  'D':((1,0,0),(0,0,-1)),
    'F':((1,0,0),(0,-1,0)), 'B':((-1,0,0),(0,-1,0)),
    'L':((0,0,1),(0,-1,0)), 'R':((0,0,-1),(0,-1,0)),
}

def rot90(v, axis, sign):
    x,y,z = v; ax,ay,az = axis; s = sign
    if ax<0 or ay<0 or az<0: ax,ay,az,s = -ax,-ay,-az,-s
    if   (ax,ay,az)==(1,0,0): return (x, -s*z,  s*y)
    elif (ax,ay,az)==(0,1,0): return ( s*z, y, -s*x)
    else:                     return (-s*y,  s*x, z)

class Cube:
    def __init__(self): self.reset()
    def reset(self):
        self.cubies=[]
        for x in(-1,0,1):
            for y in(-1,0,1):
                for z in(-1,0,1):
                    if (x,y,z)==(0,0,0): continue
                    st={}
                    if x==1:  st[(1,0,0)]=SOLVED['R']
                    if x==-1: st[(-1,0,0)]=SOLVED['L']
                    if y==1:  st[(0,1,0)]=SOLVED['U']
                    if y==-1: st[(0,-1,0)]=SOLVED['D']
                    if z==1:  st[(0,0,1)]=SOLVED['F']
                    if z==-1: st[(0,0,-1)]=SOLVED['B']
                    self.cubies.append({'p':(x,y,z),'st':st})
    def move(self, face, prime=False):
        axis=NORMALS[face]; sign=-1 if prime else 1; ax,ay,az=axis
        for c in self.cubies:
            x,y,z=c['p']
            if not ((ax and x==ax) or (ay and y==ay) or (az and z==az)): continue
            c['p']=rot90(c['p'],axis,sign)
            c['st']={rot90(k,axis,sign):v for k,v in c['st'].items()}
    def facelet(self, face, r, cc):
        n=NORMALS[face]; right,down=FACE_BASIS[face]
        pos=(n[0]+right[0]*(cc-1)+down[0]*(r-1),
             n[1]+right[1]*(cc-1)+down[1]*(r-1),
             n[2]+right[2]*(cc-1)+down[2]*(r-1))
        for c in self.cubies:
            if c['p']==pos: return c['st'].get(n)
        return None
    def grid(self, face):
        return [[self.facelet(face,r,cc) for cc in range(3)] for r in range(3)]
    def state_tuple(self):
        return tuple(self.facelet(f,r,cc) for f in FACE_ORDER for r in range(3) for cc in range(3))
    def fingerprint(self):
        h=0
        for v in self.state_tuple():
            h=(h*6+(v if v is not None else 0))&0xFFFFFFFF
            h=(h*2654435761)&0xFFFFFFFF
        return f"{h:08X}"
    def solved(self):
        for f in FACE_ORDER:
            flat=[v for row in self.grid(f) for v in row]
            if any(v!=flat[0] for v in flat): return False
        return True
    def solved_facelets(self):
        n=0
        for f in FACE_ORDER:
            g=self.grid(f)
            if g[1][1] is None: continue
            cen=g[1][1]
            for row in g:
                for v in row:
                    if v==cen: n+=1
        return n

# ---- 貼面 3D 幾何（固定；拓撲與顏色無關）----
def facelet_center(face,r,cc):
    n=NORMALS[face]; right,down=FACE_BASIS[face]
    return (n[0]*1.5+right[0]*(cc-1)+down[0]*(r-1),
            n[1]*1.5+right[1]*(cc-1)+down[1]*(r-1),
            n[2]*1.5+right[2]*(cc-1)+down[2]*(r-1))
ALL_FACELETS=[(f,r,cc) for f in FACE_ORDER for r in range(3) for cc in range(3)]
FL_INDEX={fl:i for i,fl in enumerate(ALL_FACELETS)}

def build_adjacency():
    mids={}
    def key(p): return (round(p[0],3),round(p[1],3),round(p[2],3))
    for idx,(f,r,cc) in enumerate(ALL_FACELETS):
        ctr=facelet_center(f,r,cc); right,down=FACE_BASIS[f]
        for d in (right,down):
            for s in (0.5,-0.5):
                m=key((ctr[0]+d[0]*s,ctr[1]+d[1]*s,ctr[2]+d[2]*s))
                mids.setdefault(m,[]).append(idx)
    adj={i:set() for i in range(len(ALL_FACELETS))}
    for lst in mids.values():
        for i in lst:
            for j in lst:
                if i!=j: adj[i].add(j)
    return adj
ADJ=build_adjacency()

def mono_components(cube):
    st=cube.state_tuple(); parent=list(range(len(ALL_FACELETS)))
    def find(a):
        while parent[a]!=a: parent[a]=parent[parent[a]]; a=parent[a]
        return a
    for i in ADJ:
        for j in ADJ[i]:
            if j>i and st[i]==st[j]:
                ri,rj=find(i),find(j)
                if ri!=rj: parent[ri]=rj
    return len({find(i) for i in range(len(ALL_FACELETS))})

# ============================================================
#  立體模式所需：向量 / 四元數 / 投影
# ============================================================
class V3:
    __slots__=('x','y','z')
    def __init__(s,x=0.,y=0.,z=0.): s.x,s.y,s.z=float(x),float(y),float(z)
    def dot(s,o): return s.x*o.x+s.y*o.y+s.z*o.z
    def cross(s,o): return V3(s.y*o.z-s.z*o.y, s.z*o.x-s.x*o.z, s.x*o.y-s.y*o.x)
    def __add__(s,o): return V3(s.x+o.x,s.y+o.y,s.z+o.z)
    def __sub__(s,o): return V3(s.x-o.x,s.y-o.y,s.z-o.z)
    def __mul__(s,k): return V3(s.x*k,s.y*k,s.z*k)
    @property
    def length(s): return math.sqrt(s.dot(s))
    def norm(s):
        l=s.length; return V3(s.x/l,s.y/l,s.z/l) if l>0 else V3()

class Quat:
    __slots__=('w','x','y','z')
    def __init__(s,w=1.,x=0.,y=0.,z=0.): s.w,s.x,s.y,s.z=w,x,y,z
    @classmethod
    def axis(cls,a,ang):
        a=a.norm(); h=ang/2; sn=math.sin(h)
        return cls(math.cos(h),a.x*sn,a.y*sn,a.z*sn)
    def mul(s,o):
        return Quat(s.w*o.w-s.x*o.x-s.y*o.y-s.z*o.z,
                    s.w*o.x+s.x*o.w+s.y*o.z-s.z*o.y,
                    s.w*o.y-s.x*o.z+s.y*o.w+s.z*o.x,
                    s.w*o.z+s.x*o.y-s.y*o.x+s.z*o.w)
    def normd(s):
        n=math.sqrt(s.w*s.w+s.x*s.x+s.y*s.y+s.z*s.z) or 1
        return Quat(s.w/n,s.x/n,s.y/n,s.z/n)
    def rotate(s,v):
        q=Quat(0,v.x,v.y,v.z); c=Quat(s.w,-s.x,-s.y,-s.z)
        r=s.mul(q).mul(c); return V3(r.x,r.y,r.z)

# ============================================================
#  色彩管理（有界調色盤；不做無上界快取）
# ============================================================
class Palette:
    PG=31; PG_DIM=32; PG_HI=33   # phosphor green pairs (kept < 64 for 8-colour terminals)
    def __init__(self):
        self.ready=False; self.bright=[0.45,0.65,0.85,1.05]
        self.solid={}   # (color_idx,level)->pair
        self.node={}    # color_idx->pair (full bright)
    @staticmethod
    def rgb256(r,g,b):
        if abs(r-g)<12 and abs(g-b)<12:
            v=int(round((r+g+b)/3))
            if v<8: return 16
            if v>248: return 231
            return 232+min(23,int((v-8)/247*24))
        def q(c): return int(round(c/255*5))
        return 16+36*q(r)+6*q(g)+q(b)
    def init(self):
        curses.start_color()
        try: curses.use_default_colors(); bg=-1
        except curses.error: bg=0
        def ip(pid,fg,bgc):
            try: curses.init_pair(pid,fg,bgc)
            except curses.error: pass
        pid=1
        for ci,rgb in enumerate(COLOR_RGB):       # bounded palette: 6*(1+4)=30 pairs
            self.node[ci]=pid; ip(pid,self.rgb256(*rgb),0); pid+=1
            for lv,b in enumerate(self.bright):
                col=self.rgb256(int(rgb[0]*b),int(rgb[1]*b),int(rgb[2]*b))
                ip(pid,col,col); self.solid[(ci,lv)]=pid; pid+=1
        ip(self.PG,46,bg); ip(self.PG_DIM,28,bg); ip(self.PG_HI,82,bg)
        self.ready=True
    def solid_pair(self,ci,brightness):
        lv=min(3,max(0,int(brightness*4)-1))
        return self.solid.get((ci,lv),0)
    def node_pair(self,ci): return self.node.get(ci,0)

PAL=Palette()

def safe(stdscr,y,x,s,attr=0):
    h,w=stdscr.getmaxyx()
    if y<0 or y>=h: return
    for i,ch in enumerate(s):
        if 0<=x+i<w-0:
            try: stdscr.addstr(y,x+i,ch,attr)
            except curses.error: pass

# ============================================================
#  模式 1：立體 STEREO
# ============================================================
class Solid:
    def __init__(self):
        self.rot=Quat(); self.scale=11.0
        self.cam=V3(0,0,7.5); self.focal=4.0; self.aspect=2.05; self.light=V3(0.4,0.8,0.6).norm()
        self.rot=Quat.axis(V3(1,0,0),-0.45).mul(Quat.axis(V3(0,1,0),0.6)).normd()
    def orbit(self,dx,dy):
        if dx: self.rot=Quat.axis(V3(0,1,0),dx).mul(self.rot).normd()
        if dy: self.rot=Quat.axis(V3(1,0,0),dy).mul(self.rot).normd()
    def zoom(self,d): self.scale=max(6.0,min(22.0,self.scale+d))
    def project(self,p,w,h):
        rp=self.rot.rotate(p); rel=rp-self.cam
        if rel.z>=-0.01: rel.z=-0.01
        sx=(rel.x*self.focal)/(-rel.z); sy=(-rel.y*self.focal)/(-rel.z)
        return (sx*self.scale+w/2, sy*self.scale/self.aspect+h/2)
    def fill_poly(self,stdscr,pts,pair,glyph,x0,x1,y0,y1):
        if len(pts)<3: return
        ys=[p[1] for p in pts]; ymin,ymax=int(min(ys)),int(max(ys))
        edges=[]
        n=len(pts)
        for i in range(n):
            ax,ay=pts[i]; bx,by=pts[(i+1)%n]
            if ay==by: continue
            if ay>by: ax,ay,bx,by=bx,by,ax,ay
            edges.append((ay,by,ax,(bx-ax)/(by-ay)))
        for y in range(max(ymin,y0),min(ymax,y1)+1):
            xs=[]
            for ay,by,ax,inv in edges:
                if ay<=y<by: xs.append(ax+inv*(y-ay))
            xs.sort()
            for i in range(0,len(xs)-1,2):
                a=max(x0,int(xs[i])); b=min(x1,int(xs[i+1]))
                for x in range(a,b+1):
                    try: stdscr.addstr(y,x,glyph,curses.color_pair(pair))
                    except curses.error: pass
    def draw(self,stdscr,cube,box):
        x0,y0,x1,y1=box; w=x1-x0; h=y1-y0; cx=x0+w//2; cy=y0+h//2
        faces=[]
        for c in cube.cubies:
            p=c['p']
            for n,color in c['st'].items():
                # square corners
                ctr=V3(p[0]+n[0]*0.5,p[1]+n[1]*0.5,p[2]+n[2]*0.5)
                if   n[0]: rt,dn=V3(0,1,0),V3(0,0,1)
                elif n[1]: rt,dn=V3(1,0,0),V3(0,0,1)
                else:      rt,dn=V3(1,0,0),V3(0,1,0)
                hgt=0.46
                corners=[ctr+rt*hgt+dn*hgt, ctr-rt*hgt+dn*hgt, ctr-rt*hgt-dn*hgt, ctr+rt*hgt-dn*hgt]
                nrot=self.rot.rotate(V3(*n))
                wc=self.rot.rotate(ctr)
                if nrot.dot(wc-self.cam)>=0: continue
                bright=0.3+max(0,nrot.dot(self.light))*0.85
                pair=PAL.solid_pair(color,bright)
                sp=[self.project(c2,w,h) for c2 in corners]
                sp=[(px-w/2+cx, py-h/2+cy) for px,py in sp]
                faces.append(((wc-self.cam).length, sp, pair))
        faces.sort(key=lambda f:f[0],reverse=True)
        for depth,sp,pair in faces:
            self.fill_poly(stdscr,sp,pair,'█',x0,x1,y0,y1)
    def readout(self,cube):
        return [f"嵌入維度 dim=3   視角四元數 q=({self.rot.w:+.2f},{self.rot.x:+.2f},{self.rot.y:+.2f},{self.rot.z:+.2f})",
                f"可見貼面（背面剔除後）≈ {self._visible(cube)} / 54"]
    def _visible(self,cube):
        v=0
        for c in cube.cubies:
            for n in c['st']:
                nrot=self.rot.rotate(V3(*n)); ctr=self.rot.rotate(V3(c['p'][0]+n[0]*.5,c['p'][1]+n[1]*.5,c['p'][2]+n[2]*.5))
                if nrot.dot(ctr-self.cam)<0: v+=1
        return v

# ============================================================
#  模式 2：展平 FLAT (FCSR)
# ============================================================
class Flat:
    #  layout (face -> (block_row, block_col)) on a 3x4 grid of faces
    LAYOUT={'U':(0,1),'L':(1,0),'F':(1,1),'R':(1,2),'B':(1,3),'D':(2,1)}
    def draw(self,stdscr,cube,box):
        x0,y0,x1,y1=box
        cellw=2; cellh=1; fgap_x=2; fgap_y=1
        blkw=3*cellw; blkh=3*cellh
        total_w=4*blkw+3*fgap_x; total_h=3*blkh+2*fgap_y
        ox=x0+max(0,((x1-x0)-total_w)//2); oy=y0+max(0,((y1-y0)-total_h)//2)
        for f,(br,bc) in self.LAYOUT.items():
            g=cube.grid(f)
            bx=ox+bc*(blkw+fgap_x); by=oy+br*(blkh+fgap_y)
            for r in range(3):
                for c in range(3):
                    ci=g[r][c]
                    if ci is None: continue
                    pair=PAL.node_pair(ci)
                    glyph='██'
                    cell_x=bx+c*cellw; cell_y=by+r*cellh
                    try: stdscr.addstr(cell_y,cell_x,glyph,curses.color_pair(pair)|curses.A_BOLD)
                    except curses.error: pass
            # face label
            safe(stdscr,by-0 if br==0 else by, bx+blkw, "", 0)
            safe(stdscr,by+blkh, bx, f"{f}", curses.color_pair(Palette.PG_DIM))
        # net seam hint
        safe(stdscr,oy+total_h+1,ox,"3D 表面沿稜邊攤平 → 立體鄰接關係化為平面鄰接（保結構映射 Φ）",
             curses.color_pair(Palette.PG_DIM))
    def readout(self,cube):
        return [f"展平映射 Φ: R^3 表面 → R^2 平面網   6×9 = 54 色位",
                f"歸位貼面 = {cube.solved_facelets()} / 54   "+("（容器已解：六面同色）" if cube.solved() else "")]

# ============================================================
#  模式 3：譜 SPECTRAL（貼面鄰接圖）
# ============================================================
class Spectral:
    LAYOUT=Flat.LAYOUT
    def _coords(self,box):
        x0,y0,x1,y1=box
        cellw=4; cellh=2; fgap_x=3; fgap_y=2
        blkw=3*cellw; blkh=3*cellh
        total_w=4*blkw+3*fgap_x; total_h=3*blkh+2*fgap_y
        ox=x0+max(0,((x1-x0)-total_w)//2); oy=y0+max(0,((y1-y0)-total_h)//2)
        pos={}
        for f,(br,bc) in self.LAYOUT.items():
            bx=ox+bc*(blkw+fgap_x); by=oy+br*(blkh+fgap_y)
            for r in range(3):
                for c in range(3):
                    pos[(f,r,c)]=(by+r*cellh, bx+c*cellw)
        return pos
    def draw(self,stdscr,cube,box):
        pos=self._coords(box); st=cube.state_tuple()
        # edges first (dim green), only intra-face for legibility
        drawn=set()
        for i in ADJ:
            f,r,c=ALL_FACELETS[i]
            for j in ADJ[i]:
                if (j,i) in drawn: continue
                drawn.add((i,j))
                f2,r2,c2=ALL_FACELETS[j]
                if f!=f2: continue   # seam edges omitted from drawing (kept in component math)
                y1c,x1c=pos[(f,r,c)]; y2c,x2c=pos[(f2,r2,c2)]
                same = st[i]==st[j]
                attr=curses.color_pair(Palette.PG if same else Palette.PG_DIM)
                if y1c==y2c:
                    for x in range(min(x1c,x2c)+1,max(x1c,x2c)):
                        safe(stdscr,y1c,x,'─',attr)
                elif x1c==x2c:
                    for y in range(min(y1c,y2c)+1,max(y1c,y2c)):
                        safe(stdscr,y,x1c,'│',attr)
        # nodes
        for (f,r,c),(y,x) in pos.items():
            ci=st[FL_INDEX[(f,r,c)]]
            safe(stdscr,y,x,'●',curses.color_pair(PAL.node_pair(ci))|curses.A_BOLD)
    def readout(self,cube):
        k=mono_components(cube)
        return [f"貼面鄰接圖 G=(V,E)  |V|=54  |E|=108  （每點度數 4）",
                f"同色連通分量 β0 = mult(0; L) = {k}   "+("（解 ⇒ 6 個分量，每面一塊）" if cube.solved() else f"（解時為 6；現 {k}）")]

# ============================================================
#  HUD / chrome
# ============================================================
MODE_NAME={1:('立體 STEREO','觀察模式 m = top  · 高維幾何嵌入'),
           2:('展平 FLAT (FCSR)','觀察模式 m = lin  · 攤平色位 / 邊界算子矩陣'),
           3:('譜 SPECTRAL','觀察模式 m = spec · 鄰接圖 Laplacian')}

def draw_chrome(stdscr,mode,cube,prev_fp,last_action,renderers,flash):
    h,w=stdscr.getmaxyx()
    PG=curses.color_pair(Palette.PG); PGD=curses.color_pair(Palette.PG_DIM); HI=curses.color_pair(Palette.PG_HI)|curses.A_BOLD
    bar='─'*(w-1)
    safe(stdscr,0,0,bar,PGD)
    title="FDRS · 連接算子 𝓡（容器同一性）"
    safe(stdscr,0,2,f" {title} ",HI)
    name,sub=MODE_NAME[mode]
    safe(stdscr,1,2,f"模式 [{mode}] {name}",PG)
    safe(stdscr,1,2+24,f"  {sub}",PGD)
    fp=cube.fingerprint()
    safe(stdscr,2,2,f"容器指紋 C∗(H) = {fp}",PG)
    # R invariance proof
    same = (prev_fp==fp)
    if last_action.startswith('𝓡'):
        msg=f"𝓡 套用：指紋切換前後 {'相同 ✓ — 容器不變，僅換觀察角度' if same else '改變 ✗'}    𝒟(𝓡)=0.000"
        safe(stdscr,2,2+34,msg, HI if same else PGD)
    else:
        safe(stdscr,2,2+34,f"上一動作：{last_action}    𝒟(𝓡)=0.000（𝓡 恆為等距，不降維）",PGD)
    safe(stdscr,3,0,bar,PGD)
    # per-mode readout (bottom)
    ro=renderers[mode].readout(cube)
    for i,line in enumerate(ro):
        safe(stdscr,h-5+i,2,line,PG)
    safe(stdscr,h-3,0,bar,PGD)
    ctl="[1/2/3] 套用 𝓡 切換模式   u d l r f b / 大寫=逆 轉層 Φ   ←↑↓→ 旋轉視角(立體)   +/- 縮放   x 打亂  c 還原  q 離開"
    safe(stdscr,h-2,2,ctl[:w-4],PGD)
    if flash:
        safe(stdscr,h-2, w-len(flash)-3, flash, HI)

# ============================================================
#  主程式
# ============================================================
def main(stdscr):
    curses.curs_set(0); stdscr.nodelay(1); stdscr.keypad(1)
    if not curses.has_colors():
        stdscr.addstr(0,0,"終端不支援顏色"); stdscr.getch(); return
    PAL.init()
    cube=Cube()
    renderers={1:Solid(),2:Flat(),3:Spectral()}
    mode=1
    prev_fp=cube.fingerprint()
    last_action="初始化"
    flash=""; flash_t=0
    need=True
    MOVE_KEYS={ord('u'):('U',False),ord('d'):('D',False),ord('l'):('L',False),
               ord('r'):('R',False),ord('f'):('F',False),ord('b'):('B',False),
               ord('U'):('U',True),ord('D'):('D',True),ord('L'):('L',True),
               ord('R'):('R',True),ord('F'):('F',True),ord('B'):('B',True)}
    while True:
        h,w=stdscr.getmaxyx()
        if w<74 or h<26:
            stdscr.erase(); safe(stdscr,h//2,2,"請將終端放大到至少 74 x 26",curses.color_pair(Palette.PG))
            stdscr.refresh(); time.sleep(0.2)
            k=stdscr.getch()
            if k in (27,ord('q')): break
            continue
        if need:
            stdscr.erase()
            box=(1,5,w-2,h-6)
            renderers[mode].draw(stdscr,cube,box)
            draw_chrome(stdscr,mode,cube,prev_fp,last_action,renderers,flash)
            stdscr.refresh(); need=False
        if flash and time.time()-flash_t>1.4:
            flash=""; need=True
        k=stdscr.getch()
        if k==-1: time.sleep(0.02); continue
        if k in (27,ord('q')): break
        elif k in (ord('1'),ord('2'),ord('3')):
            new=int(chr(k))
            prev_fp=cube.fingerprint()      # snapshot BEFORE switch
            if new!=mode:
                mode=new; last_action=f"𝓡: m → {MODE_NAME[mode][0]}"
                flash="𝓡 套用 · 容器不變"; flash_t=time.time()
            need=True
        elif k in MOVE_KEYS:
            f,pr=MOVE_KEYS[k]; prev_fp=cube.fingerprint()
            cube.move(f,pr); last_action=f"Φ: {f}{'′' if pr else ''}（轉層，容器改變）"
            flash="Φ 套用 · 指紋變更"; flash_t=time.time(); need=True
        elif k==curses.KEY_LEFT and mode==1: renderers[1].orbit(-0.18,0); last_action="旋轉視角"; need=True
        elif k==curses.KEY_RIGHT and mode==1: renderers[1].orbit(0.18,0); last_action="旋轉視角"; need=True
        elif k==curses.KEY_UP and mode==1: renderers[1].orbit(0,-0.18); last_action="旋轉視角"; need=True
        elif k==curses.KEY_DOWN and mode==1: renderers[1].orbit(0,0.18); last_action="旋轉視角"; need=True
        elif k in (ord('+'),ord('=')) and mode==1: renderers[1].zoom(1.5); need=True
        elif k==ord('-') and mode==1: renderers[1].zoom(-1.5); need=True
        elif k==ord('x'):
            prev_fp=cube.fingerprint()
            for _ in range(20): cube.move(random.choice('UDLRFB'),random.random()<0.5)
            last_action="Φ×20（打亂）"; flash="已打亂"; flash_t=time.time(); need=True
        elif k==ord('c'):
            prev_fp=cube.fingerprint(); cube.reset()
            last_action="還原容器"; flash="已還原"; flash_t=time.time(); need=True

def start():
    print("="*30)
    print(" FDRS 容器同一性展示 𝓡")
    print("="*30)
    print(" 一個容器 C∗(H)，三個觀察模式：立體 / 展平 / 譜")
    print(" 按 1 2 3 切換模式（= 套用算子 𝓡），u d l r f b 轉層（= Φ）")
    print(" 觀察：切換模式時容器指紋不變、𝒟(𝓡)=0；轉層時指紋變更。")
    print(" 需要 74×26 以上的終端。按任意鍵開始 …")
    try: input()
    except (EOFError,KeyboardInterrupt): pass
    curses.wrapper(main)

if __name__=="__main__":
    start()
