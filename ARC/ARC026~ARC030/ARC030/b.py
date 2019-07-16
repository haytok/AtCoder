N, start = map(int, input().split())
start -= 1
inputs = [int(i) for i in input().split()]

nodes = [[] for _ in range(N)]
for i in range(N-1):
    first, latter = map(lambda x: int(x) - 1, input().split())
    nodes[first].append(latter)
    nodes[latter].append(first)

visited = [False] * N
ans = 0

def dfs(start):
    global ans
    # 初回時のことを考慮してここにif文は設けていない
    visited[start] = True
    exist = inputs[start]
    # 連結先に関して処理を行っていく
    for node in nodes[start]:
        if visited[node]:
            continue
        # そのノードが値を返す、すなはち宝物が存在する時その辺を移動する勝ちがあるとみなせる
        # 再帰関数やから値が決定するのは末端から
        if dfs(node):
            ans += 2
            exist = 1
    return exist

dfs(start)

print(ans)
