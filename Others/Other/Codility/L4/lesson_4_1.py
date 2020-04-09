def solution(X, A):
    leaf = set()
    for index, position in enumerate(A):
        leaf.add(position)
        if len(leaf) == X:
            return index
    else:
        return -1

if __name__ == '__main__':
    # X, A = 5, [1, 3, 1, 4, 2, 3, 5, 4]
    # X, A = 1, [1, 1, 1, 1]
    X, A = 5, [1, 1, 1, 1, 1]
    print(solution(X, A))