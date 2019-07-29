import numpy as np


N, K = map(int, input().split())
inputs = np.array([int(i) for i in input().split()])

dp = np.zeros(N, dtype=int)
for i in range(1, N):
    start = max(0, i-K)
    dp[i] = (dp[start:i] + abs(inputs[i] - inputs[start:i])).min()

print(dp[-1])


"""
２重for文で計算量がカツカツの時はnumpyを使って行列の足し算を使うと高速化できることがある。
"""