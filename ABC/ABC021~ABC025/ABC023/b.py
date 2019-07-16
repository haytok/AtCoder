N = int(input())
S = input()

count = 1 + (N - 1) // 2
ans = ''

for i in range(count):
    if i == 0:
        ans = 'b'
    elif i % 3 == 1:
        ans = 'a' + ans + 'c'
    elif i % 3 == 2:
        ans = 'c' + ans + 'a'
    elif i % 3 == 0:
        ans = 'b' + ans + 'b'

if ans == S:
    print((N - 1) // 2)
else:
    print(-1)
