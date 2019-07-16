Q, H, S, D = map(int, input().split()) # 0.25 0.5 1 2
N = int(input())

one_l = min([4 * Q, 2 * Q + H, H * 2, S])
two_l = min([one_l * 2, D])

if N % 2 == 0:
    print(two_l * (N // 2))
else:
    print(two_l * (N // 2) + one_l)
