# 頂点の情報をリストに格納
# 各頂点毎にＤＦＳを逐次実行
# 
def dfs(s):
    # usedは訪れたノードを入れたリスト
    global used, G
    used.add(s)
    for t in G[s]:
        if t not in used:
            dfs(t)

N, M = map(int, input().split())
es = []
G = [[] for i in range(N)]
for i in range(M):
    a, b = [int(i) - 1 for i in input().split()]
    # 隣接リストの作成
    G[a].append(b)
    G[b].append(a)
    # ペアのindex
    es.append([a, b])
    print(a, b)

print(G)
print("==========")
print(es)
ans = 0
for a, b in es:
    # ある頂点と隣接する頂点の辺を削除
    G[a].remove(b)
    G[b].remove(a)
    used = set()
    dfs(0)
    # 連結なら、集合に入ってる数は頂点の数に等しくなる
    # すなはち、等しくないなら、連結ではないと言える
    if len(used) != N:
        ans += 1
    # 上述で削除されたある頂点と隣接する頂点の辺を元に戻す
    G[a].append(b)
    G[b].append(a)

print(ans)


