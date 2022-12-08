s = set()
with open('input.txt') as f:
    buffer = f.read().strip()
    for i in range(len(buffer)):
        if len(buffer[i : i + 14]) == len(set(buffer[i : i + 14])):
            break
print(i + 14)
