def main():
    print(
        ''.join(
            [
                chr(ord('a') + int(n) - 1) for n in input().split(' ')
            ]
        )
    )

if __name__ == '__main__':
    main()
