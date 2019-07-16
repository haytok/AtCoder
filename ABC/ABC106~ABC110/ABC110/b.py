N, M, X, Y = map(int, input().split())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]

x.sort()
y.sort()

for i in range(x[-1]+1, y[0]+1):
    if X < i <= Y:
        print('No War')
        break
else:
    print('War')
