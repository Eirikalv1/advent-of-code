lines = [(int(line.split(':')[0]), list(map(int, line.split(':')[1].split()))) for line in open('input.txt')]

def eval_left_to_right(eq):
    result = eq[0]
    i = 1 
    
    while i < len(eq) - 1:
        operator = eq[i]
        operand = eq[i + 1]
        
        if operator == '||':
            result = int(str(result) + str(operand))
        if operator == '+':
            result += operand
        if operator == '*':
            result *= operand
        
        i += 2

    return result

reachables = []

for target, numbers in lines:
    eqs = [[numbers[0]]]
    for i in range(1, len(numbers)):
        new_eqs = []
        for eq in eqs:
            new_eqs.append(eq + ['+', numbers[i]])
            new_eqs.append(eq + ['*', numbers[i]])
            new_eqs.append(eq + ['||', numbers[i]])
        eqs = new_eqs
    result = [target for eq in eqs if eval_left_to_right(eq) == target]
    if result: reachables.append(result[0])

print(sum(reachables))