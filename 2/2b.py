score = 0
with open('input.txt') as f:
    all = f.readlines()
    for game in all:
        single = game.strip().split()
        if single[0] == 'A':
            if single[1] == 'X':
                score += 3
            elif single[1] == 'Y':
                score += 4
            else:
                score += 8
        if single[0] == 'B':
            if single[1] == 'X':
                score += 1
            elif single[1] == 'Y':
                score += 5
            else:
                score += 9
        if single[0] == 'C':
            if single[1] == 'X':
                score += 2
            elif single[1] == 'Y':
                score += 6
            else:
                score += 7
print(score)

