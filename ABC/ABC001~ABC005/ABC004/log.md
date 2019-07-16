# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 考察
### B 回転 (180度回転)
- 別解
```python
inputs = [input().split() for _ in range(4)]

for rcs in inputs[::-1]:
    print(*rcs[::-1])
```