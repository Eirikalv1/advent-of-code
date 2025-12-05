from icecream import ic

def compare(r1, r2):
    r1b, r1e, r2b, r2e = r1[0], r1[1], r2[0], r2[1]

    if r1e < r2b or r2e < r1b: return r2                                            # no overlap
    if (r1b <= r2b and r1e >= r2e): return (-1, -1)                                 # full overlap left
    if (r2b < r1b and r2e > r1e): return ((r2b, r1b - 1), (r1e + 1, r2e))           # full overlap right
    if (r1b <= r2b and r1e >= r2b): return (r1e + 1, r2e)                            # overlap right
    if (r2b <= r1b and r2e >= r1b): return (r2b, r1b - 1)                            # overlap left

    ic('Unreachable', r1, r2)

assert ic(compare((0, 1), (2, 3))) == (2, 3)            # no overlap right
assert ic(compare((2, 3), (0, 1))) == (0, 1)            # no overlap left
assert ic(compare((0, 3), (1, 2))) == (-1, -1)          # full overlap left
assert ic(compare((2, 4), (0, 6))) == ((0, 1), (5, 6))  # full overlap right
assert ic(compare((0, 1), (0, 1))) == (-1, -1)          # full overlap edge case
assert ic(compare((0, 2), (1, 3))) == (3, 3)            # overlap right
assert ic(compare((1, 3), (0, 2))) == (0, 0)            # overlap left
assert ic(compare((0, 1), (1, 2))) == (2, 2)            # edge case overlap right
assert ic(compare((1, 2), (0, 1))) == (0, 0)            # edge case overlap left
assert ic(compare((0, 1), (0, 2))) == (2, 2)            # edge case overlap right
assert ic(compare((1, 2), (0, 2))) == (0, 0)            # edge case overlap left

fresh, _ = open("input.txt", "r").read().split('\n\n')
fresh = list(map(lambda x: x.split('-'), fresh.split('\n')))
fresh = list(map(lambda x: (int(x[0]), int(x[1])), fresh))

ranges = {fresh[0]}

for f in fresh[1:]:
    temp = f
    for r in ranges:
        temp = compare(r, temp)
        if type(temp[0]) == tuple:
            temp = temp[0]
            fresh.append(temp[1])
    if temp == (-1, -1): continue
    ranges.add(temp)

total = sum(map(lambda x: x[1] - x[0] + 1, ranges))
print(total)