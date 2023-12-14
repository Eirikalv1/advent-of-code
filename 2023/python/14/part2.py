TOTAL_CYCLES = 1_000_000_000

grid = [list(x) for x in open("input.txt").read().split()]

rotate = lambda matrix: [list(row)[::-1] for row in zip(*matrix)]

def move(grid, x, y):
    if grid[y][x] != 'O':
        return
    grid[y][x] = '.' 
    
    while len(grid) > y - 1 >= 0 and len(grid[0]) > x >= 0:
        if grid[y-1][x] == '.': y -= 1
        else: break
    grid[y][x] = 'O'

def cycle(grid):
    for _ in range(4):
        for y, col in enumerate(grid):
            for x, _ in enumerate(col):
                move(grid, x, y)
        grid = rotate(grid)
    return grid


def points(grid):
    total = 0
    for y, col in enumerate(grid):
        for x, _ in enumerate(col):
            if grid[y][x] == 'O': 
                total += len(grid) - y
    return total

def constant_difference(points):
    diff = points[1] - points[0]
    for i in range(2, len(points)):
        if points[i] - points[i-1] != diff:
            return False
    return True

possible_points = {}
for i in range(1, 1000):
    grid = cycle(grid)
    grid_points = points(grid)

    if not grid_points in possible_points:
        possible_points[grid_points] = []
    possible_points[grid_points].append(i)

for k, v in possible_points.items():
    if len(v) > 2:
        if (TOTAL_CYCLES - v[0]) % (v[1] - v[0]) == 0 and \
            constant_difference(v): print(k)