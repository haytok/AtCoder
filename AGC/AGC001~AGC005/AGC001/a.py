N = int(input())
inputs = sorted([int(i) for i in input().split()])

ans = 0
for i in range(N):
    ans += min(inputs[2*i:2*i+1])

print(ans)
