cleaning = 0
with open('input.txt') as f:
    all = f.readlines()
    for pair in all:
        pair = pair.strip().split(',')
        a, b = map(int, pair[0].split('-'))
        c, d = map(int, pair[1].split('-'))
        range1 = {i for i in range(a, b + 1)}
        range2 = {i for i in range(c, d + 1)}
        if range1.issubset(range2) or range2.issubset(range1):
            cleaning += 1
print(cleaning)