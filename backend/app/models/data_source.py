"""数据源表 data_source。"""

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import JSON

from app.db.base import Base, utcnow


class DataSource(Base):
    """Mock / CSV 数据源，解析后的完整数据存入 data_json。"""

    __tablename__ = "data_source"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    name = Column(String(128), nullable=False, comment="数据源名称")
    type = Column(String(32), nullable=False, comment="类型：mock / csv")
    data_json = Column(JSON, nullable=False, comment="存储解析后的完整数据")
    create_user_id = Column(
        Integer,
        ForeignKey("user.id"),
        nullable=False,
        comment="创建人ID",
    )
    create_time = Column(DateTime, nullable=False, default=utcnow, comment="创建时间")

    creator = relationship("User", back_populates="data_sources")
    datasets = relationship("Dataset", back_populates="source")
