H, W = map(int, input().split())
P = [input() for i in range(H)]

result = ""
vektor = [
    [-1, -1],
    [-1, 0], 
    [-1, 1], 
    [0, -1], 
    [0, 1],
    [1, -1],
    [1, 0], 
    [1, 1]
    ]

for i in range(H):
    for j in range(W):
        if P[i][j] == "#":
            result += "#"
        else:
            count = 0
            for k in range(8):
                try:
                    if i+vektor[k][0] >= 0 and j+vektor[k][1] >= 0 and P[i+vektor[k][0]][j+vektor[k][1]] == "#":
                        count += 1
                except IndexError:
                    pass
            result += str(count)

start = 0
for i in range(0, H*W+1, W):
    print(result[start:i])
    start = i
