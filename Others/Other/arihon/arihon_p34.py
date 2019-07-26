"""
入力
n: 整数の個数
a: 整数列
k: 和

入力１
4
1 2 4 7
13

出力１
Yes

入力２
4
1 2 4 7
15

出力２
No
"""

N = int(input())
inputs = [int(i) for i in input().split()]
K = int(input())

def dfs(total, index):
    if total == K:
        return True
    if index == N:
        return False
    
    return dfs(total, index+1) or dfs(total+inputs[index], index+1)


def dfs_sample(total, index):
    if index == N:
        return total == K
    
    if dfs(total, index+1):
        return True
    
    if dfs(total+inputs[index], index+1):
        return True
    
    return False

print('Yes' if dfs(0, 0) else 'No')
