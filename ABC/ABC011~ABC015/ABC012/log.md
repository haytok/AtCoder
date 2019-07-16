# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 考察
### A スワップ
- 別解
```python
print(*input().split()[::-1])
```

### B 入浴時間
- 別解

- `:書式指定文字列` を指定するといい感じにformatされて出力される。
```python
print('{year}年{month:02}月{day:02}日'.format(year=2018, month=1, day=11)
# 2018年01月11日
```

```python
N = int(input())
print("{:02d}:{:02d}:{:02d}".format(N//60//60,N//60%60,N%60))
```

# 参考資料
- (Python 書式指定文字列)[https://gammasoft.jp/blog/python-string-format/]