most = 0
with open('input.txt') as f:
    all = f.readlines()
    s = 0
    for cal in all:
        if cal != '\n':
            s += int(cal)
        else:
            most = max(s, most)
            s = 0
print(most)
