L, H = map(int, input().split())
N = int(input())

for _ in range(N):
    i = int(input())
    if i < L:
        print(L-i)
    elif L <= i <= H:
        print(0)
    else:
        print(-1)
