class UnionFind:

    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        # 入力された値とその値のインデックスの要素を比較
        if self.par[x] == x:
            return x
        else:
            # self.par[x] = self.find(self.par[x]) # ポインタ的な発想
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        print(x, y)
        # 同じ値の時、例えば(0, 0)の入力のとき特にする処理はない
        if x == y:
            print('par', self.par)
            return
        # rankに差がある時
        # rankの大き方に小さい方を結合する
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            print('par', self.par)
        else:
            self.par[y] = x
            print('par', self.par)
            # 同じrank同士の結合の時どちらかのランクを上げる
            # 同じrank同士の結合の時ではないときはpass
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


def solve(N, Q, queries):
    uf = UnionFind(N)
    for p, a, b in queries:
        if p == 0:
            uf.unite(a, b)
        elif p == 1:
            if uf.same(a, b):
                print("Yes")
            else:
                print("No")


def main():
    N, Q = map(int, input().split())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    solve(N, Q, queries)


if __name__ == '__main__':
    main()
