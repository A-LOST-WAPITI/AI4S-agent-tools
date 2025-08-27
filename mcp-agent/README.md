# MCP工具生成器 (Beta)

通过对话式交互自动生成符合AI4S-agent-tools规范的MCP服务器。

## 🚀 快速开始

### 安装依赖

```bash
# 在项目根目录安装 ADK
pip install google-adk python-dotenv
```

### 配置环境

创建 `.env` 文件配置 LLM 模型：

```bash
# .env
MODEL=gemini-2.0-flash  # 或其他支持的模型
```

### 使用方法

在 AI4S-agent-tools 根目录运行：

```bash
# 启动交互式 Web 界面
adk web

# 通过对话创建新的 MCP 工具
```

## 工作流程

### 1. 对话收集需求
智能Agent主动询问：
- 工具名称（英文snake_case）
- 功能描述
- 输入参数
- 输出格式
- 依赖库
- 参考资料（可选）

### 2. 生成计划并确认
整理需求为清晰的计划，请求用户确认

### 3. 自动生成MCP服务器
使用内置工具函数生成完整的服务器代码和配置文件

## 架构设计

```
MCP_Agent（单一智能代理）
├── create_server()      # 生成server.py文件
├── create_metadata()    # 生成metadata.json配置
└── create_pyproject()   # 生成pyproject.toml依赖
```

## 文件结构

```
mcp-agent/
├── agent.py           # 主代理定义
├── tools.py           # 工具函数实现
├── prompt.py          # 交互提示词
├── __init__.py        # 模块入口
├── pyproject.toml     # 项目依赖
├── requirements.txt   # Python依赖
└── README.md          # 本文件
```

## 生成的MCP服务器

严格遵循CONTRIBUTING.md规范：

```
servers/your_tool/
├── server.py         # FastMCP服务器，包含parse_args
├── metadata.json     # 元数据配置
├── pyproject.toml    # uv依赖管理
└── README.md         # 使用文档
```

## 配置

创建`.env`文件：

```bash
MODEL=gemini-2.0-flash
```

## License

MIT