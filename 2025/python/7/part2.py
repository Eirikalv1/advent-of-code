from icecream import ic

grid = list(map(lambda x: list(x.strip()), open("input.txt", "r").readlines()))
display = lambda: ic(list(map(lambda x: ''.join(x), grid)))

indices = {(x, y): 0 for x in range(len(grid[0])) for y in range(len(grid))}
indices[(grid[0].index('S'), 0)] = 1

for y, col in enumerate(grid):
    for x, row in enumerate(col):
        if y == 0: continue
        if grid[y][x] == '^' and indices[(x, y-1)] >= 1:
                indices[(x+1, y)] += indices[(x, y-1)]
                indices[(x-1, y)] += indices[(x, y-1)]
        if grid[y][x] != '^' and indices[(x, y-1)] >= 1:
            indices[(x, y)] += indices[(x, y-1)]

count = 0
for x in range(len(grid[0])):
    count += indices[(x, len(grid)-1)]
ic(count)