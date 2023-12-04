def extendLines(lines):
    for line in range(len(lines)):
        lines[line] = lines[line].strip()
        lines[line] += "."
        lines[line] += "."
    return lines

def getSymbols(lines):
    symbols = []
    for line in range(len(lines)):
        for part in range(len(lines[line])):
            if lines[line][part] != "." and not lines[line][part].isnumeric() and not lines[line][part] == "\n":
                symbols.append((part, line))
    return symbols

def getNumbers(lines):
    numbers = []
    for line in range(len(lines)):
        num = ("", 9999, 9999)
        for part in range(len(lines[line])):
            if lines[line][part].isdigit():
                if part < num[1]:
                    num = (num[0] + lines[line][part], part, line)
                else:
                    num = (num[0] + lines[line][part], num[1], line)
            elif num[0]:
                numbers.append((int(num[0]), num[1], num[2]))
                num = ("", 9999, 9999)
        if num[0]:
            numbers.append((int(num[0]), num[1], num[2]))
    
    return numbers

def adjacent(numbers, symbols):
    total = 0
    for sym in symbols:
        for num in numbers:
            dx = num[1] - sym[0]
            dy = sym[1] - num[2]
            allowed = [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 1), (0, -1), (-1, 0), (-1, -1)]

            if len(str(num[0])) == 2 or len(str(num[0])) == 3:
                allowed.extend([(-2, 1), (-2, 0), (-2, -1)])
            if len(str(num[0])) == 3:
                allowed.extend([(-3, 1), (-3, 0), (-3, -1)])

            if (dx, dy) in allowed:
                total += num[0]
    print(total)
                
                

file = open("input.txt", "r")
lines = file.readlines()

lines =  extendLines(lines)
symbols = getSymbols(lines)
numbers = getNumbers(lines)

adjacent(numbers, symbols)
