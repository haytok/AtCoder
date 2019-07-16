N = 4
# (w, v)
inputs = [[2, 3], [1, 2], [3, 4], [2, 2]]
W = 5

dp = [[-1] * (W + 1)  if i != N else [0] * (W + 1) for i in range(N + 1)]

# i番目以降の品物から重さの総和がw以下になるように選択する
def cal():
    global dp

    for i in range(N-1, -1, -1):
        for w in range(W+1):
            if w < inputs[i][0]:
                dp[i][w] = dp[i+1][w]
            else:
                dp[i][w] = max(dp[i+1][w], dp[i+1][w-inputs[i][0]] + inputs[i][1])

    print(dp[0][W])


if __name__ == '__main__':
    cal()