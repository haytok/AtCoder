N = int(input())
inputs = [[int(i) for i in input().split()] for _ in range(N)]

ans = 0

for input in inputs[::-1]:
    A, B = input[0], input[1]
    A += ans
    if A % B != 0:
        ans += B - (A % B)

print(ans)
