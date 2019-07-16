from collections import Counter

N, K = map(int, input().split())
input_list = [[int(i) for i in input().split()] for j in range(N)]
input_list.sort()

for element in input_list:
    K -= element[1]
    if K <= 0:
        print(element[0])
        break