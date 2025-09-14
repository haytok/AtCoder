def main():
    A, B, C = map(lambda str: int(str), input().split(' '))

    ans = -1
    for n in range(A, B+1):
        if n % C == 0:
            ans = n
            break

    print(ans)

if __name__ == '__main__':
    main()
