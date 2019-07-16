s = int(input())

items = [s]
while True:
    if s % 2 == 0:
        s = s // 2
    else:
        s = 3 * s + 1
    if s not in items:
        items.append(s)
    else:
        print(len(items)+ 1)
        break
