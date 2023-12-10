GRID = open("input.txt", "r").readlines()

DIRS = {
    "S": [(1, 0), (-1, 0), (0, 1), (0, -1)], ".": [],
    "-": [(1, 0), (-1, 0)], "|": [(0, 1), (0, -1)],
    "F": [(1, 0), (0, 1)], "L": [(1, 0), (0, -1)],
    "7": [(-1, 0), (0, 1)], "J": [(-1, 0), (0, -1)],
}

sym = lambda x, y: GRID[y][x] 

def move(path):
    x, y = path[-1][0], path[-1][1]
    for d in DIRS[sym(x, y)]:
        if (-d[0], -d[1]) in DIRS[sym(x+d[0], y+d[1])] \
            and not (x+d[0], y+d[1]) in path:
                return x+d[0], y+d[1]

path = []
for y in range(len(GRID)):
    for x in range(len(GRID[y])):
        if sym(x, y) == "S": path.append((x, y))

while True:
    step = move(path)
    if step == None: break
    path.append(step)
print(len(path) / 2)