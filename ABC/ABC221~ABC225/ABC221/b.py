def main():
    S = list(input())
    T = list(input())

    can_changed = True
    length = len(S)
    for i in range(length - 1):
        if S[i] != T[i]:
            if can_changed and S[i+1] == T[i]:
                S[i], S[i+1] = S[i+1], S[i]
                can_changed = False
            else:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()
