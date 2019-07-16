N, M, A, B = map(int, input().split())
inputs = [int(input()) for _ in range(M)]

for i in range(M):
    if N <= A:
        N += B

    N -= inputs[i]

    if N < 0:
        print(i + 1)
        break
else:
    print('complete')
