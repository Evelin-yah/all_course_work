def deleting_message(message):
    for index in range(len(list_of_messages)):
        if list_of_messages[index] == message.:
            list_of_messages.remove(message)
        else:
            break
def pinned_message(message):
    for index in range(len(list_of_messages)):
        if list_of_messages[index] == message:
            list_of_messages.insert(-1, list_of_messages[index])
        else:
            break
def edit_message(message):
    for index in range(len(list_of_messages)):
        if list_of_messages[index] == message:
            list_of_messages[index] = message


list_of_messages = []
command = input()

while command != "end":
    current_command = command.split()
    if current_command[0] == 'Chat':
        message = current_command[1]
        list_of_messages.append(message)

    if current_command[0] == 'Delete':
        message = current_command[1]
        deleting_message(message)

    if current_command[0] == 'Edit':
        message = current_command[1]
        edit_message(message)

    if current_command[0] == 'Pin':
        message = current_command[1]
        pinned_message(message)

    if current_command[0] == 'Spam':

        for i in range (1, len(current_command)):
            list_of_messages.append(current_command[i])

    command = input()
print('\n'.join(list_of_messages))