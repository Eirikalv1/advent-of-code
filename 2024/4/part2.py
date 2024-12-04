lines = open('input.txt').read().splitlines()

count = 0
for yi, yv in enumerate(lines):
    for xi, xv in enumerate(yv):
        if 0 < yi < len(lines) - 1 and 0 < xi < len(lines[yi]) - 1 and yv[xi] == 'A':
            corners = lines[yi-1][xi-1] + lines[yi-1][xi+1] + lines[yi+1][xi+1] + lines[yi+1][xi-1]
            count += corners.count('M') == 2 and corners.count('S') == 2 and corners[0] != corners[2] and corners[1] != corners[3]
print(count)