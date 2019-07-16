N = int(input())
F = [int(input().replace(" ", ""), 2) for j in range(N)]
P = [[int(i) for i in input().split()] for j in range(N)]
result = float("-inf")

for i in range(1, 1024):
    price = 0
    for j in range(N):
        price += P[j][bin(i&F[j]).count("1")]
    result = max(result, price)

print(result)