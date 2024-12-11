lines = open('input.txt').read().strip()

nums = list(map(int, lines.split()))
right, left = nums[::2], nums[1::2]

total = 0
while left and right:
    total += abs(min(left) - min(right))
    left.remove(min(left)), right.remove(min(right))

print(total)