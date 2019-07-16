N = int(input())

'''
再帰関数を実装する際に必要なこと
1. 引数を決める
2. 返り値を決める
3. 処理内容を決める (ベースケースをメイン処理の実装)
'''
def compute(N):
    if N == 0:
        return 0
    return N + compute(N - 1)

print(compute(N))