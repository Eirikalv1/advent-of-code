file = open("input.txt", "r")
lines = file.readlines()


total = [] 
for line in range(len(lines)):
    for i in range(len(lines[line])):
        if lines[line][i].isnumeric():
            total.append(lines[line][i])
            break
    for i in reversed(lines[line]):
        if i.isnumeric():
            total[-1] += i
            break

total = [int(x) for x in total]

print(sum(total))