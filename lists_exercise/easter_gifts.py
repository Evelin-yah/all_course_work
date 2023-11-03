gifts_given = input().split()
command = input()
while command != 'No Money':
    current_command = command.split()
    current_gift = current_command[1]
    if current_command[0] == 'OutOfStock':
        for index in range(len(gifts_given)):
            if gifts_given[index] == current_gift:
                gifts_given[index] = 'None'
    elif current_command[0] == 'Required':
        index = int(current_command[2])
        if 0 <= index < len(gifts_given):
            gifts_given[index] = current_gift
    elif current_command[0] == 'JustInCase':
        gifts_given[-1] = current_gift
    command = input()

for gift in gifts_given:
    if gift != 'None':
        print(gift, end=' ')