N, C, K = map(int, input().split())
inputs = [int(input()) for _ in range(N)]

inputs.sort()

start = inputs[0]
capa = 1
ans = 1
for i in range(1, N):
    capa += 1
    if start + K < inputs[i] or capa > C:
        ans += 1
        capa = 1
        start = inputs[i]

print(ans)
