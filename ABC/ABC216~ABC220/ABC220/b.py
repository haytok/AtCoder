def get_value(input_value, K):
    base_value = 1
    value = 0

    for i in range(len(input_value) - 1, -1, -1):
        value += base_value * int(input_value[i])
        base_value *= K

    return value

def main():
    K = int(input())
    A, B = input().split(' ')

    print(get_value(A, K) * get_value(B, K))

if __name__ == '__main__':
    main()
