encrypted_text = ''
text = input()

for char in text:
    current_symbol = ord(char) + 3
    encrypted_text += chr(current_symbol)

print(encrypted_text)