"""Greenleaf price quote. Usage: uv run quote.py "Office chair=12" "Printer paper (box)=60"
Fictional prices for the Claude Code course. Uses only built-in Python, nothing to install."""
import sys

PRICES = {"Office chair": 189.00, "Printer paper (box)": 32.00, "Ink cartridge": 45.00}
BULK = {"Office chair": (10, 0.10), "Printer paper (box)": (50, 0.15)}  # (minimum quantity, discount)

total = 0.0
print(f"{'Product':<22}{'Qty':>5}{'Price':>10}{'Discount':>10}{'Line total':>12}")
for arg in sys.argv[1:]:
    name, _, qty = arg.partition("=")
    name = name.strip()
    if name not in PRICES or not qty.strip().isdigit():
        sys.exit(f"Can't read '{arg}'. Use names from this list: {', '.join(PRICES)}")
    qty = int(qty)
    minimum, rate = BULK.get(name, (0, 0.0))
    discount = rate if minimum and qty >= minimum else 0.0
    line = qty * PRICES[name] * (1 - discount)
    total += line
    print(f"{name:<22}{qty:>5}{PRICES[name]:>10.2f}{discount:>10.0%}{line:>12.2f}")
print(f"{'Total (USD)':<57}{total:>12.2f}")
