S = input()
T = input()

cnt = 0
clist = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for i in range(len(S)):
    if S[i].islower():
        S = S.replace(S[i], clist[cnt])
        cnt += 1

cnt = 0
for i in range(len(T)):
    if T[i].islower():
        T = T.replace(T[i], clist[cnt])
        cnt += 1

if S == T:
    print('Yes')
else:
    print('No')
