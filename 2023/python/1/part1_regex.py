import re

lines = open("input.txt", "r").readlines()
print(sum([int(re.search(r"\d", line).group() \
    + re.search(r"\d", line[::-1]).group()) for line in lines]))