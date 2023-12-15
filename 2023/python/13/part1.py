import numpy as np

GRID = [np.array(list(map(list, block.splitlines()))) \
        for block in open("input.txt", "r").read().split("\n\n")]

sym_valid = lambda block, sym: all(np.array_equal(block[row1], block[row2]) \
    for row1, row2 in zip(range(sym, -1, -1), range(sym+1, len(block)))) if sym < len(block) - 1 else False
   
total = 0
for block in GRID:
    total += sum([(sym + 1) * 100 for sym in range(len(block)) if sym_valid(block, sym)])
    total += sum([sym + 1 for sym in range(len(np.rot90(block, k=3))) if sym_valid(np.rot90(block, k=3), sym)])
        
print(total)