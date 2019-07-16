S = input()

counts_black = S.count('B')
index = 0

for i in range(len(S)):
    if S[i] == 'B':
        index += i


print(sum(list(range(len(S)-counts_black, len(S)))) - index)
