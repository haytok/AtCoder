# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 考察
### B問題 高橋くんと文字列圧縮
- 今回は以下の２通りの解法で解いた。
  - `try-except`を用いてインデックスがオーバーフロー処理の手間を省いた解法
  - inputされた文字列をfor文で回して上手く処理する方法

### C問題 高橋くんと魔法の箱
- 一回目はTLEになってN<=3000のオーダーでしか処理が回りきらなかったが、refactorをかけると、めっちゃ速くなった。

- TLEになったときと解消されたときとの差分

```python
for i in input().split():
    result = cal(int(i))
    if result not in results:
        results.append(result)
```

```python
result = set(map(cal, input().split()))
```

- まぁ、そりゃそうか、一目瞭然って感じ。あればリストに入れる、ないとpassするという処理を配列でするくらいなら、setで最適化して解くのがベストでしょう。
