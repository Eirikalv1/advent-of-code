rules, updates = open('input.txt').read().split('\n\n')
rules = list(map(lambda x: list(map(int, x.split('|'))), rules.split()))
updates = list(map(lambda x: list(map(int, x.split(','))), updates.split()))

def check_rule(num, checks):
    for rule in rules:
        for check in checks:
            if rule[0] == num and rule[1] == check:
                return False
    return True 

def check_update(update):
    checks = []
    for num in update:
        if check_rule(num, checks):
            checks.append(num)
        else: 
            return False
    return True
            
total = 0
for update in updates:
    total += check_update(update) * update[len(update)//2]
print(total)