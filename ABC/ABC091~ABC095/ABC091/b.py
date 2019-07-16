def makeDictionary(in_item, out_item):
    for item in in_item:
        if item in out_item.keys():
            out_item[item] += 1
        else:
            out_item[item] = 1

sResult = {}
tResult = {}

N = int(input())
s = makeDictionary([input() for i in range(N)], sResult)
M = int(input())
t = makeDictionary([input() for i in range(M)], tResult)

for item in tResult.keys():
    if item in sResult:
        sResult[item] -= tResult[item]

result = max(sResult.values())

if result < 0:
    print(0)
else:
    print(result)