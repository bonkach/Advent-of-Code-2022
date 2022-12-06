from collections import deque
with open('input.txt') as f:
    all = f.read().split('\n')
    stacks = all[:all.index('') - 1]
    moves = all[all.index('') + 1:]
    nums = all[all.index('') - 1]
    mat = []
    d = dict()
    for row in stacks:
        if row == '':
            break
        for i in range(len(row)):
            if row[i].isalpha():
                if i in d:
                    d[i].append(row[i])
                else:
                    d[i] = deque(row[i])
k = dict()
for a, b in enumerate(sorted(d.keys())):
    k[a + 1] = b
for row in moves:
    row = row.split()
    amount = int(row[1]); start = int(row[3]); end = int(row[5])
    for i in range(amount):
        d[k[end]].appendleft(d[k[start]].popleft())
output = ''
for key, value in sorted(d.items(), key=lambda x:x[0]):
    output += value.popleft()
print(output) 