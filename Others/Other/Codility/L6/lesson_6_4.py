from itertools import permutations

def is_triangular(array):
    total = sum(array)
    for angular in array:
        value = total - angular * 2
        if value > 0:
            continue
        else:
            return False
    return True

def solution(A):
    indexes = [i for i in range(len(A))]
    for item in permutations(indexes, 3):
        array = [A[item[0]], A[item[1]], A[item[2]]]
        flag = is_triangular(array)
        if flag:
            return 1
    else:
        return 0


if __name__ == "__main__":
    array = [10, 2, 5, 1, 8, 20]
    # check = [8, 10, 20]
    check = [8, 10, 5]
    print(is_triangular(check))
    print(solution(array))
