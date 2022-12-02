#=================================================================
# Day 2 Part 1

# two columns
# first is what the opponent plays, A, B, C for Rock, Paper, Scissors respectively
# assume the second is what I should play, X, Y, Z for Rock, Paper, Scissors respectively

# score of a round is Shape I selected (Rock=1, Paper=2, Scissors=3) + Outcome of the round (Loss=0, Draw=3, Win=6)

# example strategy guide
# A - Y (Rock vs Paper, 2pts for Paper, 6pts for win, 8 total)
# B - X (Paper vs Rock, 1pt for Rock, 0 for loss, 1 total)
# C - Z (Scissors vs Scissors, 3pts for Scissors, 3pts for draw, 6 total)
# Total score of 15 (8+1+6)

# Given a strategy guide, what would be my total score?

#with open('day2.txt') as file:
#   strategy = list(map(lambda x: x.strip('\n'), file.readlines()))

my_move = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}
from itertools import permutations
# winloss = list(filter(lambda item: item if item[1] not in ['A', 'B', 'C'] and item[0] not in ['X', 'Y', 'Z'] else None, permutations('ABCXYZ', r=2)))

winloss = {
    ('A', 'X'): 3, 
    ('A', 'Y'): 6,
    ('A', 'Z'): 0,
    ('B', 'X'): 0,
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,
    ('C', 'X'): 6,
    ('C', 'Y'): 0,
    ('C', 'Z'): 3
}


def score_calc(strategy_entry: str) -> int: 
    # A = X = Rock, B = Y = Paper, C = Z = Scissors
    score = 0
    opp, me = strategy_entry.split(' ')
    score += my_move[me]
    score += winloss[(opp, me)]
    return score

#print(sum(list(map(score_calc, strategy))))
#============================================================
# Day 2 Part 2

# two columns
# first is what the opponent plays, A, B, C for Rock, Paper, Scissors respectively
# second is how the round needs to end
# X = Need to lose, Y = Need to draw, Z = Need to win
# A - Y > Need to draw so pick Rock, 1pt for rock, 3pts for draw, 4 total
# B - X > Need to lose so pick Rock, 1pt for rock, 0pts for loss, 1 total
# C - Z > Need to win so pick Rock, 1pt for rock, 6pts for win,   7 total
# 12 total points

#Total score with new calculations
with open('day2.txt') as file:
    strategy = list(map(lambda x: x.strip('\n'), file.readlines()))

result = {
    ('A', 'X'): 0+3, 
    ('A', 'Y'): 3+1,
    ('A', 'Z'): 6+2,
    ('B', 'X'): 0+1,
    ('B', 'Y'): 3+2,
    ('B', 'Z'): 6+3,
    ('C', 'X'): 0+2,
    ('C', 'Y'): 3+3,
    ('C', 'Z'): 6+1
}

def score_calc(strategy_entry: str) -> int:
    score = 0
    opp, me = strategy_entry.split(' ')
    score += result[(opp, me)]
    return score

print(sum(list(map(score_calc, strategy))))
