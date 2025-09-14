def main():
    N, P = map(lambda s: int(s), input().split(' '))
    scores = list(map(lambda s: int(s), input().split(' ')))

    print(len(list(filter(lambda n: n < P, scores))))

if __name__ == '__main__':
    main()
