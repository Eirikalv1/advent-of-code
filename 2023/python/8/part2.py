import math

def get_steps(start):
    steps = 0
    for i in inst:
        if i == "L": start = maps[start][0]
        elif i == "R": start = maps[start][1]
        steps += 1
        if start in ends: break
    return steps

lines = open("input.txt", "r").readlines()

inst = ""
maps = {}

for line in lines:
    line = line.split()
    if not "=" in line and line != []:
        inst = line[0] * 1000
    elif line == []: continue
    else:
        maps[line[0]] = (line[2][1:][:3], line[3][:3])

starts, ends = [], []
for i in maps:
    if i[2] == "A": starts.append(i)
    if i[2] == "Z": ends.append(i)

total = []
for s in starts:
    total.append(get_steps(s))

lcm = math.lcm(*total)
print(lcm)