N, D, K = map(int, input().split())
distance = [list(map(int, input().split())) for _ in range(D)]

for _ in range(K):
    day = 0
    start, end = map(int, input().split())
    if start < end:
        for i in range(D):
            day += 1
            if distance[i][0] <= start < distance[i][1]:
                if end <= distance[i][1]:
                    print(day)
                    break
                else:
                    start = distance[i][1]
    else:
        for i in range(D):
            day += 1
            if distance[i][0] <= start <= distance[i][1]:
                if end >= distance[i][0]:
                    print(day)
                    break
                else:
                    start = distance[i][0]