lines = list(map(lambda x: x.replace('.', '0').replace('#', '1').replace('^', '2'), open('input.txt').read().splitlines()))
lines = list(map(lambda x: list(map(int, list(x))), lines))

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == 2:
            start_pos = [j, i]

dires = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dire = dires[0]

def check_loop(pos, dire, lines):
    visited = set()
    
    while True:
        if (pos[0], pos[1], dire) in visited:
            return True
        visited.add((pos[0], pos[1], dire))
        
        if pos[1]+dire[1] < 0 or pos[1]+dire[1] >= len(lines) or pos[0]+dire[0] < 0 or pos[0]+dire[0] >= len(lines[0]):
            return False
        
        if lines[pos[1]+dire[1]][pos[0]+dire[0]] == 1:
            dire = dires[(dires.index(dire) + 1) % 4]  
        else:      
            pos = [pos[0]+dire[0], pos[1]+dire[1]]      

count = 0
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if lines[i][j] == 1 or [j, i] == start_pos: continue
        pos = start_pos
        dire = dires[0]
        temp = lines[i][j]
        lines[i][j] = 1
        count += check_loop(pos, dire, lines)
        lines[i][j] = temp
                    
print(count)