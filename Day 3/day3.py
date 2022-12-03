# Day 3 Part 1

# each line is a single rucksack
# 1st half of a line is in one compartment, 2nd half in the other

# x = 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'
# print(x[:len(x)//2])
# in this rucksack, L is in both compartments, so 38 would be the priority assigned to that rucksack
# Priorities; a - z = 1 - 26, A - Z = 27 - 52

import string

priorities = dict([i[::-1] for i in enumerate(string.ascii_lowercase+string.ascii_uppercase, start=1)])
#print(priorities)


with open('day3.txt') as file:
    rucksacks = list(map(lambda x: x.strip('\n'), file.readlines()))



def item_finder(rucksack) -> int:
    first, second = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    first = set(first)
    second = set(second)
    common = first.intersection(second).pop()
    print(common)
    return priorities[common]


#print(sum(map(item_finder, rucksacks)))

#==================================================================
# Day 3 Part 2

# Go through rucksacks in 3-chunks
# find the common item, sum the priotities of that common item

from itertools import zip_longest

def grouper(iterable, n):
    args = [iter(iterable)] * n
    return list(zip_longest(*args))

def badge_finder(group) -> int:
    badge = set.intersection(*list(map(set, group)))
    return priorities[badge.pop()]
    

groups = grouper(rucksacks, 3)
print(sum(map(badge_finder, groups)))