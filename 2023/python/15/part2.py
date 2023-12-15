line = open("input.txt", "r").read().strip().split(',')

def hashed(string):
    value = 0
    for c in string:
        value = ((value + ord(c)) * 17) % 256
    return value

boxes = {}

for step in line:
    if step[-1].isdigit():
        box = hashed(step.split('=')[0])
        if not box in boxes: 
            boxes[box] = []

        for i, v in enumerate(boxes[box]):
            if step[:-2] == v[:-2]:
                boxes[box][i] = step
                break
        else:
            boxes[box].append(step)
    else:
        box = hashed(step[:-1])
        if not box in boxes: continue

        for i, v in enumerate(boxes[box]):
            if step[:-1] == v[:-2]:
                boxes[box].pop(i)
            
            if len(boxes[box]) == 0: 
                del boxes[box]

total = 0
for box, boxVal in boxes.items():
    for i, boxC in enumerate(boxVal):
        total += (box + 1) * (i + 1) * int(boxC[-1])
print(total)