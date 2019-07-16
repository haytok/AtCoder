import math

N, K = map(int, input().split())

mod = 10 ** 9 + 7

# nCr
def combination(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

# nHr (重複組み合わせ)
def combinations_with_replacement(n, r):
    return combination(n + r - 1, r)


print(combinations_with_replacement(N, K) % mod if N > K else combination(N, K % N) % mod)
