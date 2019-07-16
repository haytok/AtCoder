# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 考察
### B トリボナッチ数列
- 別解

```python
mod = 10007

def solve():
    n = int(input())
    a, b, c = 0, 0, 1

    if n == 1 or n == 2:
        print(0)
        return

    for i in range(n - 3):
        a, b, c = b, c, (a + b + c) % mod

    print(c)

if __name__ == '__main__':
    solve()
```