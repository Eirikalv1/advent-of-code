import re
import math

sizex, sizey = 101, 103

def move(robot, cycles):
    robot[0] = (robot[0] + robot[2] * cycles) % sizex
    robot[1] = (robot[1] + robot[3] * cycles) % sizey
    return robot

lines = open('input.txt').read().splitlines()
for l, line in enumerate(lines):
    lines[l] = list(map(int, re.findall(r'-?\d+', line)))

robots = dict()
for l, line in enumerate(lines):
    robot = move(line, 100)
    key = (robot[0], robot[1])
    robots[key] = robots.get(key, 0) + 1
    
quads = [0, 0, 0, 0]
for robot in robots:
    x, y = robot[0], robot[1]
    if x > sizex // 2 and y > sizey // 2: quads[0] += robots[robot]
    if x > sizex // 2 and y < sizey // 2: quads[1] += robots[robot]
    if x < sizex // 2 and y > sizey // 2: quads[2] += robots[robot]
    if x < sizex // 2 and y < sizey // 2: quads[3] += robots[robot]

print(math.prod(quads))