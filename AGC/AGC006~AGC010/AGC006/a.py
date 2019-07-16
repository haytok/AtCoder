N = int(input())
s = input()
t = input()

for i in range(N):
    if s[i:] == t[:N-i]:
        ans = N + i
        break
else:
    ans = N * 2

print(ans)
