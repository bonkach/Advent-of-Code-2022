def check(tree, trees, n):
    x = tree[0]
    y = tree[1]
    up = True
    for i in range(0, x):
        if trees[(i, y)] >= trees[(x, y)]:
            up = False
            break
    down = True
    for i in range(n, x, -1):
        if trees[(i, y)] >= trees[(x, y)]:
            down = False
            break
    left = True
    for i in range(0, y):
        if trees[(x, i)] >= trees[(x, y)]:
            left = False
            break
    right = True
    for i in range(n, y, -1):
        if trees[(x, i)] >= trees[(x, y)]:
            right = False
            break
    return up or down or left or right


trees = dict()
with open('input.txt') as f:
    all = f.readlines()
    for i in range(len(all)):
        row = all[i].strip()
        for j in range(len(row)):
            trees[(i, j)] = int(row[j])
visibles = 0
for tree in trees:
    if tree[0] == 0 or tree[0] == len(all) - 1 or tree[1] == 0 or tree[1] == len(all) - 1:
        visibles += 1
    else:
        visibles += check(tree, trees, len(all) - 1)
print(visibles)