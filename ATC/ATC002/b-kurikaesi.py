N, mod, P = map(int, input().split())

def cal(n, p):
    if p == 0:
        ans = 1
    elif p % 2 == 0:
        ans = cal(n, p//2) ** 2
    else:
        ans = cal(n, p-1) * N
    ans %= mod
    return ans

print(cal(N, P))
