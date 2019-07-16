from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

R, C = map(int, input().split())
# y座標, x座標の順に書いてある
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
inputs = [input() for _ in range(R)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

change_map = []
index = 0

for y in range(R):
    item = []
    for x in range(C):
        item.append(index)
        index += 1
    change_map.append(item)

y_item = []
x_item = []

for y, input in enumerate(inputs):
    for x, item in enumerate(input):
        tmp = []
        if item == '.':
            for a, b in zip(dx, dy):
                try:
                    if inputs[y+b][x+a] == '.':
                        tmp.append([y+b, x+a])
                except IndexError:
                    pass
        for t in tmp:
            y_item.append(change_map[y][x])
            x_item.append(change_map[t[0]][t[1]])
        tmp = []

cost = [1]*len(y_item)
d_map = dijkstra(csr_matrix((cost, (x_item, y_item))))

print(int(d_map[change_map[sy-1][sx-1], change_map[gy-1][gx-1]]))
