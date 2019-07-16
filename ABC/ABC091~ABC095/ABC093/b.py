A, B, K = map(int, input().split())

first = [i for i in range(A, B+1)] if A + K >= B else [i for i in range(A, A+K)]
latter = [i for i in range(B-K+1, B+1)] if B - K >= A else [i for i in range(A, B+1)]

for i in sorted(list(set(first + latter))):
    print(i)
