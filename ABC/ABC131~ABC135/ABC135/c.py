N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

ans = 0
for i in range(N):
    # モンスターのほうが多い
    if B[i] <= A[i]:
        ans += B[i]
    elif B[i] > A[i]:
        ans += A[i]
        B[i] -= A[i]
        if B[i] <= A[i+1]:
            ans += B[i]
            A[i+1] -= B[i]
        elif B[i] > A[i+1]:
            ans += A[i+1]
            A[i+1] = 0
print(ans)