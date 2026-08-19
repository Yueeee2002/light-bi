"""看板表 dashboard（画布核心存储）。"""

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.types import JSON

from app.db.base import Base, utcnow


class Dashboard(Base):
    """画布布局、图表配置、筛选配置统一写入 layout_json。"""

    __tablename__ = "dashboard"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    name = Column(String(128), nullable=False, comment="看板名称")
    description = Column(Text, nullable=True, comment="看板描述")
    layout_json = Column(
        JSON,
        nullable=False,
        comment="画布全量配置：组件位置、大小、图表配置、筛选配置",
    )
    is_public = Column(Boolean, nullable=False, default=False, comment="是否公开分享")
    share_token = Column(String(64), unique=True, nullable=True, index=True, comment="唯一分享令牌")
    create_user_id = Column(Integer, ForeignKey("user.id"), nullable=False, comment="创建人")
    create_time = Column(DateTime, nullable=False, default=utcnow, comment="创建时间")

    creator = relationship("User", back_populates="dashboards")
