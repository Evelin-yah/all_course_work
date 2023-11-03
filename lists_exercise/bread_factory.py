energy = 100
coins = 100

working_day_events = input().split('|')
for event in working_day_events:
    ingredient, number = event.split('-')
    value = int(number)
    if ingredient == 'rest':
        current_energy = energy
        energy += value
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')
    elif ingredient == 'order':
        if energy < 30:
            print(f'You had to rest!')
            energy += 50
            continue
        energy -= 30
        coins += value
        print(f'You earned {value} coins.')
    else:
        if coins <= 0:
            print(f'Closed! Cannot afford {ingredient}.')
            exit()
        print(f'You bought {ingredient}.')
        coins -= value

print('Day completed!')
print(f'Coins: {coins}')
print(f'Energy: {energy}')