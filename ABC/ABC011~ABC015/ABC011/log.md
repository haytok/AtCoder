# 問題
* [ ] A
* [ ] B
* [ ] C 貪欲法
* [ ] C 動的計画法
* [ ] D

# 考察
### C 123引き算
- `貪欲法`

```python
n = int(input())
ng = [int(input()) for i in range(3)]

if n in ng:
  print('NO')
  exit()
  
for i in range(100):
    for j in [n-3, n-2, n-1]:
        if j not in ng:
            n = j
            break
    else:
        print('NO')
        exit()
      
if n<=0:
    print('YES')
else:
    print('NO')
```

- `動的計画法`

```python
n = int(input())
ng = [int(input() for _ in range(3)]

dp = [1000 for i in range(n+1)]

dp[n] = 0

# for文を逆から回している
# 最低でも-1で引き続ければ試行が終了する
for i in range(n+1)[::-1]:
    if i in ng:
        continue
    for j in range(1,4):
        if i-j >= 0 :
            dp[i-j] = min(dp[i] + 1, dp[i-j])
    
if n in ng:
    print('NO')
elif dp[0] <= 100:
    print('YES')
else:
    print('NO')
```
