import numpy as np

N = int(input())
inputs = np.array([float(i) for i in input().split()])

dp = np.array([np.array([0.0 for _ in range(N+1)]) for _ in range(N+1)])
dp[1][0] = 1 - inputs[0]
dp[1][1] = inputs[0]
for i in range(2, N+1):
    dp[i][1:] = dp[i-1][1:] * (1.0 - inputs[i-1]) + dp[i-1][:N] * inputs[i-1]
    dp[i][0] = dp[i-1][0] * (1.0 - inputs[i-1])

print(sum(dp[-1][(N+1)//2:]))
