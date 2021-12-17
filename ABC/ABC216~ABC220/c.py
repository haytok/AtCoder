def get_index(array, q):
    threshold = 0
    for index, value in enumerate(array):
        threshold += value
        if threshold > q:
            return index + 1
    raise 'Invalid inputs.'


def main():
    N = int(input())
    inputs = input().split()
    X = int(input())

    int_inputs = list(map(int, inputs))
    one_lot = sum(int_inputs)
    ans = 0

    if one_lot < X:
        q, mod = divmod(X, one_lot)
        ans += (N * q)
        ans += get_index(int_inputs, mod)
    else:
        ans = get_index(int_inputs, X)

    return ans


if __name__ == '__main__':
    print(main())
