from collections import Counter

w = Counter(list(input()))

for value in w.values():
    if value % 2 != 0:
        print('No')
        break
else:
    print('Yes')

w = input()
for s in set(w):
    if w.count(s) % 2 != 0:
        print('No')
        break
else:
    print('Yes')