from shapely.geometry import Polygon, Point 

lines = open("input.txt", "r").read().splitlines()

lines.append("." * len(lines[0]))
lines.insert(0, "." * len(lines[0]))
for i in range(len(lines)): 
    lines[i] = "." + lines[i] + "."


path = []
def getStart():
    for line in range(len(lines)):
        for char in range(len(lines[line])):
            if lines[line][char] == "S": return [char, line, "S"]

def move(current):
    dirs = []
    match current[2]:
        case "S": dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        case "-": dirs = [[1, 0], [-1, 0]]
        case "|": dirs = [[0, 1], [0, -1]]
        case "F": dirs = [[1, 0], [0, 1]]
        case "J": dirs = [[-1, 0], [0, -1]]
        case "L": dirs = [[1, 0], [0, -1]]
        case "7": dirs = [[-1, 0], [0, 1]]
    for dir in dirs:
        if direction(current, dir):
            return direction(current, dir)

def direction(current, dir):
    moves = {
        "right": ["7", "J", "-", "S"],
        "left": ["F", "L", "-", "S"],
        "down": ["L", "J", "|", "S"],
        "up": ["F", "7", "|", "S"]}

    x, y = current[0], current[1]
    match dir:
        case [1, 0]:
            pos = lines[y][x+1]
            if pos in moves["right"] and not [x+1, y, pos] in path:
                return [x+1, y, pos]
        case [-1, 0]:
            pos = lines[y][x-1]
            if pos in moves["left"] and not [x-1, y, pos] in path:
                return [x-1, y, pos]
        case [0, 1]:
            pos = lines[y+1][x]
            if pos in moves["down"] and not [x, y+1, pos] in path:
                return [x, y+1, pos]
        case [0, -1]:
            pos = lines[y-1][x]
            if pos in moves["up"] and not [x, y-1, pos] in path:
                return [x, y-1, pos]

def getDots():
    dots = []
    for y in range(1, len(lines)-1):
        for x in range(1, len(lines[y])-1):
            if not (x, y) in path: dots.append((x, y))
    return dots

current = getStart()
path.append(current)
while True:
    current = move(current)
    if current == None: break
    path.append(current)

for i in range(len(path)):
    path[i] = (path[i][0], path[i][1])

dots = getDots()
polygon = Polygon(path)
points = [dot for dot in dots if polygon.contains(Point(dot))]
print(len(points))