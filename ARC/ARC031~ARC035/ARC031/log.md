# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 要約
### A 名前
```text
与えられた入力が回文かどうかを判定する問題。
```

### B 埋め立て
```text
10*10のマスが与えられる。そこには陸か海かが表現されている。
ある一箇所を埋め立てた時に陸全体が地続きになるかを判定する。
```

# 考察
### A 名前
- 簡単やった。実装するのみ。

### B 埋め立て
- 実装方法が全くわからんかった。
- 海の箇所を順に一箇所ずつ全て陸に変えていって、陸の箇所を海に変えるように再帰的に変更をかける。その結果全て海になるかで判定する。
- 計算量的に無理なんかと思ったけど行けるのか ...