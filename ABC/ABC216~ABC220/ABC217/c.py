def main():
    N = int(input())
    ps = list(map(lambda str: int(str), input().split(' ')))
    
    res = [''] * N

    for i, p in enumerate(ps):
        res[p-1] = str(i+1)

    print(' '.join(res))

if __name__ == '__main__':
    main()
