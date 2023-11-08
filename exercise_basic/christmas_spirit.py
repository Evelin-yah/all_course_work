quantity_of_decor = int(input())
remaining_days = int(input())

money_spend = 0
spirit = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

for current_day in range (1, remaining_days + 1):
    if current_day % 11 == 0:
        quantity_of_decor += 2
    if current_day % 2 == 0:
        money_spend += ornament_set_price * quantity_of_decor
        spirit += 5
    if current_day % 3 == 0:
        money_spend += (tree_skirt_price + tree_garland_price) * quantity_of_decor
        spirit += 13
    if current_day % 5 == 0:
        money_spend += tree_lights_price * quantity_of_decor
        spirit += 17
        if current_day % 3 == 0:
            spirit += 30
    if current_day % 10 == 0:
        spirit -= 20
        money_spend += tree_skirt_price + tree_garland_price + tree_lights_price

if remaining_days % 10 == 0:
    spirit -= 30

print(f'Total cost: {money_spend}')
print(f'Total spirit: {spirit}')