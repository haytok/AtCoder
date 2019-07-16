N, K = map(int, input().split())
inputs = [int(i) for i in input().split()]

inputs.sort()
ans = 0

for item in inputs[N-K:]:
    ans = (ans + item) / 2

print(ans)
