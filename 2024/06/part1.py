lines = list(map(lambda x: x.replace('.', '0').replace('#', '1').replace('^', '2'), open('input.txt').read().splitlines()))
lines = list(map(lambda x: list(map(int, list(x))), lines))

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == 2:
            pos = [j, i]

dires = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dire = dires[0]

while True:
    if pos[1] == 0 or pos[1]+1 == len(lines) or pos[0] == 0 or pos[0]+1 == len(lines):
        break
    if lines[pos[1]+dire[1]][pos[0]+dire[0]] == 1:
        dire = dires[(dires.index(dire) + 1) % 4]
        
    lines[pos[1]+dire[1]][pos[0]+dire[0]] = 2
    lines[pos[1]][pos[0]] = 3
    pos = [pos[0]+dire[0], pos[1]+dire[1]]
                    
print(sum([line.count(3) for line in lines])+1)