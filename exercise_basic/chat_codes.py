n = int(input())

for i in range(n):
    n = int(input())

    if n == 88:
        print('Hello')
    elif n == 86:
        print('How are you?')
    elif n != 88 and n != 86 and n < 88:
        print('GREAT!')
    else:
        print('Bye.')
