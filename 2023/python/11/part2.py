from copy import deepcopy

def expand_grid(grid):
    steps = []
    for y, line in enumerate(grid):
        if not "#" in line:
            steps.append(y)
    return grid, steps

rotate = lambda grid: [''.join(row) for row in zip(*[s[::-1] for s in grid])]

grid = open("input.txt", "r").readlines()
for i, _ in enumerate(grid):
    grid[i] = grid[i].strip()

grid, ys = expand_grid(grid)
grid = rotate(grid)
grid = rotate(grid)
grid = rotate(grid)
grid, xs = expand_grid(grid)
grid = rotate(grid)

galaxies = []
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == "#": galaxies.append([x,y])

amnt = 1_000_000
new_galaxies = deepcopy(galaxies)
for i, galaxy in enumerate(galaxies):
    for x in xs:
        if galaxy[0] > x: new_galaxies[i][0] += amnt - 1
    for y in ys:
        if galaxy[1] > y: new_galaxies[i][1] += amnt - 1

path = 0
for i, pos in enumerate(new_galaxies):
    for pos2 in new_galaxies[i:]:
        path += abs(pos2[0] - pos[0]) + abs(pos2[1] - pos[1])
print(path)