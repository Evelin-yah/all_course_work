n = int(input())
searched_word = input()

all_strings = []
special_strings =[]

for i in range (n):
    current_string = input()
    all_strings.append(current_string)
    if searched_word in current_string:
        special_strings.append(current_string)

print(all_strings)
print(special_strings)