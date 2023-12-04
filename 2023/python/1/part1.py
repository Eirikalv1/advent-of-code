import re

lines = open("input.txt", "r").readlines()
num = 0
for line in lines:
    num += int(re.search(r"\d", line).group() \
        + re.search(r"\d", line[::-1]).group())
print(num)