def main():
    A, B = map(lambda str: int(str), input().split(' '))

    print(1 if A == B else 32 ** (A - B))

if __name__ == '__main__':
    main()
