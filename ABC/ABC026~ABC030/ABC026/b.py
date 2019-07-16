from math import pi

N = int(input())
inputs = [int(input()) for _ in range(N)]

inputs.sort(reverse=True)
flag = 1
ans = 0

for i in inputs:
    ans += flag * (i ** 2)
    flag *= -1

print(ans * pi)
