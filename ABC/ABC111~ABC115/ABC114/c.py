N = int(input())

elements = '753'

def dfs(S):
    if int(S) > N:
        return 0
    ans = 1 if all(S.count(element) for element in elements) else 0
    for element in elements:
        ans += dfs(S+element)
    return ans

print(dfs('0'))
