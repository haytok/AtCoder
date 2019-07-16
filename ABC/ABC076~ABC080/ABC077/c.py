from bisect import bisect_right, bisect_left
N = int(input())
A = sorted([int(i) for i in input().split()])
B = sorted([int(i) for i in input().split()])
C = sorted([int(i) for i in input().split()])

count = 0

for b in B:
    i = bisect_left(A, b)
    k = bisect_right(C, b)
    count += i * (N-k)

print(count)