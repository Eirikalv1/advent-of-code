grid = list(map(list, open('input.txt').read().splitlines()))
zeroes = [(x, y) for y, row in enumerate(grid) for x in range(len(row)) if grid[y][x] == '0']

trailheads = 0

def move(pos):
    global nines, trailheads
    x, y = pos
    if grid[y][x] == '9': 
        trailheads += 1
        return
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]):
            neighbor = grid[ny][nx]
            if neighbor.isdigit() and int(neighbor) == int(grid[y][x]) + 1:
                move((nx, ny))

for pos in zeroes: move(pos)
print(trailheads)