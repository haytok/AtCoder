N = int(input())

input_list = []
index = 1
for i in input().split():
    item = int(i) - index
    input_list.append(item)
    index += 1

input_list.sort()
b = input_list[N//2]

print(sum(map(lambda x: abs(x-b), input_list)))
