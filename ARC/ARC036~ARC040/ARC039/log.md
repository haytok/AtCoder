# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 要約
### A A - B problem
```text
A - Bの値が最大となるようにAかBの値をどちらか一方を書き換える。
この時のA - Bを計算する。
```

### B 
```text
N人の児童にK個の飴を分配する。
児童に分配された飴の個数の積が最大となるような分配方法を計算する。
```

# 考察
### A A - B problem
- めっちゃ考えた結果、適宜場合分けするよりも全探索をした ...

- 別解
```python
A, B = input().split()

a = max(int('9' + A[1] + A[2]), int(A[0] + '9' + A[2]), int(A[0] + A[1] + '9'))
b = min(int('1' + B[1] + B[2]), int(B[0] + '0' + B[2]), int(B[0] + B[1] + '0'))

print(max(a - int(B), int(A) - b))
```

### B 高橋幼稚園
- 大学受験の問題みたな問題やった。簡単やった。


# 参考
- 組み合わせと重複組み合わせのライブラリ

```python
# nCr
def combination(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

# nHr (重複組み合わせ)
def combinations_with_replacement(n, r):
    return combination(n + r - 1, r)
```
