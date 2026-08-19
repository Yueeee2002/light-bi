"""统一 API 返回体：{ code, message, data }。"""

from typing import Any, Generic, Optional, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    """前后端约定的统一响应结构。"""

    code: int = Field(0, description="业务状态码，0 表示成功")
    message: str = Field("success", description="提示信息")
    data: Optional[T] = Field(None, description="业务数据")


def success(data: Any = None, message: str = "success") -> dict[str, Any]:
    """成功响应。"""
    return {"code": 0, "message": message, "data": data}


def fail(message: str = "error", code: int = 400, data: Any = None) -> dict[str, Any]:
    """失败响应（配合 HTTP status 由异常处理器返回）。"""
    return {"code": code, "message": message, "data": data}
