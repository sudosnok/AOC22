# Day 6 Part 1

import time

with open('day6.txt') as file:
    data = file.read()

def find_marker(input):
    buffer = []
    for count, char in enumerate(input, start=1):
        buffer.append(char)
        tmp = list(buffer)[-4:]
        if len(set(tmp)) == len(tmp) and len(tmp) == 4:
            return count
s = time.time_ns()
res = find_marker(data)
print('Part 1: ', time.time_ns() - s)

#==========================================
# Day 6 Part 2

def find_markerp2(input, size):
    buffer = []
    for count, char in enumerate(input, start=1):
        buffer.append(char)
        tmp = list(buffer)[-size:]
        if len(set(tmp)) == len(tmp) and len(tmp) == size:
            return count
s = time.time_ns()
res = find_markerp2(data, 14)
print('Part 1: ', time.time_ns() - s)