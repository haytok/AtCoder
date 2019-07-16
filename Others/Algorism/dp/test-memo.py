N = 4
inputs = [[2, 3], [1, 2], [3, 4], [2, 2]]
W = 5

dp = [[-1] * (W + 1) for _ in range(N + 1)]
print(dp)
"""
重さの総和がWを超えないように選んだときの価値の総和が最大となるように
"""

# i番目以降の品物から重さの総和がw以下になるように選択する
def cal(i, w):
    if dp[i][w] >= 0:
        return dp[i][w]
    if i == N:
        res = 0
    # 重さがw以下になるように選択するので重すぎるとと弾く
    elif w < inputs[i][0]:
        res = cal(i+1, w)
    else:
        # 重さの条件をクリア
        # 価値が大きい方を選択
        res = max(cal(i+1, w), cal(i+1, w-inputs[i][0]) + inputs[i][1])
    
    dp[i][w] = res
    
    return dp[i][w]

print(cal(0, W))
