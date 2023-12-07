import re

def seek(grid):
    nums = []
    syms = []
    for i, row in enumerate(grid): # Numbers
        num = [(int(nums.start()), int(nums.group())) \
            for nums in re.finditer("\d+", row)]
        if len(num) != 0:
            nums.extend([[(x[0], i), x[1]] for x in num])
        
        for j, col in enumerate(row): # Symbols
            if col != "." and col != "\n" and not col.isdigit():
                syms.append([j, i])
    return nums, syms
        
grid = open("input.txt", "r").readlines()
nums, syms = seek(grid)

score = 0
for sym in syms:
    box = set([(x, y) for y in range(sym[1] - 1, sym[1] + 2) \
                for x in range(sym[0] - 1, sym[0] + 2)])
    for num in nums:
        box2 = box.copy()
        for y in range(sym[1] - 1, sym[1] + 2):
            if len(str(num[1])) > 1: box2.add((sym[0] - 2, y))
            if len(str(num[1])) > 2: box2.add((sym[0] - 3, y))
        if num[0] in box2: score += num[1]
print(score)
