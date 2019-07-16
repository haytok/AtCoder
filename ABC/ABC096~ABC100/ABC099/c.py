n = int(input())
numbers = sorted([9**5, 9**4, 9**3, 9**2, 9, 6**6, 6**5, 6**4, 6**3, 6**2, 6], reverse=True)
dic = dict()

def dp(i, N):
    if i == len(numbers):
        return N
    if (i, N) not in dic:
        dic[(i, N)] = min(dp(i, N-numbers[i])+1, dp(i+1, N)) if N-numbers[i] >= 0 else dp(i+1, N)
    return dic[(i, N)]

print(dp(0, n))
