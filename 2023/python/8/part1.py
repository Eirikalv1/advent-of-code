cycle, _, *instructions = open("input.txt", "r").read().splitlines()

network = {}
for instruction in instructions:
    left, right = instruction.split(" = ")
    network[left] = right[1:-1].split(", ")

steps = 0
current = "AAA"
while current != "ZZZ":
    if cycle[0] == "L": current = network[current][0]
    else: current = network[current][1]
    cycle = cycle[1:] + cycle[0]
    steps += 1
print(steps)