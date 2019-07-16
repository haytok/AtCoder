N, M = map(int, input().split())

# 各頂点とそれ以外の頂点の情報を持たせる
edges = [set() for _ in range(N)]
for _ in range(M):
    node1, node2 = map(lambda x: int(x) - 1, input().split())
    edges[node1].add(node2)
    edges[node2].add(node1)

# 探索開始ノードは配列のインデックスで管理する
visited = [False] * N

def dfs(current, parent=-1):
    visited[current] = True
    for node in edges[current] - { parent }:
        '''
        node = 1, current = 0 のケースなどで考えてみると良い。
        '''
        if visited[node] or dfs(node, current) == 0:
            return 0
    return 1

print(sum([dfs(i) for i in range(N) if not visited[i]]))
