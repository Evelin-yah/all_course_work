
def archery_tournament(targets):
    points = 0

    while True:
        command = input().split('@')

        if command[0] == 'Game over':
            break

        if command[0] == 'Shoot Left':
            start_index = int(command[1])
            length = int(command[2])

            if 0 <= start_index < len(targets):
                index = (start_index - length) % len(targets)
                points += shoot(targets, index)

        elif command[0] == 'Shoot Right':
            start_index = int(command[1])
            length = int(command[2])

            if 0 <= start_index < len(targets):
                index = (start_index + length) % len(targets)
                points += shoot(targets, index)

        elif command[0] == 'Reverse':
            targets.reverse()

    return points


def shoot(targets, index):
    points = 0
    target_value = targets[index]

    if target_value >= 5:
        points += 5
        targets[index] -= 5
    else:
        points += target_value
        targets[index] = 0

    return points

targets = list(map(int, input().split("|")))
total_points = archery_tournament(targets)
print(" - ".join(map(str, targets)))
print(f"John finished the archery tournament with {total_points} points!")