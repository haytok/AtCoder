N, M = map(int, input().split())
inputs = [[int(i) for i in input().split()] for _ in range(N)]

inputs.sort()
count = 0
ans = 0
for A, B in inputs:
    if M < 0:
        break
    ans += A * min(B, M)
    M -= B

print(ans)
