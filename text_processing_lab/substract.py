to_remove = input()
text = input()

while True:
    text = text.replace(to_remove, '')

    if to_remove not in text:
        break

print(text)