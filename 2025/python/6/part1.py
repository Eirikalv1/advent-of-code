from icecream import ic

lines = list(map(lambda x: x.strip().split(), open("input.txt", "r").readlines()))
lines = [[lines[j][i] for j in range(len(lines))] for i in range(len(lines[0])-1,-1,-1)]
ic(lines)
total = 0
for i, line in enumerate(lines):
    amount = int(line[0])
    op = line[-1]
    line = line[1:-1]
    for num in line:
        if op == '*': amount *= int(num)
        if op == '+': amount += int(num)
    total += amount
ic(total)