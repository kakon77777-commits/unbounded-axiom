from __future__ import annotations

import hashlib
import shutil
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RELEASE_ROOT = ROOT.parent
ARCHIVE = RELEASE_ROOT / f"{ROOT.name}.zip"
PAPER_NAME = (
    "RH支撐質數對偶前沿_軸網格假逃逸與頻譜缺口轉向"
    "_v0.4_半AI自主研究稿.md"
)
STANDALONE_PAPER = RELEASE_ROOT / PAPER_NAME
CHECKSUMS = RELEASE_ROOT / (
    "RH_Support_Prime_Dual_Frontier_v0.4_SHA256SUMS.txt"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def package_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.name != "MANIFEST.sha256"
        and "__pycache__" not in path.parts
        and ".pytest_cache" not in path.parts
    )


def main() -> None:
    files = package_files()
    manifest = "\n".join(
        f"{sha256(path)}  {path.relative_to(ROOT).as_posix()}"
        for path in files
    )
    (ROOT / "MANIFEST.sha256").write_text(
        manifest + "\n",
        encoding="utf-8",
    )

    archive_files = package_files() + [ROOT / "MANIFEST.sha256"]
    with zipfile.ZipFile(
        ARCHIVE,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as handle:
        for path in sorted(archive_files):
            relative = Path(ROOT.name) / path.relative_to(ROOT)
            handle.write(path, relative.as_posix())

    shutil.copy2(ROOT / PAPER_NAME, STANDALONE_PAPER)
    CHECKSUMS.write_text(
        "\n".join(
            (
                f"{sha256(ARCHIVE)}  {ARCHIVE.name}",
                f"{sha256(STANDALONE_PAPER)}  "
                f"{STANDALONE_PAPER.name}",
            )
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
