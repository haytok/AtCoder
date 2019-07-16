# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D
* [ ] E
* [ ] F

# 要約
### A A +...+ B Problem
```text
要素数がN個で最小値がA、最大値がBである集合を考える。
その集合の要素を使って表現できる和の個数を数える。
```

# 考察
### A A +...+ B Problem
- 問題見た時に解法はすぐにわかったけど、A==Bのときの解釈で時間を溶かしてしまった。
- A==Bのとき和の個数がN個でないことにイマイチ納得がいかなかった。解答的には1やねんけど。。。

- 最初の自分の解答
```python
N, A, B = map(int, input().split())

ans = 0

if A > B:
    pass
elif A == B:
    ans = N
else:
    if N == 1:
        pass
    else:
        ans = B * (N - 1) + A - (A * (N - 1) + B) + 1

print(ans)
```

- 変更後の自分の解答
```python
N, A, B = map(int, input().split())

if A > B:
    ans = 0
elif N == 1:
    if A == B:
        ans = 1
    else:
        ans = 0
else:
    ans = (B - A) * (N - 2) + 1

print(ans)
```
