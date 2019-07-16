# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 考察
## A 豆まき
- 意外に手こずってしまった。悲しい。

## B 文字列の反転
- 意外に少し手こずってしまった。悲しみ。

## C 菱型カウント
- 丸が白、バツが黒、*が緑
- inputがR, C, K
- 以下の条件を満たすように新たに緑色を塗る。
- K <= x <= R - K + 1
- K <= y <= K - K + 1
- 白ますを選択して、その点をベース。

- 黒ますをベースとした余事象を考える。

### 解答
```python
from collections import deque

R, C, K = map(int, input().split())
inputs =[list(input()) for _ in range(R)]

que = deque()
result = 0

# 黒の点(x)の座標を保存する
for r in range(R):
    for c in range(C):
        if inputs[r][c] == 'x':
            que.append((r, c))

for k in range(K-1):
    tmp_que = deque()
    while que:
        # 黒の点(x)の座標
        r, c = que.pop()
        # 黒の点から上下左右の点を探索する
        for i, j in [(r+1, c), (r-1, c), (r, c-1), (r, c+1)]:
            if 0 <= i < R and 0 <= j < C and inputs[i][j] == 'o':
                inputs[i][j] = 'x'
                tmp_que.append((i, j))
    que = tmp_que

for x in range(K-1, R-K+1):
    for y in range(K-1, C-K+1):
        if inputs[x][y] == 'o':
            result += 1

print(result)
```

- Pyhtonの標準ライブラリの `deque` 
  - deque とは `double-ended queue` の略で、Dequeはどちらの側からもappend, popが可能で、スレッドセーブでメモリが効率がよく、どちらの側からも `O(1)` でアクセスできる。ちなみに、listのオーダーは `O(n)` となる。
  - [公式ドキュメント](https://docs.python.jp/3/library/collections.html#collections.deque)
  - [忘れがちだが、便利なPythonのデータ型 5つ](https://qiita.com/keitakurita/items/7f02f600be8a2c9ad227#deque)

- `list()` と `[]`の違い
  - list(文字列)すると、1文字のリストが生成される。