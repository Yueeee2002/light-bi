"""数据集表 dataset（BI 加工层）。"""

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import JSON

from app.db.base import Base, utcnow


class Dataset(Base):
    """字段别名、启用状态与过滤条件，均以 JSON 持久化。"""

    __tablename__ = "dataset"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    name = Column(String(128), nullable=False, comment="数据集名称")
    source_id = Column(Integer, ForeignKey("data_source.id"), nullable=False, comment="关联数据源ID")
    fields_config = Column(JSON, nullable=False, comment="字段配置：是否启用、别名、注释")
    filter_config = Column(JSON, nullable=True, comment="过滤条件配置")
    create_user_id = Column(Integer, ForeignKey("user.id"), nullable=False, comment="创建人")
    create_time = Column(DateTime, nullable=False, default=utcnow, comment="创建时间")

    source = relationship("DataSource", back_populates="datasets")
    creator = relationship("User", back_populates="datasets")
