def solution(A):
    set_A = set(A)
    ans_A = set([i for i in range(1, len(A) + 1)])
    return 1 if set_A == ans_A else 0

if __name__ == '__main__':
    pass