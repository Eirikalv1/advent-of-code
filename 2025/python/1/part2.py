from icecream import ic

lines = open("input.txt", "r").readlines()

zeroes = 0
dial = 50

for i, line in enumerate(lines):
    num = int(line[1:])
    if line[0] == 'L':
        for i in range(num):
            dial -= 1
            if dial == 0: zeroes += 1
            if dial == -1: 
                dial += 100
    if line[0] == 'R':
        for i in range(num):
            dial += 1
            if dial == 0: zeroes += 1
            if dial == 100:
                dial -= 100
                zeroes += 1

print(zeroes)