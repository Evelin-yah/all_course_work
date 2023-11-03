n = int(input())

evens = []
odds = []
negatives = []
positives = []

for i in range (n):
    number = int(input())

    if number % 2 == 0:
        evens.append(number)
    if number % 2 == 1:
        odds.append(number)
    if number < 0:
        negatives.append(number)
    if number >= 0:
        positives.append(number)

command = input()

if command == 'even':
    print(evens)
elif command == 'odd':
    print(odds)
elif command == 'negative':
    print(negatives)
else:
    print(positives)