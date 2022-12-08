path = ['/']
call = 0
cc = 0
with open('input.txt') as f:
    all = f.readlines()
    for expr in all[1:]:
        expr = expr.strip().split()
        if expr[1] == 'cd':
            if expr[2] != '..':
                path.append(expr[2])
                cc = 0
            else:
                if cc < 100000:
                    call += cc + cc * len(path)
                path.pop()
        if expr[0].isnumeric():
            cc += int(expr[0])
            print(cc)
print(call)
print(path) 
