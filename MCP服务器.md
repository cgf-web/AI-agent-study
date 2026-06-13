## MCP服务器（Model Context Protocol Server）是由 Anthropic 主导的模型上下文协议的服务端实现，核心是给大模型 / Agent 提供标准化、安全可控的外部数据与工具调用能力。

### 一、核心定位

- **本质**：AI 与外部世界（数据库、文件、API、硬件）之间的**中间件 / 代理层**。
- **作用**：让大模型不用直接连复杂系统，通过统一协议 “安全、可控、标准化” 地读数据、调工具。
- **类比**：大模型是 “大脑”，MCP Server 是 “手脚 + 翻译官”，负责对外干活并把结果转成模型能懂的语言。

### 二、协议与架构

- **协议**：MCP（Model Context Protocol），基于 **JSON‑RPC 2.0**，用 **SSE/HTTP/stdio** 传输。
- **三大角色**：
    
    - **Host（客户端 / Agent）**：大模型所在环境（如 Claude、自定义 Agent），发起调用。
    - **MCP Server（服务端）**：暴露工具与数据，执行实际操作（查库、读文件、调 API）。
    - **Transport（传输层）**：连接通道，常用 **SSE（服务器推）+ HTTP POST（客户端请求）**。
    

### 三、核心能力

1. **数据连接**：访问数据库、知识库、CRM、ERP 等。
2. **工具调用**：调用第三方 API（天气、支付、地图）、本地脚本、浏览器自动化。
3. **文件操作**：读写本地 / 服务器文件、代码仓库、文档库。
4. **上下文增强**：注入实时数据（库存、订单、用户历史），提升回答准确性。
5. **安全隔离**：模型不直连敏感系统，权限、审计、限流都在 Server 控制。

### 四、工作流程（四步）

1. **连接握手**：Host 连 Server，协商能力与权限。
2. **发现工具**：Host 拉取 Server 提供的工具列表（名称、参数、描述）。
3. **调用工具**：Host 发 `tools/call` 请求（工具名 + 参数）。
4. **返回结果**：Server 执行后返回结构化 JSON 结果，Host 喂给模型生成回答。

### 五、常见类型（开箱即用）

- **文件类**：本地文件读写、Git 仓库操作。
- **数据库类**：MySQL、PostgreSQL、SQLite 查询 / 写入。
- **Web 类**：网页抓取、搜索、API 代理。
- **开发工具类**：代码执行、终端命令、CI/CD 集成。
- **企业系统类**：ERP、CRM、OA 适配器。

==MCP Server 就是大模型的 “万能插件总线”，用一套标准把所有外部系统变成模型可安全调用的工具，彻底解决 “大模型只会说、不会干” 的问题。==

## Agent SDK（智能体软件开发工具包） 是一套帮你快速构建、部署、管理 AI Agent 的工具库与运行时，核心是把 “模型调用→工具执行→状态记忆→多步循环→多智能体协作” 的底层逻辑封装好，让你不用从零写复杂流程。

### 一、它解决什么问题？

直接调用 LLM API 只能做 “一问一答”，而 Agent SDK 帮你做：

- **自主决策**：模型自己想 “下一步该做什么工具”
- **多步循环**：任务没完成就继续调用工具，直到结束
- **工具互联**：统一对接数据库、文件、API、MCP Server
- **记忆与状态**：记住上下文、历史、中间结果
- **安全沙箱**：防止恶意代码 / 越权操作
- **多智能体协作**：多个 Agent 分工合作（如产品、开发、测试）

一句话：**LLM 是大脑，Agent SDK 是手脚 + 神经中枢 + 安全护栏**。

---

### 二、主流 Agent SDK（2026）

#### 1. OpenAI Agents SDK（2025.3 推出）

- 特点：官方轻量、极简 API、内置沙箱、可视化调试、自动对话管理
- 核心能力：`Response API`（统一聊天 / 工具）、智能体交接、代码解释器、搜索 / 文件工具
- 优势：上手最快（4 行代码）、生态无缝、安全护栏完善
- 劣势：偏 OpenAI 生态、定制化有限
- 适合：原型验证、客服 / 运营、快速上线

python

运行

```
# 极简示例（伪代码）
from openai import AgentsSDK

agent = AgentsSDK.create_agent(
    model="gpt-5",
    instructions="你是数据分析师，能查数据库并出报告",
    tools=["sql_query", "file_write"]
)
agent.run("分析6月销量并生成PDF")
```

#### 2. Claude Agent SDK（Anthropic）

