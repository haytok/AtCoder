S = input()

indexes = []
for i in range(len(S)):
    if S[i] == 'R' and S[i+1] == 'L':
        indexes.append(i)

