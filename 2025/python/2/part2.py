from icecream import ic

lines = list(map(lambda x: x.split('-'), open("input.txt", "r").read().split(',')))

def is_repeating(num: int) -> bool:
    num = str(num)
    for i in range(1, len(num)):
        curr = num[0:i]
        if (len(num) // len(curr)) * curr == num: return True
    return False

total = 0
for i, line in enumerate(lines):
    ids = range(int(line[0]), int(line[1])+1)
    for i in ids:
        if is_repeating(i):
            total += i
ic(total)