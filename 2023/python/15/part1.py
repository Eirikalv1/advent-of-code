line = open("input.txt", "r").read().strip()

def hash_func(string):
    value = 0
    for c in string:
        value = ((value + ord(c)) * 17) % 256
    return value

total = sum(list(map(hash_func, line.split(','))))
print(total)