# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D
* [ ] E
* [ ] F

# 要約
### A Beginning
```text
入力文字列に指定された文字列が入っているかを判定する問題。
```

### B KEYENCE String
```text
ある連続した部分文字列を除いてkeyenceの文字列が現れるかを判定する問題。
```

### C Exam and Wizard
```text
高橋くんがした準備の量は一定で余裕がある箇所は余裕のない箇所に分配する。
最小の分配の回数を求める。
```

# 考察
### A Beginning
- 簡単やったんやけど、焦ってandとorを間違えてしまった。

### B KEYENCE String
- 今回のコンテストで一番詰まってしまった。7WAした上に80分もかかってしまった。
- 文字列の操作が特に課題です。

- 別解 (この解法は特にキレイ)

```python
S = input()
for i in range(7):
    if S[:i] + S[i - 7:] == "keyence":
        print("YES")
        break
else:
    print("NO")
```

### C Exam and Wizard
- レートを上げるのを諦めてたから、焦らず解けて簡単やった。
