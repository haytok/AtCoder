# 誤差を許さないときに使うと良い
from decimal import *
import math

N = int(input())
input_list = [[int(i) for i in input().split()] for j in range(N)]

T, A = input_list[0][0], input_list[0][1]

for i in range(1, N):
    n = Decimal(max(math.ceil(T/input_list[i][0]), math.ceil(A/input_list[i][1])))
    T = input_list[i][0] * n
    A = input_list[i][1] * n

print(T + A)