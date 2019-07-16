N = int(input())
S = [input() for i in range(N)]
nameDict = {"M": 0, "A": 0, "R": 0, "C": 0, "H": 0}
List = []
result = 0

# 入力された文字に対する辞書の生成
for i in range(0, N):
    if S[i][0] in nameDict.keys():
        nameDict[S[i][0]] += 1

for i in nameDict.values():
    List.append(i)

for i in range(0, 3):
    for j in range(i+1, 4):
        for k in range(j+1, 5):
            result += List[i]*List[j]*List[k]
print(result)