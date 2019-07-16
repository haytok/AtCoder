# H * W の行列をする
H, W = map(int, input().split())
field = [list(input()) for i in range(H)] 
count = 0

for i in range(H):
    for j in range(W):
        # 注目している点が#でその上下左右が#でないときにcountが加算される
        # このcountが1以上になると、#が孤立していることになり、Noが出力される
        if (i == 0 and j == 0) or (i == H-1 and j == 0) or (i == 0 and j == W-1) or (i == H-1 and j == W-1):
            pass
        elif i == 0:
            if field[i][j] == '#' and field[i][j-1] != '#' and field[i][j+1] != '#' and field[i+1][j] != '#':
                count += 1
        elif i == H-1:
            if field[i][j] == '#' and field[i][j-1] != '#' and field[i][j+1] != '#' and field[i-1][j] != '#':
                count += 1
        elif j == 0:
            if field[i][j] == '#' and field[i][j-1] != '#' and field[i][j+1] != '#' and field[i+1][j] != '#':
                count += 1
        elif j == W-1:
            if field[i][j] == '#' and field[i][j-1] != '#' and field[i+1][j] != '#' and field[i-1][j] != '#':
                count += 1
        elif field[i][j] == '#' and field[i][j-1] != '#' and field[i][j+1] != '#' and field[i+1][j] != '#' and field[i-1][j] != '#':
            count += 1
print('No' if count>=1 else 'Yes')