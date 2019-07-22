L, R = map(int, input().split())

mod = 2019
ans = 10 ** 7
results = [False for _ in range(2019)]
for low in range(L, R+1):
    for up in range(low+1, R+1):
        ans = min(ans, low * up % mod)
        if ans == 0:
            print(ans)
            exit()
print(ans)
