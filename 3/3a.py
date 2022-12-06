score = 0
with open('input.txt') as f:
    all = f.readlines()
    for comp in all:
        comp = comp.strip()
        first = comp[:len(comp)//2]
        second = comp[len(comp)//2:]
        for a in first:
            if a in second:
                break
        if a.islower():
            score += ord(a)-96
        else:
            score += ord(a)-38
print(score)