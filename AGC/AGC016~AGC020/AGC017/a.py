N, P = map(int, input().split())

for i in input().split():
    if int(i) % 2 == 0:
        continue
    else:
        print(2 ** (N - 1))
        break
else:
    if P == 0:
        print(2 ** N)
    else:
        print(0)
