import re

def check_password_len(data):
    if 6 <= len(data) < 10:
        return True
    else:
        return False
def check_password_chars(data):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:; ]')

    if (regex.search(data) == None):
        return True
    else:
        return False

def check_password_digits(data):
    #regex = re.compile('1234567890')

    #if (regex.search(data) < 2):
    if len([x for x in data if x.isdigit()]) < 2:
        return False
    else:
        return True

password_data = input()
is_valid = False
if check_password_len(password_data) == True and check_password_chars(password_data) == True and check_password_digits(password_data) == True:
    is_valid = True
    print('Password is valid')
    exit()
if not check_password_len(password_data):
    print("Password must be between 6 and 10 characters")
if not check_password_chars(password_data):
    print("Password must consist only of letters and digits")
if not check_password_digits(password_data):
    print("Password must have at least 2 digits")