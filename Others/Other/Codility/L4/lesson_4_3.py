def solution(A):
    set_A = set(A)
    sorted_set_A = sorted(set_A)
    value = 0
    for item in sorted_set_A:
        if item <= 0:
            continue
        if item == value + 1:
            value += 1
        else:
            return value + 1
    else:
        return 1 if value == 0 else value + 1


if __name__ == '__main__':
    pass