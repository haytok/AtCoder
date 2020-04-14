def solution(A):
    return len(list(set(A)))

if __name__ == '__main__':
    array = [1, 1, 2, 2, 3, 3]
    print(solution(array))