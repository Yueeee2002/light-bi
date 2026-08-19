"""
独立建表 / 种子脚本。

用法（在 backend 目录下）：
    python -m app.db.init_db
或：
    python scripts/init_db.py
"""

import sys
from pathlib import Path

# 保证以 scripts/ 运行时也能 import app
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.db.init_db import init_db  # noqa: E402

if __name__ == "__main__":
    init_db()
    print("[init_db] database ready")
