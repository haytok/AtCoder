import math

N = int(input())

ans = 0

def cal(n):
    limit = math.floor(math.sqrt(n))
    count = 0
    for i in range(1, limit+1):
        if n % i == 0:
            if n % i == i:
                count += 1
            else:
                count += 2
    return count

for i in range(1, N+1, 2):
    if cal(i) == 8:
        ans += 1

print(ans)