N = int(input())
inputs = [int(i) for i in input().split()]

for i in range(N-1, 1, -1):
    if inputs[i-1] > inputs[i]:
        inputs[i-1] -= 1

for i in range(1, N):
    if inputs[i-1] > inputs[i]:
        print('No')
        break
else:
    print('Yes')

"""
逆順から考えると良い。この発想は全くなかった。
"""