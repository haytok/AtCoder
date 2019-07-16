from itertools import permutations
from math import sqrt

import numpy as np

N = int(input())
inputs = [list(map(int, input().split())) for _ in range(N)]

length = 0
for item in permutations(inputs, 2):
    diff = np.array(item[0]) - np.array(item[1])
    length = max(length, diff[0] ** 2 + diff[1] ** 2)

print(sqrt(length))