- 特点：强安全、原生支持 **MCP 协议**、长文本 / 长任务友好
- 核心能力：MCP Server 对接、工具循环、沙箱执行、企业级权限审计
- 优势：安全可控、MCP 生态最佳、适合企业内部系统
- 适合：企业自动化、内部工具、需要强安全合规

#### 3. mcp-agent（LastMile AI）

- 特点：**MCP 优先**、纯代码编排（非图）、轻量灵活
- 理念：“写代码，不画流程图”，用 `if/while/函数` 组织工作流
- 核心模式：Orchestrator、Evaluator-Optimizer、Router、Map-Reduce
- 适合：技术团队、复杂动态流程、深度定制 MCP 工具链

#### 4. LangGraph（LangChain）

- 特点：图状编排、状态管理极强、生态最大、多模型兼容
- 优势：最成熟、可控性高、适合超长复杂任务
- 劣势：学习曲线陡、代码量较大

#### 5. AutoGen（微软）

- 特点：多智能体对话协作、角色分工、群聊式任务推进
- 适合：创意类、需要多轮讨论的任务（如软件开发、内容创作）

---

### 三、Agent SDK vs 普通 LLM API

表格

|能力|普通 LLM API|Agent SDK|
|---|---|---|
|交互模式|一问一答（无状态）|多步循环（有状态）|
|工具调用|需手动写循环|内置自动循环|
|记忆|需自己维护上下文|内置记忆 / 状态管理|
|安全|无沙箱，风险高|沙箱 + 权限 + 审计|
|多智能体|不支持|原生支持协作|

---

### 四、Agent SDK 与 MCP Server 的关系（重点）

- **MCP Server**：是 “工具提供者”，暴露数据库 / 文件 / API 给外部
- **Agent SDK**：是 “智能体运行时”，负责**调用 MCP Server**、做决策、循环执行
- 组合：**Agent SDK → MCP Client → MCP Server → 外部系统**

一句话：**MCP 是工具协议，Agent SDK 是用这个协议的智能体框架**。

---

### 五、什么时候用 Agent SDK？

- ✅ 任务需要**多步骤、多工具**（如 “查数据→分析→生成报告→发邮件”）
- ✅ 需要**自主决策**，不是固定流程
- ✅ 要对接**数据库 / 文件 / 内部系统**
- ✅ 追求**安全、可观测、可审计**
- ✅ 想做**多智能体协作**

# FastAPI 讲解

**FastAPI** 是 Python 高性能 Web 框架，专门用来**快速写接口、服务、后端**，现在大量用来做：MCP Server、Agent 后端、LLM 接口、工具服务。

## 一、核心特点

1. **快**：基于 Starlette + Pydantic，性能接近 Go/Node
2. **自动接口文档**：写完代码自动生成 `Swagger UI` / `ReDoc`，不用手写文档
3. **类型提示强**：自动参数校验、报错友好
4. **异步优先**：原生 `async/await`，适合 IO 密集（调用 LLM、数据库、网络请求）
5. **上手极快**：代码简洁





### **Pydantic v2 是 Python 数据验证 / 序列化库，核心用 Rust 重写，比 v1 快 5–50 倍，是 FastAPI、AI Agent、MCP Server 的标配数据层。**Pydantic

下面从定位、核心新特性、与 FastAPI/Agent 的结合、迁移要点、完整示例几方面讲。

## 一、定位：解决什么问题

Python 是动态类型，API / 工具调用时经常遇到：

- 数据类型乱（字符串当数字、null 漏传）
- 嵌套结构难校验
- 错误信息不清晰
- 序列化 / 反序列化繁琐

**Pydantic = 用 Python 类型注解写 “数据规则”，自动校验、转换、报错、序列化。**

v2 直接把核心逻辑用 Rust 实现，性能质变。

---

## 二、v2 核心新特性（必懂）

### 1. 🚀 性能爆炸（最大亮点）

- 底层：**pydantic-core（Rust）** 做校验 / 解析
- 速度：比 v1 **快 5–50 倍**，常规场景约 17 倍Pydantic
- 高并发 API、AI 批量数据处理首选

### 2. ✅ 更严格的类型安全（Strict Mode）

- 默认不再隐式强转（如 `'1'` → `1`、`'true'` → `True`）
- 要转换需显式声明（如 `int | str`）
- 减少 “静默错误”，适合金融 / AI 推理场景

### 3. 🧩 全新验证器 API（替代 v1 旧装饰器）

- `@field_validator`：字段级校验（替代 `@validator`）Pydantic
- `@model_validator`：模型级 / 跨字段校验（替代 `@root_validator`）Pydantic
- `@computed_field`：动态计算字段（如 `full_name = first + last`）

### 4. 📦 序列化升级（model_dump /model_dump_json）

