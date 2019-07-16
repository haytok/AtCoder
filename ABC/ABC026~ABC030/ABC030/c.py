# 二分探索
from bisect import bisect_left as left

N, M = map(int, input().split())
X, Y = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

ans = 0
time = 0

while True:
    # A -> B の flight の index
    flight = left(A, time)
    
    if flight == N:
        break

    time = (A[flight] + X)

    # B -> A の flight の index
    flight = left(B, time)

    if flight == M:
        break

    time = (B[flight] + Y)
    ans += 1

print(ans)
