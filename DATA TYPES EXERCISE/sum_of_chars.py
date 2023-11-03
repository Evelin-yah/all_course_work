lines = int(input())
sum = 0
for char in range(lines):
    current_char = input()
    sum += ord(current_char)

print(f'The sum equals: {sum}')
