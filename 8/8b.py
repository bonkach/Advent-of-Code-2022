def check(tree, trees, n):
    x = tree[0]
    y = tree[1]
    cup = 0
    for i in range(x - 1, -1 , -1):
        if trees[(i, y)] < trees[(x, y)]:
            cup += 1
        else:
            cup += 1
            break
    cdown = 0
    for i in range(x + 1, n + 1):
        if trees[(i, y)] < trees[(x, y)]:
            cdown += 1
        else:
            cdown += 1
            break
    cleft = 0
    for i in range(y - 1, -1, -1):
        if trees[(x, i)] < trees[(x, y)]:
            cleft += 1
        else:
            cleft += 1
            break
    cright = 0
    for i in range(y + 1, n + 1):
        if trees[(x, i)] < trees[(x, y)]:
            cright += 1
        else:
            cright += 1
            break
    return cup * cleft * cright * cdown


trees = dict()
with open('input.txt') as f:
    all = f.readlines()
    for i in range(len(all)):
        row = all[i].strip()
        for j in range(len(row)):
            trees[(i, j)] = int(row[j])
maxy = 0
for tree in trees:
    if tree[0] == 0 or tree[0] == len(all) - 1 or tree[1] == 0 or tree[1] == len(all) - 1:
        continue
    else:
        maxy = max(maxy, check(tree, trees, len(all) - 1))
print(maxy)