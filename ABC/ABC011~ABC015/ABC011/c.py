n = int(input())
ng = [int(input()) for _ in range(3)]

dp = [1000 for i in range(n+1)]

dp[n] = 0

# for文を逆から回している
# 最低でも-1で引き続ければ試行が終了する
for i in range(n+1)[::-1]:
    print(i, dp)
    if i in ng:
        continue
    for w in range(1,4):
        print(dp)
        if i - w >= 0:
            dp[i-w] = min(dp[i] + 1, dp[i-w])
    print(dp)
print(dp)  
if n in ng:
    print('NO')
elif dp[0] <= 100:
    print('YES')
else:
    print('NO')