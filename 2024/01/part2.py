lines = open('input.txt').read().strip()

nums = list(map(int, lines.split()))
right, left = nums[::2], nums[1::2]

total = 0
while left:
    total += min(left) * right.count(min(left))
    left.remove(min(left))

print(total)