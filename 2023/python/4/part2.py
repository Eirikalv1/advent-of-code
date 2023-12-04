def getAmount(line):
    return sum(1 for part in range(2, 2 + win_elem)
                 for part2 in range(2 + win_elem, 3 + win_elem + my_elem)
                 if line[part2] == line[part])

lines = open("input.txt", "r").readlines()

win_elem = 10
my_elem = 25

cards = [1] * len(lines)
og_cards = []

for line in lines:
    line = line.split()
    og_cards.append(line)

for card in range(len(lines)):
    amount = getAmount(og_cards[card])
    for a in range(cards[card]):
        for i in range(card+1,amount+card+1):
            cards[i] += 1

print(sum(cards))
