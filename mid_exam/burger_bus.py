cities_visited = int(input())

profit = 0
counter = 0
for city in range(cities_visited):
    name_of_city = input()
    money_earned = float(input())
    expenses = float(input())
    counter += 1
    current_expenses = expenses

    if counter % 3 == 0:
        current_expenses += expenses / 2
    if counter % 5 == 0:
        current_expenses += money_earned * 0.1
    if counter % 3 == 0 and counter % 5 == 0:
        current_expenses += expenses / 2
        current_expenses += money_earned * 0.1

    current_profit = money_earned - current_expenses
    profit += current_profit

    print(f'In {name_of_city} Burger Bus earned {current_profit:.2f} leva.')

print(f'Burger Bus total profit: {profit:.2f} leva.')