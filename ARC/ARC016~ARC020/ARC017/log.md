# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 要約
### A 素数、コンテスト、素数
```text
入力された整数が素数かどうか判定する問題
```

### B 解像度が低い。
```text
単調に増加するある一定以上の長さの数列の個数を求める問題。
```

# 考察
### A 素数、コンテスト、素数
- 一応素数のライブラリを持ってたから、簡単やった。

- 素数判定の関数
```python
def is_prime(n):
    if n < 2 or n & 1 == 0:return False
    for i in range(3, int(n ** (1/2)) + 1):
        if n % i == 0:
            return False
    return True
```

### B 解像度が低い。
- 考えたアルゴリズムは完璧やったのに1つだけWA出て解決出来へんかったのは悔しかった。(-> 解決できた)

- 別解
```python
N, K = map(int, input().split())

base = 0
length = 0
ans = 0

for i in range(N):
    item = int(input())
    if item > base:
        base = item
        length += 1
        if length >= K:
            ans += 1
    else:
        base = item
        length = 1
        if length >= K:
            ans += 1

print(ans)
```