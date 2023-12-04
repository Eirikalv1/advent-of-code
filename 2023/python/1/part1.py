lines = open("input.txt", "r").readlines()
num = 0
for line in lines:
    digits = [char for char in line if char.isdigit()]
    num += int(digits[0] + digits[-1])
print(num)