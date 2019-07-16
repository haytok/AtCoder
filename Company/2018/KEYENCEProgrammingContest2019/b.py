N = input()

S = 'keyence'
if S == N[:len(S)]:
    ans = 'YES'
elif S == N[-len(S):]:
    ans = 'YES'
else:
    for index in range(len(S)):
        if S[:index] == N[:index] and S[-(len(S) - index):] == N[-(len(S) - index):]:
            ans = 'YES'
            break
    else:
        ans = 'NO'

print(ans)
