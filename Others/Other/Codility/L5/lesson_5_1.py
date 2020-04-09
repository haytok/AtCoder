def solution(A, B, K):
    div = A // K
    mod = A % K
    first = A if mod == 0 else A + K - mod
    return 0 if first > B else 1 + (B - first) // K

if __name__ == '__main__':
    # A, B, K = 6, 11, 2
    A, B, K = 11, 23, 7
    print(solution(A, B, K))