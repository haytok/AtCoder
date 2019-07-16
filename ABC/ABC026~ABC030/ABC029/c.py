N = int(input())

elements = ['a', 'b', 'c']
first = ['a', 'b', 'c']

def saiki(items):
    ans = []
    for item in items:
        for element in elements:
            ans.append(item + element)
    return ans

for i in range(N-1):
    first = saiki(first)

for i in first:
    print(i)

# itertools を使う解法
# from itertools import product
# for i in product(['a', 'b', 'c'], repeat(int(input()))):
#     print(''.join(i))
