def add_person(people, name, health, energy):
    if name in people:
        people[name][0] += health
    else:
        people[name] = [health, energy]

def attack(people, attacker, defender, damage):
    if attacker in people and defender in people:
        people[defender][0] -= damage
        people[attacker][1] -= 1

        if people[defender][0] <= 0:
            del people[defender]
            print(f"{defender} was disqualified!")

        if people[attacker][1] <= 0:
            del people[attacker]
            print(f"{attacker} was disqualified!")

def delete_person(people, username):
    if username == "All":
        people.clear()
    elif username in people:
        del people[username]

def battle_manager():
    people = {}

    while True:
        command = input().split(":")
        if command[0] == "Results":
            break

        action = command[0]

        if action == "Add":
            name, health, energy = command[1], int(command[2]), int(command[3])
            add_person(people, name, health, energy)

        elif action == "Attack":
            attacker, defender, damage = command[1], command[2], int(command[3])
            attack(people, attacker, defender, damage)

        elif action == "Delete":
            username = command[1]
            delete_person(people, username)

    print(f"People count: {len(people)}")
    for name, stats in sorted(people.items(), key=lambda x: (-x[1][0], x[0])):
        print(f"{name} - {stats[0]} - {stats[1]}")

battle_manager()