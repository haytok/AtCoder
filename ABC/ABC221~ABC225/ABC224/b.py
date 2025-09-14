def main():
    H, W = map(lambda s: int(s), input().split(' '))
    A = [list(map(lambda s: int(s), input().split(' '))) for _ in range(H)]

    for i1 in range(1, H):
        for i2 in range(i1+1, H+1):
            for j1 in range(1, W):
                for j2 in range(j1+1, W+1):
                    if A[i1-1][j1-1] + A[i2-1][j2-1] > A[i2-1][j1-1] + A[i1-1][j2-1]:
                        print('No')
                        return
    print('Yes')

if __name__ == '__main__':
    main()
