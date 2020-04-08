def solution(N):
    bin_input = bin(N)
    one_indexes = [index for index, value in enumerate(bin_input[2:]) if int(value) == 1]
    ans = 0
    for first, second in zip(one_indexes[1:], one_indexes[:-1]):
        ans = max(ans, first - second - 1)
    return 0 if ans == 0 else ans

if __name__ == '__main__':
    solution(8)