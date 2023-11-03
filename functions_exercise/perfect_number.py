def is_perfect_number(number):
    proper_divisors = []
    for i in range(1, number):
        if number % i == 0:
            proper_divisors.append(i)

    if sum(proper_divisors) == number:
        return True
    return False

n = int(input())

if is_perfect_number(n):
    print('We have a perfect number!')
else:
    print("It's not so perfect.")