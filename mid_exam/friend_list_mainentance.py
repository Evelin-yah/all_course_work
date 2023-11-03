blacklisted_names = 0
lost_names = 0

def check_for_blacklist(name):
    for index in range(len(friends_list)):
        if friends_list[index] == name:
            print(f'{friends_list[index]} was blacklisted.')
            friends_list[index] = 'Blacklisted'
            return 1
        else:
            print(f'{name} was not found.')
            return 0

def check_for_lost(index):
    if 0 <= index < len(friends_list):
        if friends_list[index] != 'Blacklisted' and friends_list[index] != 'Lost':
            print(f'{friends_list[index]} was lost due to an error.')
            friends_list[index] = 'Lost'
            return 1
        else:
            return 0

def change_name(index, new_name):
    if 0 <= index < len(friends_list):
        print(f'{friends_list[index]} changed his username to {new_name}.')
        friends_list[index] = new_name

friends_list = input().split(', ')

command = input()

while not command == 'Report':
    current_command = command.split()

    if current_command[0] == 'Blacklist':
        current_name = current_command[1]
        result = check_for_blacklist(current_name)
        blacklisted_names += result

    if current_command[0] == 'Error':
        index = int(current_command[1])
        result = check_for_lost(index)
        lost_names += result

    if current_command[0] == 'Change':
        index = int(current_command[1])
        new_name = current_command[2]
        change_name(index, new_name)

    command = input()

print(f'Blacklisted names: {blacklisted_names}')
print(f'Lost names: {lost_names}')
print(' '.join(friends_list))