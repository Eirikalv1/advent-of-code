from functools import cache

@cache
def processtone(stone):
    if stone == 0:
        return 1,
    elif len(str(stone)) % 2 == 0:
        half = len(str(stone)) // 2
        left, right = int(str(stone)[:half]), int(str(stone)[half:])
        return left, right
    else:
        return (stone * 2024,)

stones = list(map(int, open('input.txt').read().strip().split()))
stonemap = dict()

for stone in stones:
    stonemap[stone] = 1

for b in range(75):
    currdict = stonemap.copy()
    for stone, amount in stonemap.items():
        currdict[stone] -= amount
        for s in (t := processtone(stone)):
            currdict[s] = currdict.get(s, 0) + amount
    stonemap = currdict

print(sum(stonemap.values()))