
card_values = [str(x) for x in range(2, 10)] + ["T", "J", "Q", "K", "A"]
def get_value(card):
    return card_values.index(card[0]) + 2  

def are_same(list1, list2):
    if len(list1) != len(list2):
        return False
    for i1, i2 in zip(list1, list2):
        if i1 != i2:
            return False
    return True

def get_value_of_hand(hand):
    suits = ""
    numbers = []
    for card in hand:
        suits += card[1]
        numbers.append(get_value(card))
    

    
    straight = are_same(sorted(numbers), [x for x in range(min(numbers), min(numbers) + len(hand))])
    flush = suits[0] * len(hand) == suits

    if flush and are_same(sorted(numbers), [x for x in range(10, 15)]):
        return 900 # royal flush

    if straight and flush:
        return 800 # straight flush

    three_of_a_kind = False
    pairs = 0
    for n in numbers:
        amount = len([x for x in numbers if x == n])
        if amount >= 4:
            return 700 # four of a kind
        elif amount == 3:
            three_of_a_kind = True
        elif amount == 2:
            pairs += 1
    pairs /= 2
    
    if pairs >= 1 and three_of_a_kind:
        return 600 # full house
    elif flush:
        return 500 # flush
    elif straight:
        return 400 # straight
    elif three_of_a_kind:
        return 300 # three of a kind
    elif pairs == 2:
        return 200 # two pairs
    elif pairs == 1:
        return 100 # one pair
    return 0 # highest card

file = open("poker.txt", "r")
content = file.read()
file.close()

hands = []

for line in content.split("\n"):
    cards = line.split()
    hands.append([cards[:len(cards) // 2], cards[len(cards) // 2:]])

wins = 0
for hand1, hand2 in hands:
    #print(hand1, hand2)
    value1 = get_value_of_hand(hand1)
    value2 = get_value_of_hand(hand2)
    #print(value1, value2)
    if value1 == value2:
        #print("draw, tie-breaking")
        numbers1 = [get_value(x) for x in hand1]
        numbers2 = [get_value(x) for x in hand2]
        while numbers1 and numbers2:
            max1 = max(numbers1)
            numbers1.remove(max1)
            max2 = max(numbers2)
            numbers2.remove(max2)
            #print(max1, max2)
            if max1 != max2:
                if max1 > max2:
                    #print("player 1 wins")
                    wins += 1
                break
    elif value1 > value2:
        #print("player 1 wins")
        wins += 1
print(wins)
