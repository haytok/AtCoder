from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
from math import ceil

H, W, T = map(int, input().split())
inputs = []
indexs = []
index = 0

# 入力の初期化処理
for h in range(H):
    inputs.append([])
    indexs.append([])
    row_input = input()
    for w in range(W):
        string = row_input[w]
        inputs[h].append(string)
        indexs[h].append(index)
        if string == 'S':
            S_index = index
        if string == 'G':
            G_index = index
        index += 1

def get_cost(x, string):
    return x if string == '#' else 1

def cal_total_cost(x):
    cost_between_nodes = []
    for h in range(H):
        for w in range(W):
            # ノード間のコストを表現するデータ構造を作成
            # [あるノード, あるノード, 移動コスト]
            if h < H - 1:
                cost_between_nodes.append([indexs[h][w], indexs[h+1][w], get_cost(x, inputs[h+1][w])])
                cost_between_nodes.append([indexs[h+1][w], indexs[h][w], get_cost(x, inputs[h][w])])
            if w < W - 1:
                cost_between_nodes.append([indexs[h][w+1], indexs[h][w], get_cost(x, inputs[h][w])])
                cost_between_nodes.append([indexs[h][w], indexs[h][w+1], get_cost(x, inputs[h][w+1])])
    # h, w, cost にはタプルでデータが入っている
    h, w, cost = zip(*cost_between_nodes)
    d_map = dijkstra(csr_matrix((cost, (h, w))))
    return d_map[S_index, G_index]

max_cost = 10**9
min_cost = 0

while True:
    center = ceil((min_cost + max_cost) / 2)
    if cal_total_cost(max_cost) > T:
        max_cost = center
    else:
        min_cost, max_cost = max_cost, max_cost + center

    if max_cost - min_cost == 1:
        break

# 境界における値を評価
print(max_cost if cal_total_cost(max_cost) <= T else min_cost)
