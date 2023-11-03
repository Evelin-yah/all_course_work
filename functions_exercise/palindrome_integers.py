def check_is_palindrome(data):

    for el in data:
        if data == data[::-1]:
            return True
        return False

input_data = input().split(', ')

for data in input_data:
    is_palindrome = check_is_palindrome(data)
    print(is_palindrome)