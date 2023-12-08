from math import lcm

def path(current, cycle, network):
    steps = 0
    while current[2] != "Z":
        if cycle[0] == "L": current = network[current][0]
        else: current = network[current][1]
        cycle = cycle[1:] + cycle[0]
        steps += 1
    return steps

cycle, _, *instructions = open("input.txt", "r").read().splitlines()

network = {}
for i in range(len(instructions)):
    left, right = instructions[i].split(" = ")
    network[left] = right[1:-1].split(", ")

paths = [path(i, cycle, network) for i in network if i[2] == "A"]
print(lcm(*paths))