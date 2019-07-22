N = int(input()) # 奇数
inputs = [int(i) for i in input().split()]

double_inputs = list(map(lambda x: x * 2, inputs))
ans = [0 for _ in range(N)]
for i in range(N):
    if i == 0:
        ans[i] = sum(inputs) - sum(double_inputs[1::2])
    elif i == N - 1:
        ans[i] = double_inputs[-1] - ans[0]
    else:
        ans[i] = double_inputs[i-1] - ans[i-1]

print(' ' .join(map(str, ans)))
