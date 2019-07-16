H, W = map(int, input().split())
input_list = [[i for i in input()] for j in range(H)]

option = ["#"]*(W+2)
input_list.insert(0, option)
input_list.append(option)

for i in range(1, H+1):
    input_list[i].insert(0, "#")
    input_list[i].append("#")

for i in range(H+2):
    print("".join(input_list[i]))
