from collections import Counter
from itertools import accumulate

N = int(input())
inputs = [int(i) for i in input().split()]

ans = 0

ruisekiwa = list(accumulate(inputs))

for key, value in Counter(ruisekiwa).items():
    if key == 0 and value == 1:
        ans += value
        continue
    elif key == 0 and value > 1:
        ans += value
    if value > 1:
        ans += value * (value - 1) // 2

print(ans)
