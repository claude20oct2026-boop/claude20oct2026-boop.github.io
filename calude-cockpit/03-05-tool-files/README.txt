Practice files for "Build your own tool" (lesson one, topic 3.5).
Everything here is fictional: Greenleaf Office Supplies is a made-up company.

You need uv, a small free program that runs Python for you.
Install it once, then restart VS Code:
  Windows (PowerShell):  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  Mac:                   curl -LsSf https://astral.sh/uv/install.sh | sh

orders.csv                          20 Greenleaf orders, with status and promised date
server.py                           the custom tool: an MCP server with 3 tools (order_status, late_orders, delivery_fee)
.mcp.json                           tells Claude Code how to start server.py
.claude/skills/price-quote/         a skill with a Python script (the other way to build a tool)

Open this folder in VS Code. Claude Code asks you to approve the "greenleaf" server.
Then type /mcp to check it is connected.
The first start can take a minute, while uv downloads Python and the MCP package.
