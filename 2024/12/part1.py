grid = list(map(list, open('input.txt').read().splitlines()))

def get_region(pos, region):
    region.add(pos)
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x, y = pos[0] + dx, pos[1] + dy
        if not (0 <= y < len(grid) and 0 <= x < len(grid[0])): continue
        if grid[y][x] != grid[pos[1]][pos[0]]: continue
        if not (x, y) in region: get_region((x, y), region)

regions = set()
for r, row in enumerate(grid):
    for c, col in enumerate(row):
        region = set()
        get_region((c, r), region)  
        regions.add(frozenset(region))

total = 0
for region in regions:
    area = len(region)
    perimeter = 0
    for plant in region:
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = plant[0] + dx, plant[1] + dy
            if not (x, y) in region:
                perimeter += 1
    total += area * perimeter
    
print(total)