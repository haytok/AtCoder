# いもす法

from itertools import accumulate
from operator import add

N, Q = map(int, input().split())

table = [0] * N

for i in range(Q):
    start, end = map(int, input().split())
    table[start-1] += 1
    if end < N:
        table[end] -= 1

# 累積和に変換
table = list(accumulate(table, add))

print(''.join('1' if i % 2 == 1 else '0' for i in table))

# N, Q = map(int, input().split())

# table = [False] * N

# for i in range(Q):
#     start, end = map(int, input().split())
#     table[start-1:end] = list(map(lambda x: not x, table[start-1:end]))

# print(''.join('1' if i else '0' for i in table))