def cards_score(cards):
    score = ""
    for card in cards:
        if card.isdigit(): score += str(int(card) - 2 )
        match card:
            case "T": score += "8"
            case "J": score += "9"
            case "Q": score += "A"
            case "K": score += "B"
            case "A": score += "C"
    return int(score, 13)

def type_score(cards):
    freq = {}
    for card in cards:
        if card in freq:
            freq[card] += 1
        else: freq[card] = 1
    
    type1 = []
    [type1.append(card) for card in freq.values() if card != 1]
    type1.sort()
    
    match type1:
        case []: return 1
        case [2]: return 2
        case [2, 2]: return 3
        case [3]: return 4
        case [2, 3]: return 5
        case [4]: return 6
        case [5]: return 7

lines = open("input.txt", "r").readlines()

scores = {}
for line in lines:
    line = line.strip().split()
    combined_score = type_score(line[0]) * 10000000 + cards_score(line[0])
    scores[combined_score] = int(line[1])

keys = [k for k in scores.keys()]
keys.sort()

total = 0
for i in range(1, len(keys) + 1):
    total += scores[keys[i-1]] * i
print(total)