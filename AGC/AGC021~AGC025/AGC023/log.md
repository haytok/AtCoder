# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D
* [ ] E
* [ ] F

# 考察
### A Zero-Sum Ranges
- 下の愚直な解法はそら通らんわなって感じ。
- `累積和` 使えば、連続する部分の和すなわち`区間の和`を全て求められるのかしこい。

```python
N = int(input())
inputs = [int(i) for i in input().split()]

ans = 0

for i in range(N):
    total = 0
    for item in inputs[i:]:
        total += item
        if total == 0:
            ans += 1

print(ans)
```