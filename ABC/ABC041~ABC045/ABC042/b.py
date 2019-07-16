# 辞書の問題難しい

N, L = map(int, input().split())
inputs = [input() for _ in range(N)]

orderd_inputs = sorted(inputs)

print(''.join(orderd_inputs))