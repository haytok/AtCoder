N = int(input())
inputs = [int(i) for i in input().split()]

flag = -1
ans = 1

for i in range(1, N):
    first = inputs[i-1]
    latter = inputs[i]
    if flag == -1:
        flag = int(first < latter)
    elif flag == 1:
        if first > latter:
            flag = -1
            ans += 1
    elif flag == 0:
        if first < latter:
            flag = -1
            ans += 1

print(ans)
