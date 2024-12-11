stones = list(map(int, open('input.txt').read().strip().split()))

for b in range(25):
    new_stones = [] 
    for s, stone in enumerate(stones):
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            half = len(str(stone)) // 2
            left, right = int(str(stone)[:half]), int(str(stone)[half:])
            new_stones.extend([left, right])
        else:
            new_stones.append(stone * 2024)
    stones = new_stones
print(len(stones))