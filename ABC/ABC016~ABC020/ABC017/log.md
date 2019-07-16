# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 考察
### A プロコン
- One liner is better and start.

```python
print(sum([eval(input().replace(' ', '*')) for _ in range(3)])//10)
```

### B choku語
- 集合を用いた解法
```python
print('NO' if set(input().replace('ch','')) - set('oku') else'YES')
```
- 正規表現を用いた解法１
```python
import re
print('NO' if re.sub('ch|o|k|u', '', input()) else 'YES')
```

- 正規表現を用いた解法２
```python
import re
print('YES' if re.fullmatch('(ch|[oku])*', input()) else 'NO')
```

### C ハイスコア
- `いもす法` を用いる
- 全体の合計得点から覆っている区間の合計得点を引く
- いもす法で求まるのはその区間で得られる得点

```
例１
index|   0   1   2   3   4   5   6   7|
   30|      30         -30            |
   40|          40     -40            |
   25|              25             -25|
   10|                          10 -10|
  sum|      30  70  95  25   0  35   0| 

例２
index|   0   1   2   3   4   5   6   7   8|
   30|      90         -90                |
   40|                      90         -90|
  sum|      90  90  90  0   90  90  90   0| 

例３
index|   0   1   2   3   4   5|
   30|      70             -70|
  sum|      70  70  70  70   0| 
```

#### 注意
- 以下の書き方 (-2の部分) はよろしくない。

```python
print(total_cost - min(cost[1:-2]))
```

#### 参考資料
- [eval()](https://docs.python.jp/3/library/functions.html#eval)
- [re.sub を使用して正規表現で文字列を置換する](https://uxmilk.jp/8662)
- [re.fullmatch](https://docs.python.jp/3/library/re.html#re.fullmatch)
- [Pythonの正規表現の基本的な使い方](https://uxmilk.jp/41416)
- [いもす法公式](https://imoz.jp/algorithms/imos_method.html)