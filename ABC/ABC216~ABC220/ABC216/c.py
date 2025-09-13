def main():
    N = int(input())
    ans = ''

    while N:
        if N % 2 == 1:
            ans += 'A'
            N -= 1
        else:
            ans += 'B'
            N //= 2

    print(ans)

if __name__ == '__main__':
    main()
