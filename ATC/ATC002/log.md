# 問題
* [ ] A
* [ ] B
* [ ] C

# 考察
### B n^p mod m
- `繰り返し二乗法`が使える場面
   - 組み合わせ・場合の数を求めるとき
   - 逆元を計算するとき
   - 行列を計算するケースでも使える

- 解法１ `繰り返し二乗法`

```python
N, mod, P = map(int, input().split())

print(pow(N % mod, P, mod))
```

- 解法２ `bit演算`を用いた解法

```python
```
