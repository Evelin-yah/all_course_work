number_of_orders = int(input())
price = 0
total_price = 0

for order in range (number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed = int(input())

    if not 0.01 <= price_per_capsule <= 100.00 or not 1 <= days <= 31 or not 1 <= capsules_needed <= 2000:
        continue
    # if not 1 <= days <= 31:
    #     continue
    # if not 1 <= capsules_needed <= 2000:
    #     continue
    price += (price_per_capsule * days) * capsules_needed
    print(f"The price for the coffee is: ${price:.2f}")
    price = 0
    total_price += (price_per_capsule * days) * capsules_needed

print(f"Total: ${total_price:.2f}")