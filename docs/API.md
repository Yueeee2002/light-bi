# API 接口清单（RESTful · MVP）

统一返回体：

```json
{ "code": 0, "message": "success", "data": {} }
```

> 阶段 1 仅提供 `GET /health` 探活，下列业务接口从阶段 2 起按模块实现。

## 1. 登录鉴权模块

- `POST /api/auth/login` — 用户登录、返回 JWT
- `GET /api/auth/info` — 获取当前登录用户信息、角色

## 2. 数据源模块

- `GET /api/datasource/list` — 数据源列表
- `POST /api/datasource/create` — 新建 Mock/CSV 数据源
- `POST /api/datasource/upload-csv` — 上传解析 CSV
- `DELETE /api/datasource/delete` — 删除数据源

## 3. 数据集模块

- `GET /api/dataset/list` — 数据集列表
- `POST /api/dataset/create` — 新建数据集
- `POST /api/dataset/update` — 编辑数据集
- `DELETE /api/dataset/delete` — 删除数据集
- `POST /api/dataset/preview` — 预览数据集加工后数据

## 4. 看板模块

- `GET /api/dashboard/list` — 看板列表
- `POST /api/dashboard/create` — 新建看板
- `POST /api/dashboard/save-layout` — 保存画布 JSON 布局
- `GET /api/dashboard/detail` — 获取看板详情与布局
- `DELETE /api/dashboard/delete` — 删除看板
- `POST /api/dashboard/generate-share` — 生成分享 token
- `GET /api/dashboard/share` — 公开分享看板数据（免登）

## 5. 数据查询核心接口

- `POST /api/query/chart-data` — 根据数据集 + 筛选条件返回图表数据
