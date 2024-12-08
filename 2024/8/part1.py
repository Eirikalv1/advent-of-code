grid = list(map(list, open('input.txt').read().splitlines()))

count = 0
antennas_dict = {}
locations = set()

for row_i, row in enumerate(grid):
    for col_i, col in enumerate(row):
        if col != '.':
            tile = grid[row_i][col_i]
            antennas_dict[tile] = antennas_dict.get(tile, []) + [(col_i, row_i)]

for antennas in antennas_dict.values():
    lines = [
        ((x1, y1), (x2, y2))
        for i, (x1, y1) in enumerate(antennas)
        for j, (x2, y2) in enumerate(antennas)
        if i < j
    ]
    
    for pair in lines:
        a1, a2 = pair
        da = (a1[0] - a2[0], a1[1] - a2[1])
        n1, n2 = (a1[0] + da[0], a1[1] + da[1]), (a2[0] - da[0], a2[1] - da[1])
        
        if 0 <= n1[0] < len(grid[0]) and 0 <= n1[1] < len(grid):
            locations.add(n1)
        if 0 <= n2[0] < len(grid[0]) and 0 <= n2[1] < len(grid):
            locations.add(n2)
        
count += len(locations)
                
print(count)