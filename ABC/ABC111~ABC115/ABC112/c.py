def inpl():
    return list(map(int, input().split()))

import numpy as np

N = int(input())
X = np.zeros(N, dtype=np.int64)
Y = np.zeros(N, dtype=np.int64)
H = np.zeros(N, dtype=np.int64)

# Hの降順でリストに入れてる
Q = sorted([inpl() for _ in range(N)], key=lambda x: x[2], reverse=True)

for i, q in enumerate(Q):
    X[i], Y[i], H[i] = q

# 求めるべき値のCx, Cy は0以上100以下の整数なので、全探索する
# そうすると、H の値が決まるので、その条件が他の入力に対して成り立つかを検証する
for cx in range(101):
    for cy in range(101):
        cH = H[0] + np.abs(X[0] - cx) + np.abs(Y[0] - cy)
        if np.all(H == np.maximum(cH - np.abs(X - cx) - np.abs(Y - cy), 0)):
            print(cx, cy, cH)