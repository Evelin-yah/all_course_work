import re

usernames = input().split(', ')

valid_usernames = []
regex = re.compile('[@!#$%^&*()<>?/\|}{~:]')
for username in usernames:
    if 3 <= len(username) <= 16 and regex.search(username) == None:
        valid_usernames.append(username)

print('\n'.join(valid_usernames))

#not ready
