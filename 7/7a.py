path = ['/']
dirs = dict()
sizes = dict()
with open('input.txt') as f:
    all = f.readlines()
    for expr in all[1:]:
        expr = expr.strip().split()
        if expr[1] == 'cd':
            if expr[2] != '..':
                if path[-1] not in dirs:
                    dirs[path[-1]] = [expr[2]]
                else:
                    dirs[path[-1]].append(expr[2])
                path.append(path[-1] + expr[2])
            else:
                path.pop()
        if expr[0].isnumeric():
            for val in path:
                if val not in sizes:
                    sizes[val] = int(expr[0])
                else:
                    sizes[val] += int(expr[0])
summ = 0
for key, value in sizes.items():
    if value <= 100000:
        summ += value
print(summ)