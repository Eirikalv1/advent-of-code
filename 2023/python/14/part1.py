grid = [list(x) for x in open("input.txt").read().split()]

def move(x, y):
    if grid[y][x] != 'O':
        return
    grid[y][x] = '.' 
    
    while len(grid) > y - 1 >= 0 and len(grid[0]) > x >= 0:
        if grid[y-1][x] == '.': y -= 1
        else: break
    grid[y][x] = 'O'

def points():
    total = 0
    for y, col in enumerate(grid):
        for x, _ in enumerate(col):
            if grid[y][x] == 'O': 
                total += len(grid) - y
    return total

for y, col in enumerate(grid):
    for x, _ in enumerate(col):
        move(x, y)

print(points())
