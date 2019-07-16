N = int(input())
S = input()
a = []

# 閾値nで数号を分割
def cal(n):
    result = 0
    former = set()
    latter = set()
    for i in range(N):
        if i <= n:
            former.add(S[i])
        else:
            latter.add(S[i])
    union = former & latter
    if result < len(union):
        result = len(union)
    return result

for i in range(N):
    a.append(cal(i))
print(max(a))