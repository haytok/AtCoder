N = int(input())
inputs = [int(i) for i in input().split()]

if sum(inputs) % N != 0:
    print(-1)
else:
    ans = 0
    count = 0
    ave = sum(inputs) // N
    for i in range(N-1):
        if inputs[i] != ave:
            inputs[i+1] += inputs[i] - ave
            ans += 1
    print(ans)
