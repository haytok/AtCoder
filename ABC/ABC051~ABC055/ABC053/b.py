s = input()

start = s.index("A")

for i in range(len(s)-1, start, -1):
    if s[i] == "Z":
        print(i - start + 1)
        break

# str.rfind() っていうmethodがある。
# 文字列中の領域 s[start:end] に sub が含まれる場合、その最大のインデックスを返します。
# オプション引数 start および end はスライス表記と同様に解釈されます。 sub が見つからなかった場合 -1 を返します。