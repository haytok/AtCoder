N = int(input())
station = [[int(i) for i in input().split()] for j in range(N-1)]

for i in range(N):
    time = 0
    for j in range(i, N-1):
        c, s, f = station[j]
        if time < s:
            time = s
        elif time % f == 0:
            pass
        else:
            time += f - (time % f)
        time += c
    print(time)
