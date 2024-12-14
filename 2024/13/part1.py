from sympy import symbols, Eq, solve

eqs = open('input.txt').read().split('\n\n')

tokens = 0
for i in range(len(eqs)):
    _, _, a1, a2, _, _, b1, b2, _, p1, p2 = \
        map(lambda x: int(x[2:].replace(',','')) if x[2:].replace(',','').isdigit() else x, eqs[i].split())
    
    a, b = symbols('a b')
    eq1 = Eq(a1 * a + b1 * b, p1)
    eq2 = Eq(a2 * a + b2 * b, p2)
    sols = solve((eq1, eq2), (a, b))

    assert len(sols) == 2

    tokens += 3 * sols[a] + sols[b] if sols[a].is_integer and sols[b].is_integer else 0
print(tokens)