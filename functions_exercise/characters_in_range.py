def characters_in_range(start, end):
    start = ord(start)
    end = ord(end)
    for i in range(start + 1, end):
        print(chr(i), end=" ")

starting = input()
ending = input()

characters_in_range(starting, ending)