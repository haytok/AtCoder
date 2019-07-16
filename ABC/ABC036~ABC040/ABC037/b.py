N, Q = map(int, input().split())
ans = [0] * N

for i in range(Q):
    start, end, value = map(int, input().split())
    for i in range(start-1, end):
        ans[i] = value

for i in ans:
    print(i)