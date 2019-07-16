N, K = map(int, input().split())
inputs = [int(i) for i in input().split()]

partly_sum = sum(inputs[:K])
ans = partly_sum
index = K

for i in range(1, N-K+1):
    partly_sum += (inputs[index] - inputs[i-1])
    ans += partly_sum
    index += 1

print(ans)
