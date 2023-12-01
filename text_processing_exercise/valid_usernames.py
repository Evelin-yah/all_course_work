# import re
#
# usernames = input().split(', ')
#
# valid_usernames = []
# regex = re.compile('[@!#$%^&*()<>?/\|}{~: ]')
# for username in usernames:
#     if 3 <= len(username) <= 16 and regex.search(username) == None:
#         valid_usernames.append(username)
#
# print('\n'.join(valid_usernames))
#
#Another way to solve it without regEx:

def len_is_valid(username):
    if 3 <= len(username) <= 16:
        return True
    return False
def chars_are_valid(username):
    for char in username:
        if not (char.isalnum() or char == '-' or char == '_'):
            return False
    return True
def no_reduntant_sybols(username):
    if ' ' in username:
        return False
    return True
def username_is_valid(username):
    if (len_is_valid(username)
            and chars_are_valid(username)
            and no_reduntant_sybols(username)):
        return True
    return False

usernames = input().split(', ')
for username in usernames:
    if username_is_valid(username):
        print(username)