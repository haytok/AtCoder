# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 要約
### A BMI
```text
身長とBMI指数の関係から体重を計算する。
```

### B 格子点と整数
```text
標準入力から３組の組み合わせの中でその三点を結ぶ三角形の面積が０でなくかつ整数の値を取る頂点の個数を計算する。
```

# 考察
### A BMI
- 簡単やった。実装するのみ。

### B 格子点と整数
- Pythonのライブラリで組み合わせを計算してくれる `itertools.combinations` を使ってペアを求める。
- そして、座標系で三角形の面積を求める公式を用いて計算するのみ。

# 参考
- [itertools.combinations](https://note.nkmk.me/python-math-factorial-permutations-combinations/)
