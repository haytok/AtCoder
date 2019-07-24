N, X = map(int, input().split())
inputs = [int(i) for i in input().split()]

D = 0
ans = 1 if D <= X else 0
for item in inputs:
    D += item
    if D <= X:
        ans += 1

print(ans)
