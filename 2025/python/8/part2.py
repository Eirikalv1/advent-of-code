from icecream import ic

points = list(map(lambda x: tuple(list(map(int, x.strip().split(',')))), open("input.txt", "r").readlines()))
distance = lambda p1, p2: pow(pow(p2[0]-p1[0], 2) + pow(p2[1]-p1[1], 2) + pow(p2[2]-p1[2], 2), 0.5)

visited = set()
circuits = list()
firsts = list()

def addToCircuit(p1, p2):
    global circuits, firsts

    existing = [-1, -1]
    for i, circuit in enumerate(circuits):
        if p1 in circuit: existing[0] = i
        if p2 in circuit: existing[1] = i
    
    if existing[0] == -1 and existing[1] == -1:                                 # CASE 1: Boksene finnes ikke i circuits
        circuits.append({p1, p2})
        firsts.append({p1, p2})
    if existing[0] != -1 and existing[1] == -1:                                 # CASE 2: En av boksene finnes
        circuits[existing[0]].update({p1, p2})
    if existing[0] == -1 and existing[1] != -1:                                 # CASE 2: En av boksene finnes
        circuits[existing[1]].update({p1, p2})
    if existing[0] != -1 and existing[1] != -1 and existing[0] == existing[1]:  # CASE 3: Begge boksene finnes i samme circuit
        circuits[existing[0]].update({p1, p2})
    if existing[0] != -1 and existing[1] != -1 and existing[0] != existing[1]:  # CASE 4: Begge boksene finnes, men i forskjellig circuits
        circuits[existing[0]].update(circuits[existing[1]])
        circuits.pop(existing[1])

while True:
    minDistance = float('inf')
    selected = (None, None)
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points):
            if j <= i: continue
            if distance(p1, p2) < minDistance and not (p1, p2) in visited and not (p2, p1) in visited:
                minDistance = distance(p1, p2)
                selected = (p1, p2)
                
    visited.add((selected[0], selected[1]))
    addToCircuit(selected[0], selected[1])
    if len(circuits[0]) == len(points):
        ic(selected[0][0] * selected[1][0])
        break