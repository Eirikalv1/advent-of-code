filesystem = list(open('input.txt').read().strip())
expanded = []
file_id = 0

for i, block in enumerate(filesystem):
    for _ in range(int(block)):
        if i % 2 == 0:
            expanded.append(file_id)
        else:
            expanded.append('.')
    if i % 2 == 0:
        file_id += 1

for _ in range(expanded.count('.')):
    expanded[expanded.index('.')] = expanded[-1]
    expanded.pop()

checksum = sum(i * block for i, block in enumerate(expanded) if block != '.')
print(checksum)