import numpy as np

N, W = map(int, input().split())
inputs = np.array([np.array([int(i) for i in input().split()]) for _ in range(N)])

dp = np.zeros(W+1, dtype=np.int64)
for n in range(1, N+1):
    weight, value = inputs[n-1][0], inputs[n-1][1]
    dp[weight:] = np.maximum(dp[weight:], dp[:-weight] + value)

print(dp[-1])

"""
配列の操作にこういう性質がある。
a = [0, 1, 2, 3, 4]
a[:] -> [0, 1, 2, 3, 4]
a[:-1] -> [0, 1, 2, 3] (配列の長さ + 値の長さの配列が返る)
a[:-2] -> [0, 1, 2]
a[:-3] -> [0, 1]
a[:-4] -> [0]
"""
