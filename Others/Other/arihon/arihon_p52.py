import sys
sys.setrecursionlimit(10**9)

N = 4
inputs = [[2, 3], [1, 2], [3, 4], [2, 2]]
W = 5

ans = 0
def dfs(index, weight, value):
    print('index', index, 'weight', weight, 'value', value)
    global ans
    if index == N:
        return value
    
    w = inputs[index][0]
    v = inputs[index][1]
    if weight + w <= W:
        ans = max(ans, dfs(index+1, weight+w, value+v))
    else:
        ans = max(ans, dfs(index+1, weight, value))
    return ans

dfs(0, 0, 0)
print(ans)