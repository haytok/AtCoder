N, M = map(int, input().split())

mod = (10**9 + 7)

def factorial(n):
    for i in range(1, n):
        n *= i
        if n > mod:
            n %= mod
    return n

if N == M:
    a = factorial(M)
    print(a ** 2 * 2 % mod)
elif abs(N-M) == 1:
    print(factorial(N) * factorial(M) % mod)
else:
    print(0)
