items = input().split("|")
budget = float(input())

MAX_CLOTHES_PRICE = 50.00
MAX_SHOES_PRICE = 35.00
MAX_ACCESSORIES_PRICE = 25.00

bought_items = []
overall_profit = 0

for item in items:
    item_type, item_price = item.split("->")
    item_price = float(item_price)
    if item_type == "Clothes" and item_price > MAX_CLOTHES_PRICE:
        continue
    elif item_type == "Shoes" and item_price > MAX_SHOES_PRICE:
        continue
    elif item_type == "Accessories" and item_price > MAX_ACCESSORIES_PRICE:
        continue

    if budget >= item_price:
        budget -= item_price
        current_profit = item_price * 0.40
        overall_profit += current_profit
        bought_items.append(item_price + current_profit)

for el in bought_items:
    print(f"{el:.2f}", end=' ')
print()
print(f"Profit: {overall_profit:.2f}")
budget += sum(bought_items)
if budget >= 150:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")