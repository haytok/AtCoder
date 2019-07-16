R, C, W = map(int, input().split())
inputs = [list(map(int, input().split())) for _ in range(R)]

ans = []
# i はすなはち移動できる距離のこと。
for i in range(W+1):
    if (W % 2) == (i % 2):
        for j in range(i+1):
            row, col = j, i - j
            if row < R and col < C:
                ans.append(inputs[row][col])

print(max(ans))
