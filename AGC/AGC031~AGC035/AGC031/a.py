from collections import Counter

N = int(input())
S = Counter(input())

mod = 10 ** 9 + 7
ans = 1
for value in S.values():
    ans *= (value + 1)

print((ans - 1) % mod)
