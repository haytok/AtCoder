import itertools

def main():
    N = list(input())

    length = len(N)
    ans = 0

    for item in itertools.permutations(N):
        for i in range(length):
            former, latter = item[:i], item[i:]
            if len(former) == 0 or len(latter) == 0:
                continue
            ans = max(ans, int(''.join(former)) * int(''.join(latter)))

    print(ans)

if __name__ == '__main__':
    main()
