def main():
    int_N = int(input())
    names_map = {}
    res = 'No'
    for _ in range(int_N):
        S, T = input().split(' ')
        if S in names_map:
            if T in names_map.get(S):
                res = 'Yes'
                break
            else:
                names_map[S].append(T)
        else:
            names_map[S] = [T]

    print(res)

if __name__ == '__main__':
    main()

# これ別に split() して map を作成する必要はなかった。
# input() 全体を set() に追加するだけで OK やった ...
