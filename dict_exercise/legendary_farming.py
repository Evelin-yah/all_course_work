materials = {'shards': 0, 'fragments' : 0, 'motes': 0}
current_items = input().split()
created = False

while not created:
    for item in range(0, (len(current_items)), 2):
        value = int(current_items[item])
        key = current_items[item+1].lower()
        if key not in materials:
            materials[key] = 0
        materials[key] += value
        if materials['shards'] >= 250:
            print(f'Shadowmourne obtained!')
            materials['shards'] -= 250
            created = True
        elif materials['fragments'] >= 250:
            materials['fragments'] -= 250
            print(f'Valanyr obtained!')
            created = True
        elif materials['motes'] >= 250:
            print(f'Dragonwrath obtained!')
            materials['motes'] -= 250
            created = True
        if created:
            break
    if created:
        break
    current_items = input().split()

for material, quantity in materials.items():
   print(f'{material}: {quantity}')