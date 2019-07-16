S = input()
T = input()
a = ""
for i in range(len(S)+1):
    if i == 0:
        a = (S[-1] + S[:-1])
    else:
        a = a[-1] + a[:-1]
    if a == T:
        print("Yes")
        break
else:
    print("No")

