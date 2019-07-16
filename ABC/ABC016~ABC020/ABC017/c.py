N, M = map(int, input().split())
sum = [0] * (M+2)
total_cost = 0

for n in range(N):
    start, end, value = map(int, input().split())
    total_cost += value
    sum[start] += value
    sum[end+1] -= value

for i in range(M+1):
    sum[i+1] += sum[i]

print(total_cost - min(sum[1:M+1]))