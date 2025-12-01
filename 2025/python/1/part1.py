from icecream import ic

lines = open("input.txt", "r").readlines()

zeroes = 0
dial = 50

for i, line in enumerate(lines):
    if line[0] == 'L':
        dial -= int(line[1:])
    if line[0] == 'R':
        dial += int(line[1:])
    dial = (dial + 100) % 100
    if dial == 0:
        zeroes += 1
    ic(dial)

print(zeroes)