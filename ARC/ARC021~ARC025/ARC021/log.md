# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 要約
### A DEAD END
```text
あるマスの上下左右が同じ種類のマスならゲームは続く。
ただし、プレイ回数は一回だが、プレイを続けられるかを判定する。
```

### B Your Numbers are XORed...
```text
ある値とある値をXORした値が与えられるので、そうなるような辞書順で最小の元の値を計算する。
```

# 考察
### A DEAD END
- 上手な解法がスゴかった。
- indexを入れ替えるだけで縦方向と横方向を同時に処理するのは上手い。

### B Your Numbers are XORed...
- `XOR`の性質を学べる良問！
- その性質を知らんかったから解けへんかった。

- 配列の要素を開業して出力する方法
```python
print('\n'.join(map(str, ans))) # ansは配列で配列の要素を文字列にしないと結合出来ない
```


# 参考
- [ARC021 解説](https://www.slideshare.net/chokudai/arc021)
