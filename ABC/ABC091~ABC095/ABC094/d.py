import math

n = int(input())
data = [int(i) for i in input().split()]
data.sort()
result = 0
index = []
resultIndex = []

def nCm(m, n):
    return math.factorial(n) / (math.factorial(m) * (math.factorial(n - m)))

for i in range(n) :
    for j in range(i+1, n):
        if result < nCm(data[i], data[j]):
            result = nCm(data[i], data[j])
            index.append((i, j))
resultIndex = index.pop()
print(data[resultIndex[0]], data[resultIndex[1]])