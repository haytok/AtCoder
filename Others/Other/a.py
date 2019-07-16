H, W = map(int, input().split())
input_list = [[1 for _ in range(W)] for _ in range(H)]

x_direction = [-1, 0, 1, 0]
y_direction = [0, 1, 0, -1]
ans = 0

def dfs(x, y):
    global input_list

    input_list[x][y] = 0

    for row, col in zip(x_direction, y_direction):
        xx = x + row
        yy = y + col
        if xx >= 0 and yy >= 0 and xx < H and yy < W and input_list[xx][yy] == 1:
            dfs(xx, yy)

for i in range(H):
    for j in range(W):
        if input_list[i][j] == 1:
            dfs(i, j)
            ans += 1

print(ans)