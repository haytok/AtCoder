N = int(input())

ans = 10 ** 15

for a in range(1, N // 2 + 1):
    A, B = a, N - a
    total = sum(map(int, list(str(A)))) + sum(map(int, list(str(B))))
    ans = min(ans, total)

print(ans)
