# 動的計画法
# dp[i] は１本目の柱からi本目の柱へ移動するまでの合計コストの最小値

N = int(input())
inputs = [int(i) for i in input().split()]

dp = [0] * N
dp[1] = abs(inputs[0]-inputs[1])

for i in range(2, N):
    # a = dp[i-2] + min(abs(inputs[i]-inputs[i-2]), abs(inputs[i]-inputs[i-1] + abs(inputs[i-1]-inputs[i-2])))
    # これは間違いで、これのmin()の第二引数はbと同じ
    a = dp[i-2] + abs(inputs[i]-inputs[i-2])
    b = dp[i-1] + abs(inputs[i]-inputs[i-1])
    dp[i] = min(a, b)

print(dp[-1])