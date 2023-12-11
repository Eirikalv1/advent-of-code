def expand_grid(grid):
    steps = 0
    for i, line in enumerate(grid.copy()):
        if not "#" in line:
            grid.insert(i+steps, "." * len(line))
            steps += 1
    return grid

rotate = lambda grid: [''.join(row) for row in zip(*[s[::-1] for s in grid])]

grid = open("input.txt", "r").readlines()
for i, _ in enumerate(grid):
    grid[i] = grid[i].strip()

grid = expand_grid(grid)
grid = rotate(grid)
grid = expand_grid(grid)
grid = rotate(grid)
grid = rotate(grid)
grid = rotate(grid)

galaxies = []
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == "#": galaxies.append((x,y))

path = 0
for i, pos in enumerate(galaxies):
    for pos2 in galaxies[i:]:
        path += abs(pos2[0] - pos[0]) + abs(pos2[1] - pos[1])
print(path)