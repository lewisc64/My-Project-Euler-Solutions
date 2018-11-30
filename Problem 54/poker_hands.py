
card_values = [str(x) for x in range(2, 10)] + ["T", "J", "Q", "K", "A"]
def get_value(card):
    return card_values.index(card[0]) + 2  

def get_value_of_hand(hand):
    suits = ""
    numbers = []
    for card in hand:
        suits += card[1]
        numbers.append(get_value(card))
    
    if set(numbers) == set([x for x in range(10, 15)]):
        return 1000 # royal flush

    straight = set(numbers) == set([x for x in range(min(numbers), len(hand))])
    flush = suits[0] * len(hand) == suits

    if straight and flush:
        return 900 # straight flush
    

    three_of_a_kind = False
    pairs = 0
    for n1 in numbers:
        amount = 0
        for n2 in numbers:
            amount += 1
        if amount >= 4:
            return 800 # four of a kind
        elif amount == 3:
            three_of_a_kind = True
        elif amount == 2:
            pairs += 1
    pairs /= 2
    
    pair = 

    return sum(numbers)

file = open("poker.txt", "r")
content = file.read()
file.close()

hands = []

for line in content.split("\n"):
    cards = line.split()
    hands.append([cards[:len(cards) // 2], cards[len(cards) // 2:]])

print(hands[0][0])
print(get_value_of_hand(hands[0][0]))
