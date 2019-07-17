# これがないとREで落ちるので、深い再帰を実装する際には書いておく
import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
inputs = [list(input()) for _ in range(H)]

start_h, start_w = 0, 0
for row in range(H):
    if 's' in inputs[row]:
        start_h = row
        start_w = inputs[row].index('s')

# ベクトルの向きを間違える, この場合は斜めしか進めない
# vectors = [[-1, 1], [-1, -1], [1, -1], [1, 1]]
# visited = [[False for _ in range(W)] for _ in range(H)]

def compute(h, w):
    global inputs #, visited
    # 終了条件
    if h < 0 or w < 0 or h >= H or w >= W:
        return False
    if inputs[h][w] == '#':
        return False
    if inputs[h][w] == 'g':
        return True
    
    # visited[h][w] = True
    inputs[h][w] = '#'
    return compute(h, w + 1) or compute(h, w - 1) or compute(h + 1, w) or compute(h - 1, w)

print('Yes' if compute(start_h, start_w) else 'No')