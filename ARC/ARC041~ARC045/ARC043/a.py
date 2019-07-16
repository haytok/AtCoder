N, A, B = map(int, input().split())
inputs = [int(input()) for _ in range(N)]

diff = max(inputs) - min(inputs)
if diff == 0:
    print(-1)
else:
    P = B / diff
    Q = A - P * sum(inputs) / N
    print(P, Q)
