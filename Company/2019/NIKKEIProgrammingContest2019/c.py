N = int(input())
inputs = [list(map(int, input().split())) for _ in range(N)]

dicts = {}
for i in range(N):
    dicts[i] = sum(inputs[i])

ans = 0
count = 0
for key, value in sorted(dicts.items(), key=lambda x: -x[1]):
    if count % 2 == 0:
        ans += inputs[key][0]
    else:
        ans -= inputs[key][1]
    count += 1

print(ans)
