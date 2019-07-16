N, M = map(int, input().split())
input_list = [[int(i) for i in input().split()] for j in range(M)]

ans = 1
first = 0
latter = 0

for i in range(M):
    if i == 0:
        first = input_list[i][0]
        latter = input_list[i][1]
    else:
        if first == input_list[i][0]:
            pass
        else:
            if latter == input_list[i][0] + 1:
                ans += 1
                first = input_list[i][0]
                latter = input_list[i][1]
            elif latter == input_list[i][0]:
                ans += 1
                first = input_list[i][0]
                latter = input_list[i][1]
            else:
                first = input_list[i][0]
                if latter > input_list[i][1]:
                    latter = input_list[i][1]

print(ans)