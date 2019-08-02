import sys
sys.setrecursionlimit(10**9)

N, A, B, C, D = map(int, input().split())
inputs = list(input())

def compute(index, end):
    if inputs[index] == '#' or index > end:
        return False
    if index == end:
        return True
    return compute(index+1, end) or compute(index+2, end)

flag = False
if A < C and C < B:
    flag = compute(A-1, C-1) and compute(B-1, D-1)
elif B < C < D:
    flag = compute(A-1, C-1) and compute(B-1, D-1)
elif D < C:
    for index in range(B-2, D-1):
        if (index != A - 1) and inputs[index] != '#' and inputs[index+1] != '#' and inputs[index+2] != '#':
            flag = True
    flag = flag and compute(A-1, C-1) and compute(B-1, D-1)

print('Yes' if flag else 'No')
