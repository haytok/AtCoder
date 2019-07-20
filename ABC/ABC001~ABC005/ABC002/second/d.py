'''
最大クリーク問題
'''
"""
問題を読み間違えていた...
N人の中から何人かを選んで派閥を作る。何人かを選ぶ !!!
"""
from itertools import combinations

if __name__ == '__main__':
    N, M = map(int, input().split())
    inputs = [set(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(1, 2 ** N):
        bit = format(i, 'b').zfill(N)
        parties = []
        for index in range(len(bit)):
            if bit[index] == '1':
                parties.append(index + 1)
        for party in combinations(parties, 2):
            set_party = set(party)
            if set_party not in inputs:
                break
        else:
            ans = max(ans, len(parties))
    print(1 if ans == 0 else ans)
