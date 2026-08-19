"""用户表 user。"""

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base, utcnow


class User(Base):
    """登录账号与角色（admin / analyst / viewer）。"""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键ID")
    username = Column(String(64), unique=True, nullable=False, index=True, comment="登录账号")
    password_hash = Column(String(255), nullable=False, comment="加密密码")
    role = Column(String(32), nullable=False, comment="角色：admin/analyst/viewer")
    create_time = Column(DateTime, nullable=False, default=utcnow, comment="创建时间")

    data_sources = relationship("DataSource", back_populates="creator")
    datasets = relationship("Dataset", back_populates="creator")
    dashboards = relationship("Dashboard", back_populates="creator")