- `model_dump()` → 字典（替代 `dict()`）
- `model_dump_json()` → JSON 字符串（替代 `json()`）
- 支持：排除字段、别名、深度嵌套、多态序列化Pydantic

### 5. 🛠 实用新工具

- **TypeAdapter**：任意类型校验（不用写 BaseModel）Pydantic
- **@validate_call**：直接校验函数参数
- **pydantic-settings**：独立配置管理（原 `BaseSettings`）

---

## 三、与 FastAPI / Agent / MCP 的关系（重点）

### 1. FastAPI + Pydantic v2 = 官方黄金组合

- FastAPI ≥ 0.95 **默认强制依赖 v2**
- 自动做：
    
    - 请求体 / 参数校验（422 错误）
    - 自动生成 OpenAPI 文档
    - 响应序列化（`response_model`）
    

### 2. Agent SDK / MCP Server 必备

- **Agent 侧**：校验 LLM 输出、工具调用参数、记忆结构
- **MCP Server（FastAPI）**：校验工具请求、数据库参数、文件路径
- 链路：
    
    `Agent → Pydantic 校验 → FastAPI(MCP) → Pydantic 校验 → 工具/数据库`



### 结合你前面的 **FastAPI + Pydantic v2 + Agent/MCP** 技术栈，下面讲解 **PostgreSQL + asyncpg 异步操作**。

# 一、基础介绍

- **asyncpg**：Python 目前**最快的异步 PostgreSQL 驱动**，纯异步实现，不依赖线程池，适配 `async/await`，是 FastAPI 异步项目首选。
- 对比：同步驱动 `psycopg2` 会阻塞事件循环，高并发接口、AI 服务严禁使用。
- 适配场景：MCP 服务查库、Agent 读写业务数据、会话记忆存储、日志存储。
# 二、核心概念

1. **连接池（Pool）**
    
    不要每次请求新建连接，统一用**连接池**复用连接，提升并发性能，这是生产必备。
2. 全异步语法：所有数据库操作都加 `await`。
3. 配合 Pydantic：查询结果自动映射为模型，做数据校验。



# 一、JWT 基础

**JWT（JSON Web Token）**：无状态身份令牌，用于接口登录、权限校验。

- 结构：`头部.载荷.签名`，三段 Base64 字符串
- 特点：**服务端不存会话**，客户端持有令牌，适合分布式 / API/Agent 服务
- 用途：MCP Server、Agent 接口做登录、接口访问鉴权

### 核心流程

1. 用户登录 → 服务端校验账号密码 → 生成 JWT 返回客户端
2. 客户端后续请求在请求头携带 `Authorization: Bearer <token>`
3. 服务端解析、验签、判断是否过期 → 放行 / 拒绝访问





结合你现有栈（FastAPI + JWT + asyncpg + Pydantic v2），实现**Access Token + Refresh Token 双令牌刷新机制**，解决短期访问令牌过期、免重复登录的问题。

# 一、机制说明

1. **Access Token（访问令牌）**
    
    有效期短（5~30 分钟），用于日常接口鉴权，泄露风险低。
2. **Refresh Token（刷新令牌）**
    
    有效期长（7 天 / 30 天），**仅用于换新 Access Token**，不用来访问业务接口。
3. 流程
    
    - 登录：同时返回 `access_token` + `refresh_token`
    - Access 过期：客户端用 `refresh_token` 调用刷新接口，获取新 `access_token`
    - Refresh 过期：强制重新登录
    
4. 实现要点：**Refresh Token 存入 PostgreSQL**（服务端留存，支持吊销、下线）





结合你 **FastAPI + 异步 PG + JWT** 技术栈，讲解**API 密钥（API Key）**，包含两种主流用法、数据库存储、鉴权、和 JWT 混用、完整可运行代码，适配 MCP/Agent 服务场景。

---
## 一、API Key 基础

### 1. 是什么

一串随机字符串，作为**接口访问凭证**，多用于：

- 服务间调用、第三方系统对接
- 机器人、脚本、Agent、MCP 客户端鉴权
- 区别于人账号登录（JWT 面向用户，API Key 面向程序 / 服务）
## #2.常见传递方式（FastAPI 主流两种）
1.请求头（推荐，标准做法）
2.**URL 查询参数**（简单但不安全，日志会泄露
3.和 JWT 区别
![[Pasted image 20260613231431.png]]



结合你 **FastAPI + asyncpg + JWT + API Key** 全栈，这里讲解 **Redis + 异步客户端 aioredis**，聚焦实战场景：缓存、令牌黑名单、限流、会话存储、热点数据加速，附完整可运行代码。

