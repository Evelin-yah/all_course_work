money_per_search = float(input())
number_of_users = int(input())
total_money = 0

for user in range(number_of_users):
    number_of_searches = int(input())
    money_earned = money_per_search * number_of_searches
    if number_of_searches > 5 and (user+1) % 3 != 0:
        money_earned *= 2
    if number_of_searches <= 1:
        money_earned -= (money_per_search * number_of_searches)
    if user != 0 and (user + 1) % 3 == 0:
        money_earned *= 3
        if number_of_searches > 5:
            money_earned *= 2

    total_money += money_earned


print(f'Total money earned: {total_money:.2f}')
