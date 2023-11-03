def calculate_orders(product, quantity):

    return {
        'coffee': 1.50 * quantity,
        'water': 1.00 * quantity,
        'coke': 1.40 * quantity,
        'snacks': 2.00 * quantity
    }.get(product)


product = input()
quantity = int(input())

result = calculate_orders(product, quantity)
print(f'{result:.2f}')
