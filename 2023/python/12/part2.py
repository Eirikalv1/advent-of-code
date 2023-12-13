from collections import Counter
from itertools import product
import re

LINES = open("input.txt", "r").readlines()
cache = {}

def format():
    springs, stats = [], []
    for line in LINES:
        springs.append(re.findall(r"[.#?]+", line)[0])
        stats.append(tuple(map(int, re.findall(r"\d+", line))))

    return springs, stats

def from_unknown(springs, i, perms):
    if i == len(springs):
        perms.append(springs)
        return 

    if springs[i] == '?':
        for char in ['.', '#']:
            springs = springs[:i] + char + springs[i+1:]
            from_unknown(springs, i+1, perms)
    else: from_unknown(springs, i+1, perms)

def to_stats(springs):
    stats = []
    springs = '.' + springs
    assert springs[0] == "."
    for i, char in enumerate(springs[1:]):
        if char == "#" and springs[i] == ".":
            stats.append(1)
        elif char == "#" and springs[i] == "#": stats[-1] += 1

    return tuple(stats)

def unknown_to_stats(springs):
    if springs in cache:
        return cache[springs]
    
    perms = []
    from_unknown(springs, 0, perms)
    all_stats = Counter([to_stats(p) for p in perms])
    cache[springs] = all_stats

    return all_stats

def count_arrangements(springs, stats):
    filtered = list(filter(None, springs.split('.')))
    filtered = list(map(unknown_to_stats, filtered))

    count = 1
    for group in product(*filtered):
        if sum(group, ()) == stats:
            for left, right in zip(group, filtered):
                count *= right[left]
    return count

count = 0
all_springs, all_stats = format()
for springs, stats in zip(all_springs, all_stats):
    count += count_arrangements(springs, stats)
print(count)