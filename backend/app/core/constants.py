"""角色常量，后续接口二次校验使用。"""

class UserRole:
    ADMIN = "admin"
    ANALYST = "analyst"
    VIEWER = "viewer"

    ALL = (ADMIN, ANALYST, VIEWER)


class DataSourceType:
    MOCK = "mock"
    CSV = "csv"

    ALL = (MOCK, CSV)
