s = input()
k = int(input())

ans = []
count = len(s) - k + 1

if count < 0:
    print(0)
else:
    for i in range(count):
        if s[i:i+k] not in ans:
            ans.append(s[i:i+k])
    print(len(ans))
