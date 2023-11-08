n = int(input())

for i in range(n):
    num = int(input())
    if not num % 2 == 0:
        print(f'{num} is odd!')
        break
else:
    print('All numbers are even.')
