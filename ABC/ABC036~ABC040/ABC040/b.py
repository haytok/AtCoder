n = int(input())

ans = 10 ** 20

for i in range(1, n+1):
    sum = abs((n // i) - i) + n % i
    ans = min(ans, sum)

print(ans)