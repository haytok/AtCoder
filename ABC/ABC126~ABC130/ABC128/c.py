N, M = map(int, input().split())
inputs = [list(map(int, input().split())) for _ in range(M)]
P = list(map(int, input().split()))

ans = 0
for i in range(2 ** N):
    bit = format(i, 'b').zfill(N)
    flag = True
    for j in range(M):
        count = 0
        item = inputs[j][1:]
        for number in item:
            if bit[number-1] == '1':
                count += 1
        if count % 2 != P[j]:
            flag = False
    if flag:
        ans += 1

print(ans)
