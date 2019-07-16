# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 要約
### A 元気にお使い！高橋君
```text
商品の個数と値段が複数与えられるので消費税込みでその総和を計算する。
```

### B おとぎの国の高橋君
```text
10進数の大小関係ではない独自の大小関係のもとで、与えられた数字をソートする。
```

# 考察
### A 元気にお使い！高橋君
- 処理的には簡単なのに、短いコードで実装出来なかったのが悔しかった。

- 別解１
```python
print(sum([eval(input().replace(' ','*'))for _ in range(int(input()))]) * 105 // 100)
```

- 処理が走る順に標準入力が行われる。

### B おとぎの国の高橋君
- 結構てこづった。悔しい。
- 写像先の空間は10進数なので、そこでソートを掛けて元の空間に戻る感じ。


# 参考
- `split() returns a list of the words in the string, using sep as the delimiter string. ` 
- [str.split()](https://docs.python.jp/3/library/stdtypes.html?highlight=split#str.rsplit)

- 複数の文字を変換処理に便利な `str.translate()`
- [文字の変換にはstr.translate()が便利](https://qiita.com/tag1216/items/df6c93bdb823dd48af6c)
