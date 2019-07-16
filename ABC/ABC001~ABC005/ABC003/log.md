# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 考察
### B AtCoderトランプ
- 別解

```python
S = input()
T = input()

wirdcard = ['a', 't', 'c', 'o', 'd', 'e', 'r']

for a, b in zip(S, T):
    if a == b:
        continue
    if (a == '@' and b in wirdcard) or (b == '@' and a in wirdcard):
        continue
    print('You will lose')
    break
else:
    print('You can win')
```

### C AtCoderプログラミング講座
- 適当に手元で試して規則性を探す。