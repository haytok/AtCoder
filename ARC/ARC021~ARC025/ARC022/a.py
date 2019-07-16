S = input().upper()

string = 'ICT'
length = len(S)
ans = 'NO'
for i in range(length):
    index = 0
    if S[i] == string[index]:
        index += 1
        for j in range(i, length):
            if S[j] == string[index]:
                index += 1
                for k in range(j, length):
                    if S[k] == string[index]:
                        ans = 'YES'
                        print(ans)
                        exit()

print(ans)
