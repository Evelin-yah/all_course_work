parking_lot_info = {}
commands_given = int(input())
given_data = []

for current_command in range(commands_given):
    given_data = input().split()
    for index in range(0,(len(given_data)), 3):
        if given_data[index] == 'register':
            user, licence_plate = given_data[index+1], given_data[index+2]
            if user not in parking_lot_info:
                parking_lot_info[user] = licence_plate
                print(f'{user} registered {licence_plate} successfully')
            else:
                print(f'ERROR: already registered with plate number {licence_plate}')
        else:
            command, user = given_data[index], given_data[index+1]
            if user not in parking_lot_info:
                print(f'ERROR: user {user} not found')
            else:
                print(f'{user} unregistered successfully')
                del parking_lot_info[user]

for key, value in parking_lot_info.items():
    print(f'{key} => {value}')