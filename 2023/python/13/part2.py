GRID = [block.splitlines() \
        for block in open("input.txt", "r").read().split("\n\n")]

rotate = lambda matrix: [''.join(row) for row in zip(*matrix[::-1])]

def find_symmetries(pattern):
    symmetries = []
    for i, (row1, row2) in enumerate(zip(pattern[:-1], pattern[1:])):
        if row1 == row2: symmetries.append(i)
    return symmetries

def count_symmetries(pattern):
    vert_symmetries, hor_symmetries = [], []
    hor_symmetries.extend(find_symmetries(pattern))
    vert_symmetries.extend(find_symmetries(rotate(pattern)))

    return hor_symmetries, vert_symmetries

def symmetry_distance(pattern, symmetry):
    size = 3
    symmetry -= 1
    while symmetry >= 0 and symmetry + size < len(pattern) \
        and pattern[symmetry] == pattern[symmetry+size]:
            size += 2
            symmetry -= 1
    
    return size / 2 - 0.5

def allowed_symmetry(pattern, symmetries):
    distances = [symmetry_distance(pattern, s) for s in symmetries]
    for s, d in zip(symmetries, distances):
        if s + d == len(pattern) - 1: return s, True
        if s - (d - 1) == 0: return s, True
    
    return 0, False

def score(symmetry, vert):
    if vert:
        return symmetry + 1
    return (symmetry + 1) * 100

total = 0
for pattern in GRID:
    symmetries = count_symmetries(pattern)
    hor_symmetry,  hor_allowed = allowed_symmetry(pattern, symmetries[0])
    vert_symmetry, _ = allowed_symmetry(rotate(pattern), symmetries[1])

    if hor_allowed: total += score(hor_symmetry, False)   
    else: total += score(vert_symmetry, True)
print(total)