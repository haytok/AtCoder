from collections import Counter
 
n, k = map(int, input().split())
a = Counter((i for i in input().split()))
sort_count = sorted(a.values())
total = 0
l = len(sort_count)
 
if len(sort_count) <= k:
    print(0)
else:
    print(sum(sort_count[:l-k]))