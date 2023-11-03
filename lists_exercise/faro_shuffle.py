cards = input().split()
shuffles = int(input())
middle_deck = len(cards) // 2


for shuffle in range(shuffles):
    left_part = cards[:middle_deck]
    right_part = cards[middle_deck:]
    shuffled_cards = []
    for card in range(len(left_part)):
        shuffled_cards.append(left_part[card])
        shuffled_cards.append(right_part[card])
    cards = shuffled_cards

print(shuffled_cards)