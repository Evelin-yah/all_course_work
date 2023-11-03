def calculate(operator, num1, num2):
    result = 0
    if operator == 'multiply':
        result = num1*num2
    elif operator == 'divide':
        result = num1//num2
    elif operator == 'add':
        result = num1+num2
    elif operator == 'subtract':
        result = num1 - num2
    print(result)

operator = input()
num1 = int(input())
num2 = int(input())

calculate(operator, num1, num2)