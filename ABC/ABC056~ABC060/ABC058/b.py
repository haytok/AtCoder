O = input()
E = input()

ans = ""

for i in range(len(O)):
    try:
        ans += O[i]
        ans += E[i]
    except IndexError:
        pass

print(ans)