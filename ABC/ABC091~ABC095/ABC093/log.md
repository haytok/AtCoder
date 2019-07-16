# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 考察
### A abc of ABC

- 別解

```python
S = list(input())
if 'a' in S and 'b' in S and 'c' in S:
    print("Yes")
else:
    print("No")
```

- 別解

```python
s = ''.join(sorted(list(input())))

print('Yes' if s=='abc' else 'No')
```