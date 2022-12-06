# Day 5 Part 1
import re
import time

with open('day5.txt') as file:
    data = file.read()

instructions = data.split('\n\n')[1].split('\n')

starting = {
    1: ['G', 'F', 'V', 'H', 'P', 'S'],
    2: ['G', 'J', 'F', 'B', 'V', 'D', 'Z', 'M'],
    3: ['G', 'M', 'L', 'J', 'N'],
    4: ['N', 'G', 'Z', 'V', 'D', 'W', 'P'],
    5: ['V', 'R', 'C', 'B'],
    6: ['V', 'R', 'S', 'M', 'P', 'W', 'L', 'Z'],
    7: ['T', 'H', 'P'],
    8: ['Q', 'R', 'S', 'N', 'C', 'H', 'Z', 'V'],
    9: ['F', 'L', 'G', 'P', 'V', 'Q', 'J'],
}
pattern = re.compile(r'^\D*(\d*)\D*(\d*)\D*(\d*)$')

def decode(instructions):
    # will return the quantity, source and destination for each instruction
    for line in instructions:
        match = pattern.match(line)
        qty, src, dst = map(int, match.groups())
        for itn in range(qty):
            crate = starting[src].pop()
            starting[dst].append(crate)
    return starting

"""s = time.time_ns()
x = decode(instructions)
for stack in x.values():
    result = stack.pop()
print(time.time_ns()-s)"""

#========================================================
# Day 5 Part 2

def p2decode(instructions):
    for line in instructions:
        match = pattern.match(line)
        qty, src, dst = map(int, match.groups())
        tmp = [starting[src].pop() for _ in range(qty)][::-1]
        [starting[dst].append(crate) for crate in tmp]
    return starting

"""s = time.time_ns()
x = p2decode(instructions)
_= ''.join(stack.pop() for stack in x.values())
print(time.time_ns() - s)
"""