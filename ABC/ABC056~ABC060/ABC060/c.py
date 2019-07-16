N, T = map(int, input().split())
input_list = [int(i) for i in input().split()]

sum_time = 0

for i in range(1, N):
    sum_time += min(T, input_list[i] - input_list[i-1])

print(sum_time + T)