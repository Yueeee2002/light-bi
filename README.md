# Light-BI 轻量自助 BI 看板平台

面向企业内部分析师的轻量化自助 BI 可视化平台（MVP）。  
技术栈：**Next.js 14 App Router + Ant Design v5 + Recharts + react-grid-layout + Zustand + FastAPI + SQLAlchemy + SQLite**。

> 当前进度：**阶段 1 — 脚手架初始化**（框架 / ORM / 种子数据）。业务接口与页面按阶段迭代，尚未实现。

## 功能范围（MVP）

- 角色权限：admin / analyst / viewer（后端二次校验）
- 数据源：内置 Mock + CSV 上传（≤5MB，UTF-8 / GBK）
- 数据集：字段别名、过滤配置（JSON 存储）
- 拖拽画布：柱状图 / 折线图 / 饼图 / 表格，布局 JSON 持久化
- 看板只读分享 + PDF 导出

二期能力（多数据源、AI 问答、下钻等）不在本仓库 MVP 范围内。

## 仓库结构

```text
light-bi/
├── backend/                     # FastAPI 后端
│   ├── app/
│   │   ├── main.py              # 应用入口：CORS / 统一异常 / 探活
│   │   ├── api/                 # 业务路由（阶段2起填充）
│   │   ├── core/
│   │   │   ├── config.py        # 配置
│   │   │   ├── constants.py     # 角色 / 数据源类型常量
│   │   │   ├── security.py      # 密码哈希
│   │   │   ├── response.py      # 统一返回体 {code, message, data}
│   │   │   └── exceptions.py    # 全局异常捕获
│   │   ├── db/
│   │   │   ├── base.py          # SQLAlchemy Base
│   │   │   ├── session.py       # Engine / Session / get_db
│   │   │   └── init_db.py       # 建表 + 种子账号
│   │   ├── models/              # user / data_source / dataset / dashboard
│   │   └── schemas/             # Pydantic Schema
│   ├── data/                    # SQLite 文件目录（*.db 不入库）
│   ├── scripts/init_db.py       # 独立初始化脚本
│   ├── requirements.txt
│   └── run.py
├── frontend/                    # Next.js 14 App Router
│   ├── app/                     # 路由（阶段1仅占位页）
│   ├── components/providers/    # Ant Design 注册
│   ├── lib/request.ts           # axios 封装
│   ├── store/useAppStore.ts     # Zustand 全局状态
│   └── types/
├── docs/                        # PRD / 表结构 / API 清单
└── README.md
```

## 环境要求

- Node.js 18+（推荐 20 / 22）
- Python 3.11+（当前开发环境为 3.12）
- npm

## 后端启动

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 建表并写入测试账号（应用启动时也会自动执行）
python -m app.db.init_db
# 或：python scripts/init_db.py

python run.py
# 等价：uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- 探活：<http://localhost:8000/health>
- Swagger：<http://localhost:8000/docs>

### 内置测试账号

| 用户名 | 密码 | 角色 |
| --- | --- | --- |
| admin | 123456 | admin |
| analyst | 123456 | analyst |
| viewer | 123456 | viewer |

### 后端依赖

`fastapi`、`uvicorn`、`sqlalchemy`、`pydantic`、`python-jose[cryptography]`、`passlib[bcrypt]`、`python-multipart`、`charset-normalizer`（另锁定 `bcrypt==4.0.1` 以避免与 passlib 不兼容）。

## 前端启动

```bash
cd frontend
cp .env.example .env.local         # 默认 API: http://localhost:8000
npm install
npm run dev
```

浏览器打开 <http://localhost:3000>。

### 前端依赖

`next@14`、`antd`、`recharts`、`react-grid-layout`、`zustand`、`axios`、`html2pdf.js`、`@ant-design/nextjs-registry`、`@types/react-grid-layout`。

## 数据库初始化说明

- 引擎：SQLite，文件位于 `backend/data/light_bi.db`
- 四张表：`user`、`data_source`、`dataset`、`dashboard`（字段见 [docs/DATABASE.md](docs/DATABASE.md)）
- 画布布局、图表配置、字段过滤一律以 JSON 列持久化
- 启动 FastAPI 时 `lifespan` 会 `create_all` 并补齐缺失的种子用户

手动初始化：

```bash
cd backend && source .venv/bin/activate
python -m app.db.init_db
```

## 阶段计划

1. **脚手架初始化**（本阶段）
2. 登录鉴权
3. 数据源 / 数据集
4. 看板画布核心
5. 分享导出
6. 自测联调

业务 API 清单见 [docs/API.md](docs/API.md)。
