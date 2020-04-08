# 計算量にも気を付けなあかん

def solution(A):
    length = len(A)
    ans = (length + 1) * (length + 2) // 2 - sum(A)
    return ans

if __name__ == '__main__':
    A = []
    print(solution(A))