# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 考察
### B Palace
- 別解
```python
N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
X = [abs(A - (T - h * 0.006)) for h in H]
print(X.index(min(X)) + 1)
```
