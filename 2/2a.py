score = 0
with open('input.txt') as f:
    all = f.readlines()
    for game in all:
        single = game.strip().split()
        if single[1] == 'X':
            score += 1
            if single[0] == 'A':
                score += 3
            elif single[0] == 'C':
                score += 6
        elif single[1] == 'Y':
            score += 2
            if single[0] == 'A':
                score += 6
            elif single[0] == 'B':
                score += 3
        else:
            score += 3
            if single[0] == 'B':
                score += 6
            elif single[0] == 'C':
                score += 3
print(score)

