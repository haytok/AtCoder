def main():
    N = input()
    int_N = int(N)

    length = 0
    while int_N:
        int_N //= 10
        length += 1
    
    print('0' * (4 - length) + N if N != '0' else '0000')

if __name__ == '__main__':
    main()
