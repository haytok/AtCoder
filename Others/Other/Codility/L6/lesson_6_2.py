def solution(A):
    array = []
    for i in range(5):
        if len(A) == 0:
            break
        if i <= 1:
            value = min(A)
        else:
            value = max(A)
        A.remove(value)
        array.append(value)
    return max(array[0] * array[1] * array[2], array[-3] * array[-2] * array[-1])

if __name__ == '__main__':
    array = [-3, 1, 2, -2, 5, 6]
    # array = [1, 2, 3]
    print(solution(array))