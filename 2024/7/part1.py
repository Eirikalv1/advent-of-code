lines = [(int(line.split(':')[0]), list(map(int, line.split(':')[1].split()))) for line in open('input.txt')]

def eval_left_to_right(numbers_and_ops):
    numbers = numbers_and_ops[::2]
    ops = numbers_and_ops[1::2]

    result = numbers[0]

    for i, op in enumerate(ops):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]

    return result

reachables = set()

for target, numbers in lines:
    eqs = [[numbers[0]]]
    for i in range(1, len(numbers)):
        new_eqs = []
        for eq in eqs:
            new_eqs.append(eq + ['+', numbers[i]])
            new_eqs.append(eq + ['*', numbers[i]])
        eqs = new_eqs
    [reachables.add(target) for eq in eqs if eval_left_to_right(eq) == target] 
    
print(sum(reachables))