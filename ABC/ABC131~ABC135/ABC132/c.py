from bisect import bisect

N = int(input())
inputs = sorted([int(i) for i in input().split()])

ans = 0
for i in range(inputs[-1] + 1):
    index = bisect(inputs, i)
    if index == (N // 2):
        ans += 1
    elif index > (N // 2):
        break
print(ans)
