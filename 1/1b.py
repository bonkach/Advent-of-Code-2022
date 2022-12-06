lst = []
with open('input.txt') as f:
    all = f.readlines()
    s = 0
    for cal in all:
        if cal != '\n':
            s += int(cal)
        else:
            lst.append(s)
            s = 0
lst.sort()
print(sum(lst[-3:]))
