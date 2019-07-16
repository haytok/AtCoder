N, Y = map(int, input().split())

if Y >= N*1000:
    for i in range(N+1):
        if (Y / 1000 - N) - 9 * i >= 0 and int(((Y / 1000 - N) - 9 * i) % 4) == 0:
            y =((Y / 1000 - N) - 9 * i) / 4
            if int(N-i-y)>= 0 and 10000*i+5000*int(y)+1000*int(N-i-y) == Y:
                print(i, int(y), int(N-i-y))
                break
        elif i == N:
            print('-1 -1 -1')
else:
    print('-1 -1 -1')