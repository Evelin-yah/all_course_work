money_as_str = input().split(', ')
number_of_beggars = int(input())
money = []

for i in money_as_str:
    money.append(int(i))

final_sums = []
start_index = 0

while start_index < number_of_beggars:
    current_beg_sum = 0
    for current_index in range(start_index, len(money), number_of_beggars):
        current_beg_sum += money[current_index]
    final_sums.append(current_beg_sum)
    start_index += 1
print(final_sums)