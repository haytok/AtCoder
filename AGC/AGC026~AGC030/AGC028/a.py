N, M = map(int, input().split())
S = input()
T = input()

# ユークリッドの互除法
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

length = N * M // gcd(N, M)

if S[0::length//M] == T[0::length//N]:
    print(length)
else:
    print(-1)
