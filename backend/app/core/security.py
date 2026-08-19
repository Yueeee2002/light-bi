"""密码哈希工具。JWT 签发将在登录鉴权阶段接入。"""

from passlib.context import CryptContext

# bcrypt 方案；与 requirements 中 bcrypt==4.0.1 配套
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain_password: str) -> str:
    """明文密码转 bcrypt 哈希。"""
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, password_hash: str) -> bool:
    """校验明文密码与哈希是否匹配。"""
    return pwd_context.verify(plain_password, password_hash)
