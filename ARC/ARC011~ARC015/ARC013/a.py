from itertools import permutations

N, M, L = map(int, input().split())
inputs = list(map(int, input().split()))

ans = 0
for item in permutations(inputs):
    P, Q, R = item[0], item[1], item[2]
    ans = max(ans, (N // P) * (M // Q) * (L // R))

print(ans)
