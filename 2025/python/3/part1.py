lines = open("input.txt", "r").readlines()

summ = 0
for line in lines:
    line = list(map(int, line.strip()))
    largest = 0
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            num = int(str(line[i]) + str(line[j]))
            if num > largest:
                largest = num
    summ += largest


print(summ)
