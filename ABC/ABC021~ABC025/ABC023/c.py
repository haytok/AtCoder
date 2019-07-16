from collections import Counter

R, C, K = map(int, input().split())
N = int(input())
inputs = [[int(i) for i in input().split()] for _ in range(N)]


r = [0]*R
c = [0]*C
result = 0

for row, col in inputs:
    r[row-1] += 1
    c[col-1] += 1

# 例
# 1個が1列, 2個が2列 / 0個が2列, 1個が1列, 2個が2列
r_C = Counter(r)
c_C = Counter(c)

for i in range(K+1):
    result += r_C[i] * c_C[K-i]

for i, j in inputs:
    count = r[i-1] + c[j-1]
    if count == K:
        result -= 1
    if count == K+1:
        result += 1

print(result)
