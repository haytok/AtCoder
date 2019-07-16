S = input()

ans = 10 ** 15
base = 753

for i in range(len(S)-2):
    ans = min(ans, abs(base - int(S[i:i+3])))

print(ans)

# よくやりがちなやつ
# print(min([abs(753 - int(S[i:i+3])) for i in range(len(S)-2)]))