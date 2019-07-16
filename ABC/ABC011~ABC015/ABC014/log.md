# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 考察
### B 価格の合計  `bit演算`
- 別解

```python
n, X = map(int, input().split())
a = list(map(int, input().split()))

print(sum([a[i] for i in range(n) if X & (1 << i)]))
```

- `1 << i` は 1 を i bit 左シフトさせる。すなはち i 桁番目の X の値を抽出できる。

- この解答はComputerScienceっぽい解答〜〜

### C AtColor `いもす法とaccumulate関数を用いた累積和`
- `いもす法 `を使うのは瞬殺でわかる。あとはいかにして解くか。

- 例１の処理の具体例

```text
 0  1  2  3  4  5  6  7  8  9  10
 1       -1
       1    -1
       1       -1
                1     -1
 1  1  3  2  1  1  1   0  0  0  0
```

- データ構造を作りきった後に、累積和を計算するときに役に立つPythonのライブラリに `from itertools import accumulate` と言う関数を用いると計算が速くできる。

- 参考資料
  - [accumulate](https://docs.python.jp/3/library/itertools.html#itertools.accumulate)