N, T = map(int, input().split())

inputs = [int(input()) for _ in range(N)]

time = inputs[0]
ans = 0

for i in range(1, N):
    interval = inputs[i] - inputs[i-1]
    if interval > T:
        ans += T
    else:
        ans += interval

ans += T

print(ans)
