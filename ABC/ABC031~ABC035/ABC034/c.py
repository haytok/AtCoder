W, H = map(int, input().split())

mod = 10 ** 9 + 7

def fact(n):
    mod = 10 ** 9 + 7
    ans = 1
    for i in range(1, n+1):
        ans = ans * i % mod
    return ans

print(fact(W + H -2) * pow(fact(W-1), mod-2, mod) * pow(fact(H-1), mod-2, mod) % mod)
