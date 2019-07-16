import bisect

N = int(input())
inputs = [int(input()) for _ in range(N)]

mod = 10 ** 9 + 7
inputs.sort()
print(inputs)

third = [0] * N
for i in range(N):
    third[i] = N - bisect.bisect_left(inputs, inputs[i] * 2)

print(third)
