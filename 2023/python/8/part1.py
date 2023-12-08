lines = open("input.txt", "r").readlines()

inst = ""
maps = {}

for line in lines:
    line = line.split()
    if not "=" in line and line != []:
        inst = line[0] * 10000
    elif line == []: continue
    else:
        maps[line[0]] = (line[2][1:][:3], line[3][:3])

steps = 0
cur = "AAA"
for i in inst:
    if i == "L": cur = maps[cur][0]
    elif i == "R": cur = maps[cur][1]
    steps += 1
    if cur == "ZZZ": break
print(steps)

