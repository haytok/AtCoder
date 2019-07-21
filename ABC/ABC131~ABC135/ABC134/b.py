N, D = map(int, input().split())

mod = 2 * D + 1
print(N // mod + (1 if N % mod != 0 else 0))