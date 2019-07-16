# from collections import Counter

# N, K = map(int, input().split())
# S = input()

# sorted_S = sorted(S)
# diff = 0

# for index, item in enumerate(sorted_S):
#     if S[index] != item:
#         diff += 1
#     print(Counter(S[index:]) - Counter(sorted_S[index:]))
#     print(index, item)


from collections import Counter

N, K = map(int, input().split())
S = input() # atcoder
diff = 0
ans = []
rem = sorted(S) # ['a', 'c', 'd', 'e', 'o', 'r', 't']

print(rem)

# 入力文字列を見ていく
for i in range(N):
    counter = Counter(S[:i+1]) - Counter(ans)
    print(counter)
    counts = sum(counter.values())
    print(counts)
    # ソートされ入力文字列を回す
    for c in rem[:]:
        # ソートされた文字と入力の文字を逐次比較している
        diff1 = diff + (c != S[i])
        diff2 = counts - (counter[c] > 0)
        print(diff1, diff2)
        if diff1 + diff2 <= K:
            ans.append(c)
            print(ans)
            rem.remove(c)
            diff = diff1
            break

print("".join(ans))

"""
7 2
atcoder
"""

"""
10 3
helloworld
"""