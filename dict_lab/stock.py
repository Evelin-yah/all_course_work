products = input().split()
stock = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = products[i + 1]
    stock[key] = int(value)

searched_products = input().split()

for product in searched_products:
    if product not in stock:
        print(f"Sorry, we don't have {product}")
    else:
        print(f"We have {stock[product]} of {product} left")