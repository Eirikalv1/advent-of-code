import math

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
        da = (a2[0] - a1[0], a2[1] - a1[1])

        gcd = math.gcd(da[0], da[1])
        step = (da[0] // gcd, da[1] // gcd)

        n1, n2 = a1, a2
        while 0 <= n1[0] < len(grid[0]) and 0 <= n1[1] < len(grid):
            locations.add(n1)
            n1 = (n1[0] + step[0], n1[1] + step[1])
        while 0 <= n2[0] < len(grid[0]) and 0 <= n2[1] < len(grid):
            locations.add(n2)
            n2 = (n2[0] - step[0], n2[1] - step[1])

        
count += len(locations)
                
print(count)