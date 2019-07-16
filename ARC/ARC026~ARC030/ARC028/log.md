# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 要約
### A 小石を取るゲーム
```text
最初、袋にN個の小石が入っている。その袋から二人が交互に決められた石を取っていく。
この操作を順に繰り返していって、自分のターンで袋を空にしたら勝ち。
```

### B 特別賞
```text
コンテストに参加した人の入賞者の年齢が与えられる。
この時、順位がi位以内の人のうちK番目に若い人の順位を求める。
```

# 考察
### A 小石を取るゲーム
- 書いてる通りに実装するのみ。簡単やった。

- 別解１
```python
N, A, B = [int(i) for i in input().split()]

print('Ant' if 0 < N % (A + B) <= A else 'Bug')
```

### B 特別賞
- この問題を解くのに必要なのは要素を追加して、最小値を取り出すこと。

# 参考
- `heapq` (優先度キューアルゴリズム, priority queue)の使い方

- 使い方まとめ
```python
import heapq

heapq.heappush(heap, item) # itemをheapにpushする。

heapq.heappop(heap) # heapから最小の要素を返す。空のときはIndexErrorが返る。

heapq.heappushpop(heap, item) # itemをheapにpushした後にpopをしてheapから最初の値を返す。

heapq.heapify(x) # リストxをインプレス処理して、線形時間でヒープに変換する。
```

- 具体例
```python
import heapq

a = [6, 3, 2, 4, 5]

heapq.heapify(a) # 破壊的

print(a[0]) # 2

heapq.heappop(a) # aから最小値を取り出す

print(a[0]) # 3

heapq.heqppush(a, 1) # ヒープaに値を入れる

print(a[0])
```

- [doc heapq](https://docs.python.org/ja/3/library/heapq.html)
