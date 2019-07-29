N = int(input())
inputs = [[int(i) for i in input().split()] for _ in range(N)]

if N == 1:
    print(max(inputs[0]))
else:
    # dp[i]には1, 2, 3を選択した時の幸福度の最大値を入れている
    dp = [[0, 0, 0] for _ in range(N)]
    dp[0] = inputs[0]
    for i in range(N):
        dp[i][0] = max(dp[i-1][1] + inputs[i][0], dp[i-1][2] + inputs[i][0])
        dp[i][1] = max(dp[i-1][2] + inputs[i][1], dp[i-1][0] + inputs[i][1])
        dp[i][2] = max(dp[i-1][0] + inputs[i][2], dp[i-1][1] + inputs[i][2])

    print(max(dp[-1]))
