import math

N, P = map(int, input().split())
max_value = round(pow(P, 1/N)) + 1 
ans = 1

if N == 1:
    ans = P
else:
    for i in range(1, max_value):
        mod = i ** N
        if P % mod == 0:
            ans = i

print(ans)
