import re
line = input()
pattern = r"([#\$%&])([A-Za-z]+)\1=(\d+)!!(.+)"
coordinates_found = False
while not coordinates_found:
    match = re.findall(pattern, line)
    if match:
        name = match[0][1]
        length = int(match[0][2])
        code = match[0][3]

        if len(code) == length:
            decrypted_code = ''.join(chr(ord(symbol) + length) for symbol in code)
            print(f"Coordinates found! {name} -> {decrypted_code}")
            coordinates_found = True
            break
        else:
            print('Nothing found!')
    else:
        print('Nothing found!')
    line = input()