# Day 4 Part 1

with open('day4.txt') as file:
    pairs = list(map(lambda x: x.strip('\n'), file.readlines()))

def does_contain(pair):
    a, b = pair.split(',')
    a, b = a.split('-'), b.split('-')
    a = list(map(int, a))
    b = list(map(int, b))
    print(a, b)
    if (a[0] <= b[0]) and (a[1] >= b[1]):
        print('a contains b')
        return 1
    if (b[0] <= a[0]) and (b[1] >= a[1]):
        print('b contains a')
        return 1
    else:
        print('not completely overlapping')
        return 0

#print(sum(map(does_contain,pairs)))

#============================================================
# Day 4 Part 2

def does_overlap(pair):
    a, b = pair.split(',')
    a, b = a.split('-'), b.split('-')
    a = list(map(int, a))
    b = list(map(int, b))
    #print(a, b, any(num in range(b[0], b[1]+1) for num in range(a[0], a[1]+1)))
    if any(num in range(b[0], b[1]+1) for num in range(a[0], a[1]+1)):
        return 1
    else: return 0

print(sum(map(does_overlap, pairs[:])))