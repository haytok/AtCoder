N = int(input())
inputs = [int(i) for i in input().split()]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

ans = inputs[0]
for i in range(1, N):
    ans = gcd(ans, inputs[i])

print(ans)
