N, M, C = map(int, input().split())
B = [int(i) for i in input().split()]
inputs = [[int(i) for i in input().split()] for _ in range(N)]

ans = 0
for i in range(N):
    if C + sum([a * b for a, b in zip(inputs[i], B)]) > 0:
        ans += 1

print(ans)
