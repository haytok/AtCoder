N = int(input())
inputs = [int(i) for i in input().split()]

ans = [0 for _ in range(N)]
for i in range(N-1, -1, -1):
    if sum(ans[i::i+1]) % 2 != inputs[i]:
        ans[i] = 1

print(ans.count(1))
result = ''
for i in range(N):
    if ans[i] == 1:
        result += str(i+1) + ' '
print(result)

"""
問題分を読み間違えるし、出力の方法も間違えたから、よくわからん問題やった。
"""