N = int(input())
inputs = [input() for _ in range(N)][::-1]

for i in range(N):
    ans = ''
    for j in range(N):
        ans = ans + inputs[j][i]
    print(ans)