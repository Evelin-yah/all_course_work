year = int(input())
is_special = False

while not is_special:
    year += 1
    year_as_str = str(year)
    is_special = True
    for digit in year_as_str:
        if year_as_str.count(digit) != 1:
            is_special = False
            break

print(year)