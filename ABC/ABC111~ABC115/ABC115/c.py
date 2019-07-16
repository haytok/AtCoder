N, K = map(int, input().split())
inputs = [int(input()) for _ in range(N)]

inputs.sort()
diff = 10**19

for i in range(N-K+1):
    diff = min(diff, inputs[i+K-1] - inputs[i])

print(diff)