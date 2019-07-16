inputs = list(map(int, input().split()))
K = inputs.pop()

ans = inputs[0] - inputs[1]

print(-1 if abs(ans) > 10 ** 18 else ans * ((-1)**K))