# 一、基础说明

- **Redis**：高性能内存数据库，主打**缓存、计数、分布式锁、临时数据**。
- **aioredis**：Python 官方推荐**异步 Redis 客户端**，完美适配 FastAPI 异步链路，不阻塞事件循环。
- 你的业务适用场景：
    1. JWT / Refresh Token 黑名单（注销、强制下线）
    2. API Key 高频校验缓存（减轻 PostgreSQL 压力）
    3. 接口限流（防刷、防暴力请求）
    4. 热点数据缓存（配置、字典、常用查询结果）
    5. 会话 / 临时状态存储

# 二、1. 全局异步 Redis 连接（单例连接池）

生产必须用**连接池**，不要每次请求新建连接。
### 三、2. 常用基础命令（异步） 
全部加 await，常用读写、过期、删除：




## 一、LangGraph 是什么（一句话）

**LangGraph = 用 “图” 来编排有状态、可循环、可分支的 LLM 工作流 / Agent**。

- 传统 LangChain：链式、线性、状态难管理
- LangGraph：**状态 (State) + 节点 (Node) + 边 (Edge)**，支持循环、分支、记忆、人在回路LangGraph

**适合做：**

- 对话 Agent（带记忆）
- 工具调用 Agent（ReAct 循环）
- 多步骤任务（规划→执行→反思→修正）
- 多智能体协作

---
## 二、核心三要素（必懂）

### 1. State（状态）

全局共享上下文，所有节点读写同一份状态。用 `TypedDict` 定义LangGraph：

### 2. Node（节点）

一个函数，**输入 State → 做一件事 → 返回 State 更新（增量）**：

### 3.Edge（边） 
定义下一步去哪： 普通边：固定跳转（A→B） 条件边：根据状态分支（如 “需要工具”→工具节点，否则→结束）LangGraph



# 一、pgvector 简介

`pgvector` 是 PostgreSQL 开源扩展，让数据库原生支持**向量数据类型、向量索引、相似度查询**。

- 优势：不用额外部署独立向量库（Milvus/FAISS），一套 PG 同时存业务数据 + 向量，运维简单
- 适配场景：RAG 知识库、语义检索、记忆向量、文档问答（LangGraph Agent 常用）
- 支持距离计算：余弦相似度、欧氏距离、点积

## 核心概念

1. `vector(n)`：向量字段类型，`n` 代表向量维度（OpenAI `text-embedding-3-small` 维度 1536）
2. 向量索引：加速检索（IVFFlat、HNSW，海量数据必建）
3. 相似度查询：按向量距离排序，召回相似文本



# 一、Celery 核心简介

Celery 是 Python 主流**分布式任务队列**，用来解耦耗时操作：

- 适用场景：大文件解析、长文本向量化、批量向量入库、邮件推送、日志归档、报表生成、模型推理（耗时任务）
- 架构角色：
    
    1. **生产者 (Producer)**：FastAPI 接口触发任务，下发任务消息
    2. **Broker (消息代理)**：中转任务，这里用 **Redis**（你已部署），也可用 RabbitMQ
    3. **Worker (工作进程)**：常驻后台，消费并执行任务
    4. **Backend (结果存储)**：保存任务执行结果、状态，一般复用 Redis/PostgreSQL
    

### 为什么在你的栈里要用？

- 向量批量导入、大文档切片向量化：耗时久，不能阻塞 FastAPI 接口
- LangGraph 复杂 Agent 流程、长任务推理：丢到后台执行
- 定时巡检、数据同步、过期数据清理：定时任务能力





结合你后端全栈（FastAPI / PG /pgvector/ Redis / Celery / LangGraph / JWT/API Key），讲解 **Next.js 15 + React 19 + Tailwind CSS v4** 前端技术栈，聚焦**项目搭建、核心特性、前后端联调、AI/Agent 业务落地、工程化最佳实践**，附可直接上手代码。

# 一、技术栈整体定位

- **Next.js 15**：React 全栈框架，App Router 为主流，支持服务端组件 (RSC)、服务端动作 (Server Actions)、API 路由、静态 / 动态渲染，适配前后端分离 + 同构渲染。
- **React 19**：底层更新，简化数据请求、异步组件、表单处理、优化渲染性能，和 Next 15 深度绑定。
- **Tailwind CSS v4**：全新引擎，速度更快、体积更小、配置简化，原子化 CSS，快速写界面，适配后台管理、AI 对话、知识库页面。

**适配你的业务场景**：

AI 对话界面、RAG 知识库管理、API Key / 用户权限后台、任务进度展示（Celery 任务）、向量文档管理。
