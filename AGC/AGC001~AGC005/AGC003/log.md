# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D
* [ ] E
* [ ] F

# 要約
### A Wanna go back home
```text
東西南北に移動する回数が与えられる。
移動する距離は任意の距離である。
その際にスタートした位置に帰って来れるか。
```

# 考察
### A Wanna go back home
- 簡単やった。下の解答の方がいい感じやった。

```python
t = input()

if ('N' in t) == ('S' in t) and ('E' in t) == ('W' in t):
    print('Yes')
else:
    print('No')
```
