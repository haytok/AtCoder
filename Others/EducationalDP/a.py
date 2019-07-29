N = int(input())
inputs = [int(i) for i in input().split()]

dp = [10 ** 9 for _ in range(N)]
dp[0] = 0

for i in range(1, N):
    if i == 1:
        dp[i] = abs(inputs[i] - inputs[i-1])
    else:
        dp[i] = min(dp[i-1] + abs(inputs[i] - inputs[i-1]), dp[i-2] + abs(inputs[i] - inputs[i-2]))

print(dp[-1])
