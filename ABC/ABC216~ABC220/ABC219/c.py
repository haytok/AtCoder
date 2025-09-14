def get_value(dicts, key):
    for k, v in dicts.items():
        if v == key:
            return k

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]

    dicts = {}
    for i in range(len(X)):
        dicts[X[i]] = chr(ord('a') + i)
    
    modified_S = []
    for s in S:
        modified_S.append(
            ''.join([dicts[string] for string in s])
        )
    modified_S.sort()

    for string in modified_S:
        print(''.join([get_value(dicts, s) for s in string]))

if __name__ == '__main__':
    main()
