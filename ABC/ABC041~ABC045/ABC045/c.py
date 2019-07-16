S = input()

ans = 0
count_list = [[2 ** (len(S)-1)]]

for i in range(1, len(S)):
    if i == 1:
        count_list.append([2 ** (len(S)-2), 2 ** (len(S)-2)])
    else:
        a = []
        for j in count_list[i-1][:i-1]:
            a.append(j)
        a.append(count_list[i-1][-1]//2)
        a.append(count_list[i-1][-1]//2)
        count_list.append(a)

count_list = count_list[::-1]

for i in range(len(S)):
    flag = 1
    for j in count_list[i]:
        ans += int(S[i]) * flag * j
        flag *= 10

print(ans)