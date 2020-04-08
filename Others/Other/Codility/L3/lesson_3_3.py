def solution(A):
    total = sum(A)
    other = 0
    ans = 10e9
    for index in range(len(A) - 1):
        other += A[index]
        ans = min(ans, abs(total - other * 2))
        print(abs(total - other * 2))
    print('-'*10)
    return ans

if __name__ == '__main__':
    A = [3, 1, 2, 4, 3]
    print(solution(A))