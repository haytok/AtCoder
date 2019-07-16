# あんまり得意でない辞書の問題
n = int(input())
s=[]
ans = ""
# sは文字列が複数入ってる
for i in range(n):
    s.append(input())

# 最初の入力をsetかけて、昇順のリストに変換
ls = sorted(list(set(s[0])))

for l in ls:
    # リスト内包表記を使って最小値を求めてるのが上手い
    cnt = min([s[i].count(l) for i in range(n)])
    # 文字列の結合はできる(文字列操作はimmutableのイメージが強く、あまり実感なかった。)
    ans += l*cnt

print(ans)
