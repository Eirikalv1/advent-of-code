lines = open("input.txt", "r").readlines()

total = 0
for line in lines:
    diffs = [list(map(int, line.strip().split()))]
    while any(diffs[-1]) != 0:
        diffs.append([b - a for a, b in zip(diffs[-1][:-1], diffs[-1][1:])])
        
    diffs = diffs[::-1]
    for i, diff in enumerate(diffs[1:]):
        diffs[i+1].insert(0, diff[0] - diffs[i][0])
    total += diffs[-1][0]
print(total)