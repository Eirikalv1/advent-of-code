from icecream import ic

lines = list(map(lambda x: list(x[:-1]), open("input.txt", "r").readlines()))

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if j == 0: continue
        if lines[-1][j] != ' ':
            lines[i][j-1] = '|'

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if i == len(lines)-1: break
        if lines[i][j] == ' ': lines[i][j] = '-'

lines = [''.join([lines[j][i] for j in range(len(lines))]) for i in range(len(lines[0])-1,-1,-1)][::-1]
for i, line in enumerate(lines):
    while lines[i][-1] != '|' and i < len(lines)-1 and lines[i+1][-1] != '|':
        lines[i] = lines[i][:-1] + line[-1]
        i += 1
    if '|' in line:
        lines[i] = '+'

total = eval(''.join(lines).replace('-', ''))
ic(total)