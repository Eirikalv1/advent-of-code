import re

mul = lambda x, y: x * y

pattern = r"mul\(\d{1,3},\d{1,3}\)"

lines = open("input.txt").read()

print(sum(map(eval, re.findall(pattern, lines))))