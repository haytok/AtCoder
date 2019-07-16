# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 要約
### A B +/- A
```text
AがBの約数なら和をそうでない時はB-Aを出力する。
```

### B Foods Loved by Everyone
```text
各人の好みの食べ物が与えられる。
このとき、全員の好みの食べ物の種類を計算する。
```

### C Monsters Battle Royale
```text
モンスターがN体存在する。
生きているモンスターがランダムに他のモンスターに攻撃し、生きているモンスターの体力の分だけダメージを与える。
このとき、最後生き残ったモンスターの最終的な体力の最小値を計算する。
```

### D Match Matching
```text
```

# 考察
### A B +/- A
- 簡単やった。問題分通り実装するのみ。

### B Foods Loved by Everyone
- 問題分を読み間違えて結構な時間を溶かしてしまった。自分の読解力に反省。
- その点以外は単純にsetして集合を求めていくのみ。

### C Monsters Battle Royale
- 問題分と3つのサンプルから最大公約数を計算すれば解けるって感覚的にわかった。

- 別解
```python
from fractions import gcd
from functools import reduce

_ = input()
*a, = map(int,input().split())

print(reduce(gcd,a))
```

### D Match Matching
- 解けへんかった ...
