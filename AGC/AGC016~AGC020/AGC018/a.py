N, K = map(int, input().split())
inputs = [int(i) for i in input().split()]

def gcd(a, b):
    while b:
	    a, b = b, a % b
    return a

tmp = inputs[0]
if K in inputs:
    print('POSSIBLE')
elif max(inputs) < K:
    print('IMPOSSIBLE')
else:
    if N == 1:
        if K == inputs[0]:
            print('POSSIBLE')
        else:
            print('IMPOSSIBLE')
    else:
        for i in range(1, N):
            tmp = gcd(tmp, inputs[i])
        if tmp == 1:
            print('POSSIBLE')
        else:
            if (max(inputs) - K) % tmp == 0:
                print('POSSIBLE')
            else:
                print('IMPOSSIBLE')
