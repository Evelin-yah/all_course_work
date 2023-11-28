command = input()
final_info = {}

while command != 'buy':
    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if product not in final_info:
        final_info[product] = 0
    final_info[product] += price*quantity

    command = input()

for key, value in final_info.items():
   print(f'{key} -> {value:.2f}')