lines = list(map(lambda x: list(map(int, x.split())), open("input.txt").read().splitlines()))

def check(line):
    for i in range(len(line) - 1):
        if not (abs(line[i] - line[i+1]) > 0 and abs(line[i] - line[i+1]) < 4) or not (all(line[i] < line[i + 1] \
            for i in range(len(line) - 1)) or all(line[i] > line[i + 1] for i in range(len(line) - 1))):
            return False
    return True

print(sum(any(check(i) for i in [line[:i] + line[i+1:] for i in range(len(line))]) for line in lines))