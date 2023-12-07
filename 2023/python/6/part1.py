def get_scores(round):
    rec = []
    for i in range(round[0]+1):
        score = (round[0] - i) * i
        if score > round[1]: rec.append(i)
    return rec

lines = open("input.txt", "r").readlines()
lines = [x.split() for x in lines]

score = 1
for i in range(1, len(lines[0])):
    score *= len(get_scores([int(lines[0][i]), int(lines[1][i])]))

print(score)