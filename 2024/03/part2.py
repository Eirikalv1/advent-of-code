import re

e = True

def mul(x, y):
    if e:
        return x * y
    else:
        return 0

def do(): 
    global e
    e = True
    return False
    
def dont(): 
    global e
    e = False
    return False

pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

lines = open("input.txt").read()

print(sum(map(eval, map(lambda x: x.replace('\'', ''), re.findall(pattern, lines)))))