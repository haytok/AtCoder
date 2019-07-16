N = int(input())
inputs = [int(i) for i in input().split()]

ao = []
ans = - 10 ** 9

for taka in range(N):
    res = [- 10 ** 9, - 10 ** 9]
    for ao in range(N):
        if ao == taka:
            continue
        else:
            if taka < ao:
                part = inputs[taka:ao+1]
            else:
                part = inputs[ao:taka+1]
            a = sum(part[1::2])
            t = sum(part[::2])
            if a > res[1]:
                res = [t, a]
    ans = max(ans, res[0])

print(ans)
