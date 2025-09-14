def main():
    N = int(input())
    A = list(map(lambda s: int(s), input().split(' ')))
    X = int(input())

    sum_A = sum(A)
    lot = X // sum_A
    count = lot * len(A)
    total = lot * sum_A

    if total <= X:
        for a in A:
            total += a
            count += 1
            if total > X:
                print(count)
                return
    else:
        print(total)

if __name__ == '__main__':
    main()
