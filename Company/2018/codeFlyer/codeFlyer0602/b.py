A, B, N = map(int, input().split())
S = input()

for i in range(N):
    if S[i] == "S":
        if A > 0:
            A -= 1
    elif S[i] == "C":
        if B > 0:
            B-= 1
    elif S[i] == "E":
        if A > B:
            A -= 1
        elif A < B:
            B -= 1
        elif A == 0 and B == 0:
            pass
        elif A == B:
            A -= 1
print(A)
print(B)