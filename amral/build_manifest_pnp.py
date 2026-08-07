import argparse, glob, hashlib, json, os, re

ROUND_RE = re.compile(r"^(\d{2})_")

ROUND_TITLES = {
    "00": "數學構造—狀態機中介層",
    "01": "存在量詞狀態坍縮",
    "02": "跨表示不變量爭奪戰",
    "03": "演算法軌跡切割與因果瓶頸",
    "04": "局部—全域障礙與表示逃逸",
    "05": "表示逃逸錦標賽與困難矩陣",
    "06": "多項式表示變換閉包與閉包悖論",
    "07": "代數不變量爭奪戰與演算法—代數橋",
    "08": "演算法—代數橋壓力測試與精確商結構",
    "09": "尋找 SAT 的 Blossom 與商化債務",
    "10": "多重反結構核心與異質黏合債務",
    "11": "共同保存結構崩塌與動態橋接",
    "12": "介面語言格、Schaefer 臨界與遞迴 SAT",
    "13": "可解閉包穩定性與多項式鏈爆炸",
    "14": "複雜度勢能遊戲與證書完備性陷阱",
    "15": "Tractability Proof System 與正常形逃逸",
    "16": "Clocked 對角化與統一指數障礙",
    "17": "統一計算證書壓縮與普遍化跳躍",
    "18": "對角切片壓縮與稀疏性上推陷阱",
    "19": "Block／Delayed Diagonalization 與階段控制依賴",
    "20": "階段控制複雜度與極限監視器",
    "21": "量詞監視器與有限證書階層",
    "22": "量詞壓縮定理與有限基底遊戲",
    "23": "演算法 WQO 與語義單調性裂縫",
    "24": "語義單調性工程與抽象精度三難",
}

def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", required=True, choices=["p-np-dual"])
    args = ap.parse_args()

    base = f"public/{args.case}"
    files_dir = f"{base}/files"
    p_dir = f"{base}/p"

    rounds = []
    total_size = 0
    for fn in sorted(glob.glob(files_dir + "/[0-9][0-9]_*.md")):
        basename = os.path.basename(fn)
        m = ROUND_RE.match(basename)
        num = m.group(1)
        size = os.path.getsize(fn)
        total_size += size
        rid = "round-00" if num == "00" else f"round-{int(num):02d}"
        has_detail = os.path.isdir(f"{p_dir}/{rid}")
        rounds.append({
            "id": rid,
            "version": num,
            "title": ROUND_TITLES.get(num, basename),
            "filename": basename,
            "size": size,
            "sha256": sha256_of(fn),
            "generated_at": "2026-08-01T00:00:00Z" if num != "00" else "2026-08-01T00:00:00Z",
            "file_count": 1,
            "has_detail_page": has_detail,
        })

    manifest = {
        "generated_by": "build_manifest_pnp.py",
        "case": args.case,
        "counts": {"total": len(rounds)},
        "total_size": total_size,
        "rounds": rounds,
        "other": [],
    }

    out_path = f"{base}/manifest.json"
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"wrote {out_path} -- {len(rounds)} docs, {total_size // 1024} KiB")

if __name__ == "__main__":
    main()
