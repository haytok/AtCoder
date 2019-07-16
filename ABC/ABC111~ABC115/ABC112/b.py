N, T = map(int, input().split())

ans = 10 ** 9

for _ in range(N):
    a, b = map(int, input().split())
    if b <= T:
        ans = min(ans, a)

if ans == 10 ** 9:
    print('TLE')
else:
    print(ans)