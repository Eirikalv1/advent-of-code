import random

rules, updates = open('input.txt').read().split('\n\n')
rules = list(map(lambda x: list(map(int, x.split('|'))), rules.split()))
updates = list(map(lambda x: list(map(int, x.split(','))), updates.split()))

def count_rules(num, checks):
    count = 0
    for rule in rules:
        for check in checks:
            if rule[0] == num and rule[1] == check:
                count += 1
    return count

def check_update(update):
    checks = []
    for num in update:
        if count_rules(num, checks) == 0:
            checks.append(num)
        else: 
            return False
    return True

def custom_sort(update):
    checks = []
    for i in range(len(update)):
        if count_rules(update[i], checks) == 0:
            checks.append(update[i])
            continue
        tmp = update.copy()
        pos = random.randint(0, len(update)-1)
        tmp[i], tmp[pos] = tmp[pos], tmp[i]
        if count_rules(update[i], checks) > count_rules(tmp[i], checks):
            update = tmp.copy()
            checks.append(update[i])
    return update
              
total = 0
for update in updates:
    if not check_update(update):
        while not check_update(update):
            update = custom_sort(update)
        total += update[len(update)//2]
print(total)