N = input()

ans = ''

for i in range(len(N)):
    if N[i] == '1':
        ans += '9'
    else:
        ans += '1'

print(ans)

# 別解
# d = {'1':'9', '9':'1'}
# print(''.join(d[c] for c in input()))

# x = input().replace("1", "X").replace("9", "1").replace("X", "9")
# print(x)