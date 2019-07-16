A, B = map(int, input().split())
S = input()
if S[A] == "-":
    if "-" in S[:A] or "-" in S[A+1:]:
        print("No")
    else:
        print("Yes")
else:
    print("No")