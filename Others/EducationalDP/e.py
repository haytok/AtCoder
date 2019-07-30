import numpy as np

N, W = map(int, input().split())
inputs = np.array([np.array([int(i) for i in input().split()]) for _ in range(N)])

dp = np.full(N*1000+1, 10 ** 10, dtype=np.int64)
dp[0] = 0
for n in range(1, N+1):
    weight, value = inputs[n-1][0], inputs[n-1][1]
    dp[value:] = np.minimum(dp[value:], dp[:-value] + weight)

print(np.max(np.where(dp <= W)))

"""
dp = np.zeros(W+1, dtype=np.int64) やと、メモリで落ちる。
numpy.where()はnumpy.array()の各要素とある値との比較をし、条件を満たす値のインデックスをタプルで返す。
"""
