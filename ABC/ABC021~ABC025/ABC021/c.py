n = range(int(input()))
i1 = lambda x: int(x) - 1

a, b = map(i1, input().split())
m = int(input())
# 入力データのデータ構造
eg = [[] for _ in n]
for i in range(m):
	x, y = map(i1, input().split())
	eg[x] += [y]
	eg[y] += [x]

# 初期化した行列を生成
d = [[0 for i in n] for j in n]
# スタート地点を設定
d[0][a] = 1
f = 0
# 初期化した行列を編集していくため
for i in n:
    # どのノードがどのノード隣接しているかの情報を回すため
    for j in n:
        for k in eg[j]:
            # この処理がわからん
            # i+1 は次の状態の各ノードの場合の数
            d[i+1][k] += d[i][j]
            if d[i+1][b] > 0:
                f = 1
    if f == 1:
        print(d[i+1][b] % (10**9 + 7))
        break