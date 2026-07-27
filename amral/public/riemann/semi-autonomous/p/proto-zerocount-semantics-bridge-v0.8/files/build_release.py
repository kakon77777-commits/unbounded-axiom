from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PARENT = ROOT.parent
PACKAGE_NAME = ROOT.name
PAPER_NAME = (
    "零點計數係數語義橋_RH上包絡無效定理組態下界與連續逃逸_"
    "v0.8_半AI自主研究稿.md"
)
ZIP_PATH = PARENT / f"{PACKAGE_NAME}.zip"
STANDALONE_PAPER = PARENT / PAPER_NAME
CHECKSUM_PATH = PARENT / f"{PACKAGE_NAME}_SHA256SUMS.txt"
MANIFEST = ROOT / "MANIFEST.sha256"


def ignored(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    return (
        "__pycache__" in relative.parts
        or path.suffix == ".pyc"
        or path.name == ".DS_Store"
    )


def package_files(include_manifest: bool = True) -> list[Path]:
    output = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ignored(path):
            continue
        if not include_manifest and path == MANIFEST:
            continue
        output.append(path)
    return sorted(output, key=lambda item: item.as_posix())


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_manifest() -> None:
    rows = [
        f"{sha256(path)}  {path.relative_to(ROOT).as_posix()}"
        for path in package_files(include_manifest=False)
    ]
    MANIFEST.write_text("\n".join(rows) + "\n", encoding="utf-8")


def main() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "validate_package.py")],
        cwd=ROOT,
        check=True,
    )
    write_manifest()
    with zipfile.ZipFile(
        ZIP_PATH,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        for path in package_files(include_manifest=True):
            archive.write(
                path,
                arcname=(
                    Path(PACKAGE_NAME)
                    / path.relative_to(ROOT)
                ).as_posix(),
            )
    shutil.copy2(ROOT / PAPER_NAME, STANDALONE_PAPER)
    CHECKSUM_PATH.write_text(
        "\n".join(
            (
                f"{sha256(ZIP_PATH)}  {ZIP_PATH.name}",
                (
                    f"{sha256(STANDALONE_PAPER)}  "
                    f"{STANDALONE_PAPER.name}"
                ),
            )
        )
        + "\n",
        encoding="utf-8",
    )
    print(ZIP_PATH)
    print(STANDALONE_PAPER)
    print(CHECKSUM_PATH)


if __name__ == "__main__":
    main()
