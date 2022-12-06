score = 0
with open('input.txt') as f:
    all = f.readlines()
    for i in range(0, len(all), 3):
        first = all[i]
        second = all[i + 1]
        third = all[i + 2]
        for a in first:
            if a in second and a in third:
                    break
        if a.islower():
            score += ord(a)-96
        else:
            score += ord(a)-38
print(score)