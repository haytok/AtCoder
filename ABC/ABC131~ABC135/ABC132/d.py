from scipy.misc import comb

N, K = map(int, input().split())

mod = 10**9 + 7

for i in range(1, K+1):
    blue = comb(K-1, i-1, exact=True)
    red_count = N - K
    red = comb(red_count+1, i, exact=True)
    print(blue * red % mod)
