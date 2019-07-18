from itertools import product

S = input()
ans = 0
for symbol in product(['+', ''], repeat=len(S) - 1):
    string = ''
    for i in range(len(S) - 1):
        string += S[i] + symbol[i]
    ans += eval(string + S[-1])

print(ans)
