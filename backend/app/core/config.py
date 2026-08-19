"""应用配置。优先读取环境变量，开发环境提供可用默认值。"""

import os
from pathlib import Path

# backend/ 目录
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)


def _split_origins(raw: str) -> list[str]:
    return [item.strip() for item in raw.split(",") if item.strip()]


class Settings:
    """全局配置单例来源，后续阶段鉴权 / CSV 限制均从此读取。"""

    APP_NAME: str = "Light-BI"
    APP_VERSION: str = "0.1.0"

    SECRET_KEY: str = os.getenv("SECRET_KEY", "light-bi-dev-secret-change-me")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440"))

    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{DATA_DIR / 'light_bi.db'}",
    )

    CORS_ORIGINS: list[str] = _split_origins(
        os.getenv("CORS_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000")
    )

    # CSV 上传限制 5MB（后续数据源阶段使用）
    CSV_MAX_SIZE: int = 5 * 1024 * 1024
    CSV_ALLOWED_ENCODINGS: tuple[str, ...] = ("utf-8", "gbk", "gb2312")


settings = Settings()
