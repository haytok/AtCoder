N = int(input())
inputs = [complex(*map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, abs(inputs[i] - inputs[j]))

print(ans)