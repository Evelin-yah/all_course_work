list_number = input().split()
absolute_values = []

for number in list_number:
    absolute_values.append(abs(float(number)))

print(absolute_values)