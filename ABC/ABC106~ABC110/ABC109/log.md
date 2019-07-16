# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 考察
### C Skip
- `ユークリッドの互除法` を用いる。
- これは図を書くとすぐにできる考察。

# 参考
### ユークリッドの互除法

```python
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
```