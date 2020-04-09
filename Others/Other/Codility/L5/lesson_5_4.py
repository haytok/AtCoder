# DeepLと問題が違う場合があるので、制約などセンシティブな情報は必ず英語の問題文を読む
def solution(A):
    ans = 0
    counts = 0
    for item in A[::-1]:
        if item == 1:
            counts += 1
        else:
            ans += counts
    return -1 if ans > 1e9 else ans

if __name__ == '__main__':
    # A = [0, 1, 0, 1, 1]
    # A = [0, 0, 0, 0, 0]
    A = [1, 1, 1, 1, 1]
    print(solution(A))