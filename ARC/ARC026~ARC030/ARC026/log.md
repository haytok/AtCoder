# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 要約
### A ダイナミックなポーズ
```text
５回だけ速く問題を解けるが、それ以外は普通の速さで解ける高橋くんがいる。
この時、高橋くんは問題を全部解ききるのにかかる時間をも求める。
```

### B 完全数
```text
与えられた整数が完全数かそれよりも大きいか小さいかを判定する。
```

# 考察
### A ダイナミックなポーズ
- 簡単やった。問題文通りに実装実装するのみ。

### B 完全数
- 簡単やった。計算量に注意して実装するのみ。
- 平方根を求めて完全数を計算するなら、計算量的にも全然大丈夫やった。
- 約数のライブラリ作成せねば。これまで何回か出てるけど、毎回一瞬考えるのダルい。

# 参考
- [Python でのワンライナーの `if ... elif ... else` に関して](https://note.nkmk.me/python-if-conditional-expressions/)

```python
# 三項演算子をネストするイメージ。
a = 2
print('negative' if a < 0 else 'positive' if a > 0 else 'zero') # positive
```
- 約数の計算

```python
import math

N = int(input())

square_root = int(math.sqrt(N))
end = square_root if square_root ** 2 == N else square_root + 1

for i in range(1, end):
    if N % i == 0:
        print(i, N // i)
```
