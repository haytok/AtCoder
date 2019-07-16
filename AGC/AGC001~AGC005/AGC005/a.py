S_count = 0

for item in input():
    if item == 'S':
        S_count += 1
    elif item == 'T' and S_count > 0:
        S_count -= 1

print(2 * S_count)
