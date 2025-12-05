from icecream import ic

fresh, available = open("input.txt", "r").read().split('\n\n')
fresh = list(map(lambda x: x.split('-'), fresh.split('\n')))
fresh = list(map(lambda x: range(int(x[0]), int(x[1])+1), fresh))
available = list(map(int, available.split('\n')))

total = 0
for i in available:
    for j in fresh:
        if i in j:
            total += 1
            break
print(total)