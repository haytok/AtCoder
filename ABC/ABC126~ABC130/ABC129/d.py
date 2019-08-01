import numpy as np

H, W = map(int, input().split())
inputs = np.array([list(input()) for _ in range(H)])
grid = inputs == '.'

# 左から右に処理を行う
vertical_1 = np.zeros((H, W), dtype=int)
vertical_1[:, 0] = grid[:, 0]
for i in range(1, W):
    vertical_1[:, i] = (vertical_1[:, i-1] + 1) * grid[:, i]

# 右から左に処理を行う
vertical_2 = np.zeros((H, W), dtype=int)
vertical_2[:, -1] = grid[:, -1]
for i in range(W-2, -1, -1):
    vertical_2[:, i] = (vertical_2[:, i+1] + 1) * grid[:, i]

# 上から下に処理を行う
down_1 = np.zeros((H, W), dtype=int)
down_1[0] = grid[0]
for i in range(1, H):
    down_1[i] = (down_1[i-1] + 1) * grid[i]

# 右から左に処理を行う
down_2 = np.zeros((H, W), dtype=int)
down_2[-1] = grid[-1]
for i in range(H-2, -1, -1):
    down_2[i] = (down_2[i+1] + 1) * grid[i]

print((vertical_1 + vertical_2 +  down_1 + down_2 - 3).max())
