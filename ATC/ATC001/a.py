import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
inputs = [list(input()) for _ in range(H)]

for h in range(H):
    row = inputs[h]
    if 's' in row:
        start = [row.index('s'), h]

def dfs(p_x, p_y):
    if not (0 <= p_x < W):
        return False
    if not (0 <= p_y < H):
        return False
    if inputs[p_y][p_x] == '#':
        return False
    if inputs[p_y][p_x] == 'q':
        return False
    if inputs[p_y][p_x] == 'g':
        return True
    
    inputs[p_y][p_x] = 'q'

    return dfs(p_x-1, p_y) or dfs(p_x, p_y+1) or dfs(p_x+1, p_y) or dfs(p_x, p_y-1)


print('Yes' if dfs(start[0], start[1]) else 'No')
