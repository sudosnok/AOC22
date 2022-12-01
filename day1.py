# Day 1 Part 1
with open('day1part1.txt') as file:
    data = file.read()

elves = data.split('\n\n')

each_elf = []

for elf in elves:
    given_elf = sum([int(fooditem) for fooditem in elf.split('\n')])
    each_elf.append(given_elf)

most_food = max(each_elf)
number_elf = each_elf.index(most_food)

# print(most_food, number_elf)

#==============================================================================================================#

# Day 1 Part 2

with open('day1part1.txt') as file:
    data = file.read()

elves = data.split('\n\n')

each_elf = []

for elf in elves:
    given_elf = sum([int(fooditem) for fooditem in elf.split('\n')])
    each_elf.append(given_elf)

sorted_elves = sorted(each_elf, reverse=True)
top_three = sorted_elves[:3]
result = sum(top_three)
print(result)