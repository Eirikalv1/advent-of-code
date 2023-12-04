def formatString(line):
    line = line.replace(":","")
    line = line.replace(";"," ; ")
    line = line.replace(",","")
    line = line.split()
    line.append(";")
    return line

def checkCubes(cubes):
    return True if cubes[0] <= 12 and cubes[1] <= 13 and cubes[2] <= 14 else False

file = open("input.txt", "r")
lines = file.readlines()

answer = 0

for line in lines:
    line = formatString(line)
    
    cubes = [0, 0, 0]
    failed = False
    for i in range(2, len(line)):
        if line[i] == ";":
            print(cubes)
            if not checkCubes(cubes): 
                failed = True
                break
            cubes = [0, 0, 0]
        
        if line[i].isnumeric():
            match line[i+1]:
                case "red":
                    cubes[0] = int(line[i])
                case "green":
                    cubes[1] = int(line[i])
                case "blue":
                    cubes[2] = int(line[i])
    if not failed: answer += int(line[1])

print(answer)