# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 要約
### A GPA計算
```text
与えられた文字列から ABCDF の数を数えて、それに対応する価値を掛けて計算する。
```

### B さかさま辞書
```text
与えられた文字列を逆さにしたやつの辞書を求める。
```

# 考察
### A GPA計算
- 簡単やったけど、できるだけ短いコードを考えるのが楽しかった。

- 別解１ (一般的なやり方)
```python
N = int(input())
inputs = input()

score ={'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
scores = [score[i] * inputs.count(i) for i in 'ABCDF']

print(sum(scores) / N)
```

- 別解２ (配列のインデックスを使うやり方)
```python
print(1 / int(input()) * sum('FDCBA'.index(i) for i in input()))
```

### B さかさま辞書
- 簡単やった。

# 参考

```python
ord('A') -> 65
```
