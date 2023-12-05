def format_inp(lines):
    seeds = []
    seed_map = {}

    current_map = ""
    for line in lines:
        line = line.split()
        if line == []: continue
        
        if line[0] == "seeds:": 
            seeds = line[1:]
        elif line[0][0].isalpha():
            seed_map[line[0]] = []
            current_map = line[0]
        else:
            line = [int(x) for x in line]
            seed_map[current_map].append(line)

    seeds = [int(x) for x in seeds]
    return seeds, seed_map

lines = open("input.txt", "r").readlines()
seeds, seed_map = format_inp(lines)

lowest = 9999999999999
for seed in seeds:
    for k, v in seed_map.items():
        for r in v:
            if seed in range(r[1], r[1] + r[2]):
                seed += r[0] - r[1]
                break
    if seed < lowest: lowest = seed
print(lowest)