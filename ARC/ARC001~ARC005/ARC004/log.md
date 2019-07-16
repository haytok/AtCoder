# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 要約
### A 2点間距離の最大値 ( The longest distance )
```text
二点間の距離の最大値を求める。
```

### B 2点間距離の最大と最小 ( Maximum and Minimum )
```text
隣り合うノードの距離が与えられる。
そこで、最初と最後のノードの距離の最小値と最大値を求める。
```

# 考察
### A 2点間距離の最大値 ( The longest distance )
- 簡単やったけど、もっと良い解き方があるとは思ってはいた。
- 複素数を使って二次元の行列(ベクトル)の計算を手軽にやってたのは天才かもしれん。

- 別解
```python
N = int(input())
inputs = [complex(*map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, abs(inputs[i] - inputs[j]))

print(ans)
```

### B 2点間距離の最大と最小 ( Maximum and Minimum )
- あんまり腑に落ちひんけど、ギリギリ納得は出来た。イメージしづらかった。。。

```text
最大のエッジ間の距離とそれ以外のエッジ間の差を比較する。
それ以外のエッジ間距離の方が大きいときは求める値の最小値は0。
そうでないときは最大のエッジ間の距離とそれ以外のエッジ間の差が答え。
```

# 参考
- `map()` は`イテレーター`を返すので、アンパックするには `*` を使う。
- 長さを求める方法の１つに `abs(complex(1, 2))` がある。

- [complex() の使い方の一例](https://python.atelierkobato.com/complex/)

- [map](https://docs.python.jp/3/library/functions.html#map)

- [イテレーターとイテラブル](https://hibiki-press.tech/learn_prog/python/iterable_iterator/1567#i-3)
