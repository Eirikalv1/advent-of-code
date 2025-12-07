from icecream import ic

grid = list(map(lambda x: list(x.strip()), open("input.txt", "r").readlines()))
display = lambda: ic(list(map(lambda x: ''.join(x), grid)))

count = 0
for y, col in enumerate(grid):
    for x, row in enumerate(col):
        if y == 0: continue
        if grid[y][x] == '^' and grid[y-1][x] == '|':
                count += 1
                grid[y][x-1] = '|'
                grid[y][x+1] = '|'
        if grid[y][x] != '^' and (grid[y-1][x] == 'S' or grid[y-1][x] == '|'):
            grid[y][x] = '|'

ic(count)