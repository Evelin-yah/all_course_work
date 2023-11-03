bottles = int(input())
litters_in_tank = 0

for i in range(bottles):
    bottle = int(input())
    litters_in_tank += bottle
    if litters_in_tank > 255:
        print('Insufficient capacity!')
        litters_in_tank -= bottle
        continue

print(litters_in_tank)
