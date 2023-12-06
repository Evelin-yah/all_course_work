text = input()
command = input()

while command != 'End':
    if 'Translate' in command:
        current_command, char, replacement = command.split()
        text = text.replace(char, replacement)
        print(text)
    if 'Includes' in command:
        current_command, substring = command.split()
        if substring in text:
            print(True)
        else:
            print(False)
    if 'Start' in command:
        current_command, substring = command.split()
        if text.startswith(substring):
            print(True)
        else:
            print(False)
    if 'Lowercase' in command:
        text = text.lower()
        print(text)
    if 'FindIndex' in command:
        current_command, char = command.split()
        print(text.rfind(char))
    if 'Remove' in command:
        current_command, start_index, count = command.split()
        start_index = int(start_index)
        count = int(count)
        text = text[:start_index] + text[start_index + count:]
        print(text)

    command = input()