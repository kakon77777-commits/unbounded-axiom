"""统一运行可重现实验。"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent


def run(name: str, required: bool = True) -> None:
    print(f"\n##### {name} #####")
    try:
        subprocess.run([sys.executable, str(ROOT / name)], check=True)
    except subprocess.CalledProcessError:
        if required:
            raise
        print(f"{name} 未完成；可能缺少可选依赖。")


def main() -> None:
    run("verify_pi_formulas.py")
    run("compare_matrix_vs_role.py")
    run("higher_order_extensions.py")
    run("symbolic_verify.py", required=False)


if __name__ == "__main__":
    main()
