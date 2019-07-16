N = int(input())
K = int(input())

result = 1

for i in range(N):
    if result < K:
        result *= 2
    else:
        result += K 

print(result)
