N, x = map(int, input().split())
input_list = [int(i) for i in input().split()]
result = 0

for i in range(N-1):
    count = 0
    if input_list[i] + input_list[i+1] > x:
        count = (input_list[i] + input_list[i+1] - x)
        result += count
        if input_list[i+1] < count:
            input_list[i+1] = 0
            input_list[i] -= (count - input_list[i+1])
        else:
            input_list[i+1] -= count

print(result)