lines = list(map(lambda x: list(map(int, x.split())), open("input.txt").read().splitlines()))

total = 0
for line in lines:
    for i in range(len(line) - 1):
        if not (abs(line[i] - line[i+1]) > 0 and abs(line[i] - line[i+1]) < 4) or not (all(line[i] < line[i + 1] for i in range(len(line) - 1)) or \
           all(line[i] > line[i + 1] for i in range(len(line) - 1))):
            break
    else:
        total += 1
print(total)