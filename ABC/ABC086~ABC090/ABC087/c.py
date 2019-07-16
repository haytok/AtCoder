N = int(input())
A = list(int(i) for i in input().split())
B = list(int(i) for i in input().split())
result = 0

if N == 1:
    result = A[0] + B[0]
else:
    for i in range(N-1):
        result = max(result, sum(A[:i+1]) + sum(B[i:]))

print(result)