"""
Light-BI FastAPI 入口：CORS、统一异常、启动时建表。
本阶段不注册业务路由，仅提供健康检查便于脚手架自测。
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.exceptions import register_exception_handlers
from app.core.response import success
from app.db.init_db import init_db


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """应用启动时自动建表并写入种子账号。"""
    init_db()
    yield


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="轻量自助 BI 看板平台（MVP）",
    lifespan=lifespan,
)

# 全局 CORS，允许前端本地开发源跨域携带鉴权头
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handlers(app)


@app.get("/health", tags=["system"])
def health_check():
    """脚手架探活，不属于业务 API 清单。"""
    return success(
        data={
            "name": settings.APP_NAME,
            "version": settings.APP_VERSION,
        }
    )
