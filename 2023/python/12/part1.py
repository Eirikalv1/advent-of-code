LINES = open("input.txt", "r").readlines()

def check_spring(spring, stat):
    check = []
    for i, char in enumerate(spring[1:]):
        if char == "#" and spring[i] == ".":
            check.append(1)
        elif char == "#" and spring[i] == "#": check[-1] += 1
    return stat == check

def gen_perms(spring, i, perms):
    if i == len(spring):
        perms.add(spring)
        return

    if spring[i] == '?':
        for char in ['.', '#']:
            spring = spring[:i] + char + spring[i+1:]
            gen_perms(spring, i+1, perms)
    else: gen_perms(spring, i+1, perms)

springs = []
stats = []
for i, line in enumerate(LINES):
    line = line.strip()
    line = line.split(" ")
    line[1] = line[1].split(",")
    line[1] = list(map(int, line[1]))
    line[0] = "." + line[0]
    springs.append(line[0])
    stats.append(line[1])


total = 0
for i, spring in enumerate(springs):
    perms = set()
    gen_perms(spring, 0, perms)

    for perm in perms:
        total += check_spring(perm, stats[i])
print(total)