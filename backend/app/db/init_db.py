"""建表并写入 3 个内置测试账号。"""

from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.db.base import Base
from app.db.session import SessionLocal, engine
from app.models import User  # noqa: F401  确保模型注册到 metadata

# 内置测试账号（MVP 开发 / 演示用）
SEED_USERS: list[tuple[str, str, str]] = [
    ("admin", "123456", "admin"),
    ("analyst", "123456", "analyst"),
    ("viewer", "123456", "viewer"),
]


def init_db() -> None:
    """创建 4 张表（若不存在），并补齐种子用户。"""
    # 导入全部模型，避免 create_all 漏表
    from app.models.data_source import DataSource  # noqa: F401
    from app.models.dataset import Dataset  # noqa: F401
    from app.models.dashboard import Dashboard  # noqa: F401

    Base.metadata.create_all(bind=engine)

    db: Session = SessionLocal()
    try:
        _seed_users(db)
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def _seed_users(db: Session) -> None:
    for username, password, role in SEED_USERS:
        exists = db.query(User).filter(User.username == username).first()
        if exists:
            continue
        db.add(
            User(
                username=username,
                password_hash=hash_password(password),
                role=role,
            )
        )
        print(f"[init_db] seeded user: {username} / {password} role={role}")


if __name__ == "__main__":
    init_db()
    print("[init_db] database ready")
