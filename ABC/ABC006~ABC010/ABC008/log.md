# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 考察
###  C コイン
- この問題はNが小さいときは全探索をすることができるが、大きくなるにつれて計算量も増えるので、より強力なアルゴリズムを設計する必要がある。

- そこで全く視点を変えてあるコインが表になる条件を考え、その和を計算する。

- 以下画像を参照

# 参考
### 階乗を計算する時に使うライブラリ

```python
from math import factorial

print(factorial(5))
```

```
120
```

### 順列を全列挙するライブラリ

- 入力
```python
from itertools import permutations

for item in permutations([2, 4, 6], 3):
    print(item)
```

- 出力
```
(2, 4, 6)
(2, 6, 4)
(4, 2, 6)
(4, 6, 2)
(6, 2, 4)
(6, 4, 2)
```
