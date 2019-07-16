# わかりやすい
# from collections import Counter

# N = int(input())
# inputs = Counter([input() for _ in range(N)])

# print(sorted(inputs.items(), key=lambda x: x[1], reverse=True)[0][0])

# ワンライナー
from collections import Counter

N = int(input())

print(sorted(Counter([input() for _ in range(N)]).items(), key=lambda x: x[1], reverse=True)[0][0])
