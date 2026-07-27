from __future__ import annotations

import hashlib
import os
import shutil
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PARENT = ROOT.parent
PACKAGE_NAME = ROOT.name
MAIN_PAPER = (
    "區間Green核原子證書_RH抽象連續障礙的有理包絡與二階"
    "Sylvester判定_v0.7_半AI自主研究稿.md"
)
ZIP_PATH = PARENT / f"{PACKAGE_NAME}.zip"
PAPER_PATH = PARENT / MAIN_PAPER
CHECKSUM_PATH = (
    PARENT
    / "RH_IntervalGreenKernel_AtomicCertificate_v0.7_SHA256SUMS.txt"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def release_files() -> list[Path]:
    output = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if "__pycache__" in relative.parts:
            continue
        if path.suffix in {".pyc", ".pyo"}:
            continue
        if relative.as_posix() == "MANIFEST.sha256":
            continue
        output.append(path)
    return sorted(output, key=lambda path: path.relative_to(ROOT).as_posix())


def write_manifest() -> None:
    rows = [
        f"{sha256(path)}  {path.relative_to(ROOT).as_posix()}"
        for path in release_files()
    ]
    (ROOT / "MANIFEST.sha256").write_text(
        "\n".join(rows) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    write_manifest()
    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(
        ZIP_PATH,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        for path in sorted(
            list(release_files()) + [ROOT / "MANIFEST.sha256"],
            key=lambda item: item.relative_to(ROOT).as_posix(),
        ):
            archive.write(
                path,
                arcname=(
                    Path(PACKAGE_NAME)
                    / path.relative_to(ROOT)
                ).as_posix(),
            )
    shutil.copy2(ROOT / MAIN_PAPER, PAPER_PATH)
    checksum_rows = [
        f"{sha256(ZIP_PATH)}  {ZIP_PATH.name}",
        f"{sha256(PAPER_PATH)}  {PAPER_PATH.name}",
    ]
    CHECKSUM_PATH.write_text(
        "\n".join(checksum_rows) + "\n",
        encoding="utf-8",
    )
    for path in (ZIP_PATH, PAPER_PATH, CHECKSUM_PATH):
        print(
            f"{path.name}\t{os.path.getsize(path)} bytes\t{sha256(path)}"
        )


if __name__ == "__main__":
    main()

