N, M = map(int, input().split())

# データ構造の設定が上手と思った
# 配列の配列にせず、文字列の配列にしている点
A = [input() for j in range(N)]
B = [input() for j in range(M)]

for i in range(N-M+1):
    for j in range(N-M+1):
        for k in range(M):
            if A[i+k][j:j+M] != B[k]:
                break
        else:
            print("Yes")
            exit()
else:
    print("No")

# あんまり頭働いてなかったから、楽しめんかった
# 上述の通り、データ構造が結果を左右したと思う