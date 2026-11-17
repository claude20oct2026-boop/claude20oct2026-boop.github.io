"""Greenleaf tools: a small MCP server that lets Claude look up orders and delivery fees.

Fictional practice data for the Claude Code course.
Claude Code starts it for you (see .mcp.json). To start it by hand:
    uv run --python 3.12 --with "mcp[cli]>=2" mcp run server.py
"""
import csv
from pathlib import Path

from mcp.server import MCPServer
from mcp.server.mcpserver.exceptions import ToolError

# 1. Give the server a name. Claude Code shows it in /mcp.
mcp = MCPServer("greenleaf")

ORDERS_FILE = Path(__file__).parent / "orders.csv"
LATE = ("Delivered late", "Delayed")


def load_orders() -> list[dict]:
    """Read orders.csv. The tools below use this; it is not a tool itself."""
    with open(ORDERS_FILE, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# 2. Each @mcp.tool() turns one Python function into one tool.
# 3. The docstring tells Claude what the tool does and when to use it.
# 4. The type hints (order_id: str) tell Claude what to send.
@mcp.tool()
def order_status(order_id: str) -> dict:
    """Look up one Greenleaf order by its number, like GL-1007.
    Returns the customer, items, total, status and promised delivery date."""
    wanted = order_id.strip().upper()
    for order in load_orders():
        if order["order_id"] == wanted:
            return order
    # 5. Raise ToolError for a problem Claude can fix. Claude reads the message and tries again.
    raise ToolError(f"There is no order {wanted}. Order numbers look like GL-1001.")


@mcp.tool()
def late_orders() -> list[dict]:
    """List all Greenleaf orders that are delayed or were delivered late."""
    return [order for order in load_orders() if order["status"] in LATE]


@mcp.tool()
def delivery_fee(order_total_usd: float, express: bool = False) -> dict:
    """Work out Greenleaf's delivery fee for an order.
    Standard delivery costs $8, and is free for orders of $300 or more.
    Express delivery adds $12."""
    if order_total_usd < 0:
        raise ToolError("The order total can't be negative.")
    fee = 0 if order_total_usd >= 300 else 8
    if express:
        fee += 12
    return {"order_total_usd": order_total_usd, "express": express, "delivery_fee_usd": fee}


# 6. Start the server when this file is run.
if __name__ == "__main__":
    mcp.run()
