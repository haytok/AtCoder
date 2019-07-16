b = [[int(j) for j in input().split()] for i in range(2)]
c = [[int(j) for j in input().split()] for i in range(3)]

# 得点の合計
S = sum([sum(i) for i in b]) + sum([sum(j) for j in c])
memo = {}

# 盤の得点を計算する関数
def score(t):
    s = 0
    for i in range(2):
        for j in range(3):
            if t[i+1][j] == t[i][j]:
                s += b[i][j]
    for i in range(3):
        for j in range(2):
            if t[i][j+1] == t[i][j]:
                s += c[i][j]
    return s

def solve(t, turn=1):
    if str(t) in memo:
        return memo[str(t)]
    if turn == 10:
        return score(t)
    bs1 = 0
    bs2 = float('inf')
    for i in range(3):
        for j in range(3):
            # もともとtはNoneで初期化されている
            # すなはち数字が入るとfor文がパス、Noneが入っていると以下の処理が挟まる
            if not t[i][j] is None:
                continue
            t[i][j] = turn % 2
            s = solve(t, turn+1)
            # この箇所が微妙にわからん
            t[i][j] = None
            bs1 = max(bs1, s)
            bs2 = min(bs2, s)
    ret = bs1 if turn % 2 else bs2
    memo[str(t)] = ret
    return ret

ret = solve([[None for j in range(3)] for i in range(3)])
print(ret)
print(S - ret)
