def getAmount(line):
    return sum(1 for part in range(2, 2 + win_elem)
                 for part2 in range(2 + win_elem, 3 + win_elem + my_elem)
                 if line[part2] == line[part])

lines = open("input.txt", "r").readlines()

win_elem = 10
my_elem = 25

total_points = 0
for line in lines:
    line = line.split()

    points = 1
    for i in range(len(getAmount(line))):
        points *= 2
    points /= 2
    if len(getAmount(line)) == 0: points = 0
    total_points += points
print(total_points)
        