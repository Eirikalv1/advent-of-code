def formatString(line):
    line = line.replace(":","")
    line = line.replace(";"," ; ")
    line = line.replace(",","")
    line = line.split()
    line.append(";")
    return line

file = open("input.txt", "r")
lines = file.readlines()

answer = 0

for line in lines:
    line = formatString(line)
    
    cubes = [0, 0, 0]
    for i in range(2, len(line)):
        
        if line[i].isnumeric():
            match line[i+1]:
                case "red":
                    if cubes[0] < int(line[i]):
                        cubes[0] = int(line[i])
                case "green":
                    if cubes[1] < int(line[i]):
                        cubes[1] = int(line[i])
                case "blue":
                    if cubes[2] < int(line[i]):
                        cubes[2] = int(line[i])
    answer += cubes[0] * cubes[1] * cubes[2]
print(answer)