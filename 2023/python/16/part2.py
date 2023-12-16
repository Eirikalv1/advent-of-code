import numpy as np
import sys

sys.setrecursionlimit(5000)

GRID = np.array(list(map(list, open("input.txt", "r").read().splitlines())))

INTERACTIONS = {
    ((0, 1), '-'): [(1, 0), (-1, 0)],
    ((0, -1), '-'): [(1, 0), (-1, 0)],

    ((1, 0), '|'): [(0, 1), (0, -1)],
    ((-1, 0), '|'): [(0, 1), (0, -1)],

    ((1, 0), '/'): [(0, -1)], ((-1, 0), '/'): [(0, 1)],
    ((0, 1), '/'): [(-1, 0)], ((0, -1), '/'): [(1, 0)],

    ((1, 0), '\\'): [(0, 1)], ((-1, 0), '\\'): [(0, -1)],
    ((0, 1), '\\'): [(1, 0)], ((0, -1), '\\'): [(-1, 0)],
}

out_of_bounds = lambda pos: not 0 <= pos[0] < len(GRID[0]) or not 0 <= pos[1] < len(GRID)

path, seen = set(), []

def move(pos, aim):
    if out_of_bounds(pos): return
    if (pos, aim) in seen: return

    interaction = (aim, GRID[pos[1], pos[0]])

    path.add(pos)
    seen.append((pos, aim))

    if not interaction in INTERACTIONS:
        move((pos[0] + aim[0], pos[1] + aim[1]), aim)
        return
    
    for split_aim in INTERACTIONS[interaction]:
        split_pos = (pos[0] + split_aim[0], pos[1] + split_aim[1])    
        if out_of_bounds(split_pos): continue

        path.add(split_pos)
        move(split_pos, split_aim)


highscore = 0

for i in range(len(GRID[0])):
    path, seen = set(), []
    move((i, 0), (0, 1))
    if len(path) > highscore: highscore = len(path)

    path, seen = set(), []
    move((i, len(GRID[0])-1), (0, -1))
    if len(path) > highscore: highscore = len(path)

for i in range(len(GRID)):
    path, seen = set(), []
    move((0, i), (1, 0))
    if len(path) > highscore: highscore = len(path)

    path, seen = set(), []
    move((len(GRID)-1, i), (-1, 0))
    if len(path) > highscore: highscore = len(path)

print(highscore)