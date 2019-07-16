x, y = map(int, input().split())

if x >= 0 and y >= 0:
    if y >= x:
        print(y - x)
    else:
        if y == 0:
            print(1 + x - y)
        else:
            print(x - y + 2)
elif x < 0 and y < 0:
    if y >= x:
        print(y - x)
    else:
        print(2 + x - y)
else:
    if y == 0:
        print(abs(x))
    else:
        print(abs(abs(x) - abs(y)) + 1)
