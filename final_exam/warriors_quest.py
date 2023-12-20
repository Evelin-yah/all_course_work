skill = input()
command = input()
def target_change(skill, first_substring, second_substring):
    skill = skill.replace(first_substring, second_substring)
    return skill

def target_remove(skill, substring):
    if substring in skill:
        skill = skill.replace(substring, '')
    return skill

while command != 'For Azeroth':

    if command == 'GladiatorStance':
        skill = skill.upper()
        print(skill)
    elif command == 'DefensiveStance':
        skill = skill.lower()
        print(skill)
    elif command.startswith('Dispel'):
        command = command.split()
        index = int(command[1])
        letter = command[2]
        if 0 <= index < len(skill):
            skill_list = list(skill)
            skill_list[index] = letter
            skill = ''.join(skill_list)
            print("Success!")
        else:
            print("Dispel too weak.")
    elif command.startswith('Target Change'):
        command = command.split()
        first_substring = command[2]
        second_substring = command[3]
        skill = target_change(skill, first_substring, second_substring)
        print(skill)
    elif command.startswith("Target Remove"):
        command = command.split()
        substring = command[2]
        skill = target_remove(skill, substring)
        print(skill)
    else:
        print("Command doesn't exist!")

    command = input()
