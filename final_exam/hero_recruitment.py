command = input()
heroes = {}

while command != 'End':
    if 'Enroll' in command:
        current_command, hero_name = command.split()
        if hero_name not in heroes:
            heroes[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")
    if 'Learn' in command:
        current_command, hero_name, spell_name = command.split()
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        else:
            # for spell in heroes.items():
            if spell_name in heroes[hero_name]:
                print(f"{hero_name} has already learnt {spell_name}.")
            else:
                heroes[hero_name].append(spell_name)
    if 'Unlearn' in command:
        current_command, hero_name, spell_name = command.split()
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        else:
            if spell_name in heroes[hero_name]:
                heroes[hero_name].remove(spell_name)
            else:
                print(f"{hero_name} doesn't know {spell_name}.")

    command = input()
print('Heroes:')
for hero, spell in heroes.items():
    print(f'== {hero}: {"".join(spell)}')
