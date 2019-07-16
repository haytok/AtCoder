# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 要約
### A Still TBD
```text
yyyy/mm/ddのフォーマットで与えられた入力と2019年4月30日を比較してHeiseiかTBDを判断する。
```

### B Digital Gifts
```text
お金とそのお金がどの通貨であるかの情報が与えられるので、日本円としての価値の総和を計算する。
```

### C Synthetic Kadomatsu
```text
あるN本の竹が与えられる。
このN本の竹を用いて、結合(コスト１０)、縮小(コスト１)、延長(コスト１)して、
長さが与えられたA, B, Cの竹の長さになるようにする。
このときコストの最小値を求める。
```

# 考察
### A Still TBD
- datetimeモジュールに苦戦した結果、めっちゃ時間食ってしまった ... 
- わざわざdatetimeモジュールを使わずとも単純に文字列の比較でも解けてしまうってことに頭が回らんかった ...

- 解法１
```python
import datetime

a  = (datetime.datetime.strptime('2019/04/30', '%Y/%m/%d') 
- datetime.datetime.strptime(input(), '%Y/%m/%d')).days

print('Heisei' if a >= 0 else 'TBD')
```

- 解法２
```python
print('Heisei' if input() <= '2019/04/30' else 'TBD')
```

### B Digital Gifts
- この回で一番簡単やった。問題文通りに実装するのみ。

### C Synthetic Kadomatsu
- DFSと再帰の問題やった。そろそろ解けるようになりたい。
