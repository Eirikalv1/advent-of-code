grid = list(map(list, open('input.txt').read().splitlines()))

def get_region(pos, region):
    region.add(pos)
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x, y = pos[0] + dx, pos[1] + dy
        if not (0 <= y < len(grid) and 0 <= x < len(grid[0])): continue
        if grid[y][x] != grid[pos[1]][pos[0]]: continue
        if not (x, y) in region: get_region((x, y), region)
        
def get_line(pos, dire, region, visited):
    visited.add((pos, dire))
    nx, ny = pos[0] + dire[0], pos[1] + dire[1]
    x, y = pos[0] - dire[1], pos[1] - dire[0]
    if not (nx, ny) in region and (x, y) in region and not ((x, y), dire) in visited: 
        get_line((x, y), dire, region, visited)
    x, y = pos[0] + dire[1], pos[1] + dire[0]
    if not (nx, ny) in region and (x, y) in region and not ((x, y), dire) in visited: get_line((x, y), dire, region, visited)
    
regions = set()
for r, row in enumerate(grid):
    for c, col in enumerate(row):
        region = set()
        get_region((c, r), region)  
        regions.add(frozenset(region))

total = 0
for region in regions:
    area = len(region)
    sides = 0
    visited = set()
    for x, y in region:
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if ((x, y), (dx, dy)) in visited: continue
            if (nx, ny) in region: continue
            get_line((x, y), (dx, dy), region, visited)
            sides += 1
    total += area * sides
print(total)