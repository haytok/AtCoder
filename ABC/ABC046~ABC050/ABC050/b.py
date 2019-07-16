N = int(input())
T_list = [int(i) for i in input().split()]
M = int(input())
M_list = [[int(i) for i in input().split()] for i in range(M)]

base_value = sum(T_list)

for i in range(M):
    print(base_value - (T_list[M_list[i][0]-1] - M_list[i][1]))