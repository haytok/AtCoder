N = int(input())
inputs = [int(i) for i in input().split()]

ans = 0
tmp = 0
for i in range(1, N):
    if inputs[i-1] <= inputs[i]:
        pass
    else:
        ans += (inputs[i-1] - tmp)
        tmp = inputs[i]

if inputs[-1] > tmp:
    ans += inputs[-1] - tmp

print(ans)
