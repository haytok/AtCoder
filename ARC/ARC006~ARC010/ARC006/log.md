# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 要約
### A 宝くじ
```text
問題の名前通り宝くじが当たっている個数を数える。
オプションとしてボーナスチャレンジがあることが少し変わった点。
```

### B あみだくじ
```text
問題の名前通りあみだくじで当たりとなる人を探す。
```

# 考察
### A 宝くじ
- 下の解答は上手い。当たっているかをfor文で処理するのではなく集合を用いて考えている。

- 別解
```python
a = set([int(i) for i in input().split()])
b = int(input())
c = set([int(i) for i in input().split()])

k = len(a & c)
if k == 5 and b in c:
    print(2)
else:
    print({6: 1, 5: 3, 4: 4, 3: 5}.get(k, 0))
```

### B あみだくじ
- 簡単やった。
