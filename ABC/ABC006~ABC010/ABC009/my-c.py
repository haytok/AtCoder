from collections import Counter

N, K = map(int, input().split())
S = input()

sorted_S = sorted(S)
ans = []
diff = 0

# 入力文字列を調べていく
for i in range(N):
    used_S = Counter(S[:i+1]) - Counter(ans)
    used_S_counts = sum(used_S.values())
    # ソートされた最強の文字列を見ていく
    for s in sorted_S[:]:
        diff_from_sorted = diff
        diff_from_input = used_S_counts
        if s != S[i]:
            diff_from_sorted += 1
        if used_S[s]:
            diff_from_input -= 1
        if diff_from_sorted + diff_from_input <= K:
            ans.append(s)
            sorted_S.remove(s)
            diff = diff_from_sorted
            break

print(''.join(ans))
