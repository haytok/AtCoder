N = int(input())

result = 1
mod = 10**9+7

for i in range(1, N+1):
    result *= i
    result %= mod

print(result)