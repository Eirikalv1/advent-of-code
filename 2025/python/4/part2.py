from icecream import ic
from copy import deepcopy

lines = list(map(lambda x: list(x.strip()), open("input.txt", "r").readlines()))

total = 0
while True:
    new = deepcopy(lines)
    for y, col in enumerate(lines):
        colLen = len(lines)
        for x, row in enumerate(col):
            rowLen = len(col)
            if lines[y][x] == '@':
                amount = 0
                if y + 1 < colLen:
                    amount += int(lines[y+1][x] == '@') 
                if y - 1 >= 0:
                    amount += int(lines[y-1][x] == '@')
                if x + 1 < rowLen:
                    amount += int(lines[y][x+1] == '@') 
                if x - 1 >= 0:
                    amount += int(lines[y][x-1] == '@')
                if y + 1 < colLen and x + 1 < rowLen:
                    amount += int(lines[y+1][x+1] == '@')
                if y + 1 < colLen and x - 1 >= 0:
                    amount += int(lines[y+1][x-1] == '@')
                if y - 1 >= 0 and x + 1 < rowLen:
                    amount += int(lines[y-1][x+1] == '@') 
                if y - 1 >= 0 and x - 1 >= 0:
                    amount += int(lines[y-1][x-1] == '@')
                if amount < 4:
                    total += 1
                    new[y][x] = '.'
    lines = new
    print(total)
            