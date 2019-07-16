N = int(input())

r = N // 7

for i in range(r+1):
    if (N - 7*i) % 4 == 0:
        print('Yes')
        break
else:
    print('No')