from collections import Counter
from itertools import accumulate
from math import factorial

N = int(input())
inputs = [int(input()) for _ in range(N)]

inputs.sort()

mod = 10 ** 9 + 7

counter_inputs = Counter(inputs)

ans = 1
for value in counter_inputs.values():
    ans *= factorial(value)

print(sum(accumulate(inputs)))
print(ans % mod)
