import numpy as np

lines = open('input.txt').read().splitlines()

count = 0
for j in range(2):
    for i in lines:
        count += i.count('XMAS') + i.count('SAMX')

    lines = np.array(list(map(list, lines)))
    for i in range(-len(lines[0]), len(lines[0])):
        diag = ''.join(lines.diagonal(i))
        count += diag.count('XMAS') + diag.count('SAMX')

    lines = [''.join(list(row)) for row in zip(*lines[::-1])]

print(count)