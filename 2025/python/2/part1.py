from icecream import ic

lines = list(map(lambda x: x.split('-'), open("input.txt", "r").read().split(',')))

def is_repeating(num: int) -> bool:
    num = str(num)
    if len(num) % 2 != 0: return False
    return num[:len(num)//2] == num[len(num)//2:]

total = 0
for i, line in enumerate(lines):
    ids = range(int(line[0]), int(line[1])+1)
    for i in ids:
        if is_repeating(i):
            total += i
ic(total)