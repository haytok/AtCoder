N = int(input())
S = list(int(i) for i in input().split())  
dict = {}
count = 0

for i in range(N):
    if S[i] not in dict:
        dict[S[i]] = 1
    else:
        dict[S[i]] += 1

for key, value in dict.items():
    if key < value:
        count += (value-key)
    elif key > value:
        count += value

print(count)