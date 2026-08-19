"""SQLAlchemy 声明基类。"""

from datetime import datetime, timezone

from sqlalchemy.orm import DeclarativeBase


def utcnow() -> datetime:
    """无时区 UTC 时间，写入 SQLite DATETIME。"""
    return datetime.now(timezone.utc).replace(tzinfo=None)


class Base(DeclarativeBase):
    """所有 ORM 模型的基类。"""
