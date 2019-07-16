N, X = map(int, input().split())
distance = [abs(int(i)-X) for i in input().split()]

ans = distance[0]

# ユークリッドの互除法
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

for i in range(N):
    ans = gcd(ans, distance[i])

print(ans)
