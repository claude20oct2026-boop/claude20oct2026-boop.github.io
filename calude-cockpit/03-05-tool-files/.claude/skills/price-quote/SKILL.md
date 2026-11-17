---
name: price-quote
description: Makes a price quote for Greenleaf products, with bulk discounts. Use it when someone asks for a quote, an offer or a total price for several Greenleaf products.
---

# Greenleaf price quote

1. Find each product and its quantity in the request.
   Products: Office chair, Printer paper (box), Ink cartridge.
2. Run the script, with one "product=quantity" pair per product:

   uv run ${CLAUDE_SKILL_DIR}/quote.py "Office chair=12" "Printer paper (box)=60"

3. Show the script's table as it is. Never work out the prices yourself.
4. End with one friendly sentence the salesperson can send to the customer.
