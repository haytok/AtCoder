N, K = map(int, input().split())
inputs = [int(input()) for _ in range(N)]

seki = 1
ans = 0
right = 0

if 0 in inputs:
    ans = N
elif min(inputs) > K:
    pass
else:
    for left in range(N):
        # この時点ではleftは固定されている
        while right <= N-1 and seki * inputs[right] <= K:
            seki *= inputs[right]
            right += 1
        # while が抜けたときには条件を満たさなくなったので、rightが余分
        ans = max(ans, right-left)
        seki //= inputs[left]
        if left == right:
            right += 1

print(ans)
