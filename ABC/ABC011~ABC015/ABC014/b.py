n, X = map(int, input().split())
inputs = [int(i) for i in input().split()]


if X == 0:
    print(0)
else:
    binary_number = '0' + bin(X)[2:]
    ans = 0
    reverse_binary_number = binary_number[::-1]
    for b, i in zip(reverse_binary_number, inputs):
        ans += int(b) * i

    print(ans)
