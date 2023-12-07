def get_scores(round):
    rec = []
    for i in range(round[0]+1):
        score = (round[0] - i) * i
        if score > round[1]: rec.append(i)
    return rec

lines = open("input.txt", "r").readlines()

score = len(get_scores([int(lines[0][5:].replace(" ","")), int(lines[1][9:].replace(" ",""))]))

print(score)