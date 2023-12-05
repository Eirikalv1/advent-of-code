def format_input():
    seeds = []
    seeds_map = []

    lines = open("input.txt", "r").readlines()
    for line in lines:
        line = line.split()
        if line == []: continue
        elif line[0] == "seeds:":
            row = [int(x) for x in line[1:]]
            seeds = [[row[x], row[x] + row[x+1] - 1] for x in range(0, len(row), 2)]
        elif line[0][0].isalpha():
            seeds_map.append([])
        else:
            row = [int(num) for num in line]
            seeds_map[-1].append([row[1], row[1] + row[2] - 1, row[0], row[0] + row[2] - 1])
    return seeds, seeds_map

def map_ranges(seed, source):
    assert seed[0] <= seed[1]
    if seed[0] >= source[0] and seed[1] <= source[1]:
        return [[], seed, []]
    if seed[0] < source[0] and seed[1] > source[1]:
        return [[seed[0], source[0] - 1], source, [source[1] + 1, seed[1]]]
    elif seed[0] >= source[0] and seed[0] <= source[1] and seed[1] > source[1]:
        return [[], [seed[0], source[1]], [source[1] + 1, seed[1]]]
    elif seed[0] < source[0] and seed[1] >= source[0] and seed[1] <= source[1]:
        return [[seed[0], source[0] - 1], [source[0], seed[1]], []]
    elif seed[1] < source[0]:
        return [seed, [], []]
    elif seed[0] > source[1]:
        return [[], [], seed]

    print("Unreachable")

def map_dest(seed, source, dest):
    return [seed[0] - source[0] + dest[0], seed[1] - source[1] + dest[1]]

seeds, seeds_map = format_input()

for category in seeds_map:
    to_dest = []
    for group in category:
        new_seeds = []
        for seed in seeds:
            filtered_group = map_ranges(seed, group[:2])

            if filtered_group[0] != []: new_seeds.append(filtered_group[0])
            if filtered_group[1] != []: to_dest.append([filtered_group[1], group[:2], group[2:]])
            if filtered_group[2] != []: new_seeds.append(filtered_group[2])
        seeds = new_seeds
    dest = [map_dest(x[0], x[1], x[2]) for x in to_dest]
    seeds.extend(dest)
print(min([x[0] for x in seeds]))

