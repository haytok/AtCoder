import sys
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
inputs = [int(input()) for _ in range(M)]

set_inputs = set(inputs)
mod = 10 ** 9 + 7
dp = [0 for _ in range(N+1)]
dp[0] = 1
for i in range(1, N+1):
    if i in set_inputs:
        continue
    if i == 1:
        dp[i] = dp[i-1]
    else:
        if i - 1 not in set_inputs:
            dp[i] += dp[i-1]
        if i - 2 not in set_inputs:
            dp[i] += dp[i-2]

print(dp[-1] % mod)
