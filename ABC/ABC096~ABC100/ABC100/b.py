D, N = map(int, input().split())

if D == 0:
    if N == 100:
        print(101)
    else:
        print(N)
elif D == 1:
    if N == 100:
        print(10100)
    else:
        print(100*N)
elif D == 2:
    if N == 100:
        print(1010000)
    else:
        print(10000*N)
