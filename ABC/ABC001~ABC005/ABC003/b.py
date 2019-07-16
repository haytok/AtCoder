S = list(input())
T = list(input())

wirdcard = ['a', 't', 'c', 'o', 'd', 'e', 'r']

for index in range(len(S)):
    if S[index] == '@' and T[index] == '@':
        pass
    elif S[index] == '@':
        if T[index] not in wirdcard:
            print('You will lose')
            break
        else:
            T[index] = '@'
    elif T[index] == '@':
        if S[index] not in wirdcard:
            print('You will lose')
            break
        else:
            S[index] = '@'
else:
    if S == T:
        print('You can win')
    else:
        print('You will lose')
