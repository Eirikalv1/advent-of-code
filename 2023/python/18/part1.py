(directions, duration, _) = list(zip(*[i.split() for i in open("input.txt.", "r").read().splitlines()]))
duration = list(map(int, duration))

MAPPING = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1),
}

path = list()
pos = (0, 0)

for direct, dur in zip(directions, duration):
    direct = MAPPING[direct]
    temp = (direct[0] * dur, direct[1] * dur)
    path.append((pos[0] + temp[0], pos[1] + temp[1]))
    pos = (pos[0] + temp[0], pos[1] + temp[1])

area = 0
for p in range(len(path)-1):
    area += path[p][0] * path[p+1][1]
    area -= path[p][1] * path[p+1][0]

area = abs(area) / 2
points = area - sum(duration) / 2 + 1

print(points + sum(duration))