A = int(input())

ans = 0

for i in range(1, A//2 + 1):
    ans = max(ans, i * (A-i))

print(ans)

# 相加平均、相乗平均を使うともっと楽に解ける