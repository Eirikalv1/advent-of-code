filesystem = list(open('input.txt').read().strip())
expanded = []
file_id = 0

for i, block in enumerate(filesystem):
    for _ in range(int(block)):
        if i % 2 == 0:
            expanded.append(file_id)
        else:
            expanded.append(-1)
    if i % 2 == 0:
        file_id += 1
        
for current_id in range(max(expanded), 0, -1):
    file_index = expanded.index(current_id)
    file_size = sum(1 for block in expanded if block == expanded[file_index])
    
    for i, _ in enumerate(expanded):
        if i + file_size > len(expanded) - 1 or i >= file_index: break
        if all(expanded[j] == -1 for j in range(i, i + file_size)):
            for j in range(i, i + file_size):
                expanded[j] = expanded[file_index]
            for j in range(file_index, file_index + file_size):
                expanded[j] = -1
            break

print(sum(i * block for i, block in enumerate(expanded) if block != -1))