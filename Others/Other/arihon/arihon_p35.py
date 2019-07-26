"""
入力
10 12
W........WW.
.WWW.....WWW
....WW...WW.
.........WW.
.........W..
..W......W..
.W.W.....WW.
W.W.W.....W.
.W.W......W.
..W.......W.

出力
3
"""

import sys
sys.setrecursionlimit(10**9)

H, W = map(int, input().split())
inputs = [list(input()) for _ in range(H)]

vectors = []
for x in range(-1, 2):
    for y in range(-1, 2):
        if x != 0 or y != 0:
            vectors.append([x, y])

def dfs(h, w):
    inputs[h][w] = '.'
    for vector in vectors:
        next_h, next_w = h + vector[0], w + vector[1]
        if 0 <= next_h < H and 0 <= next_w < W and inputs[next_h][next_w] == 'W':
            dfs(next_h, next_w)
    return

ans = 0
for h in range(H):
    for w in range(W):
        if inputs[h][w] == 'W':
            dfs(h, w)
            ans += 1

print(ans)
