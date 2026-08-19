# 数据库设计（MVP · 4 张核心表）

数据库：SQLite  
ORM：SQLAlchemy  
存储核心：用户权限、数据源、数据集、看板布局与配置 JSON

## 1. 用户表 `user`

| 字段名 | 类型 | 说明 | 约束 |
| --- | --- | --- | --- |
| id | int | 主键 ID | 自增、唯一 |
| username | varchar | 登录账号 | 唯一、非空 |
| password_hash | varchar | 加密密码 | 非空 |
| role | varchar | 角色：admin / analyst / viewer | 非空 |
| create_time | datetime | 创建时间 | 默认当前时间 |

## 2. 数据源表 `data_source`

| 字段名 | 类型 | 说明 | 约束 |
| --- | --- | --- | --- |
| id | int | 主键 | 自增 |
| name | varchar | 数据源名称 | 非空 |
| type | varchar | 类型：mock / csv | 非空 |
| data_json | json | 存储解析后的完整数据 | 非空 |
| create_user_id | int | 创建人 ID | 外键关联 user |
| create_time | datetime | 创建时间 | 默认当前时间 |

## 3. 数据集表 `dataset`（BI 核心加工层）

| 字段名 | 类型 | 说明 | 约束 |
| --- | --- | --- | --- |
| id | int | 主键 | 自增 |
| name | varchar | 数据集名称 | 非空 |
| source_id | int | 关联数据源 ID | 外键 |
| fields_config | json | 字段配置：是否启用、别名、注释 | 非空 |
| filter_config | json | 过滤条件配置 | 可为空 |
| create_user_id | int | 创建人 | 非空 |
| create_time | datetime | 创建时间 | 默认当前时间 |

## 4. 看板表 `dashboard`（画布核心存储）

| 字段名 | 类型 | 说明 | 约束 |
| --- | --- | --- | --- |
| id | int | 主键 | 自增 |
| name | varchar | 看板名称 | 非空 |
| description | text | 看板描述 | 可为空 |
| layout_json | json | 画布全量配置：组件位置、大小、图表配置、筛选配置 | 非空 |
| is_public | boolean | 是否公开分享 | 默认 false |
| share_token | varchar | 唯一分享令牌 | 唯一 |
| create_user_id | int | 创建人 | 非空 |
| create_time | datetime | 创建时间 | 默认当前时间 |
