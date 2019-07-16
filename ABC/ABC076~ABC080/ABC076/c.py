s = list(input())
T = list(input())
flag = False
result = ""

for i in range(len(s)-len(T)+1):
    ss = s[i:i+len(T)]
    for j in range(len(T)):
        if ss[j] != "?" and ss[j] !=T[j]:
            break
    else:
        flag = True
        begin = i

if flag:
    for i in range(len(T)):
        s[begin+i] = T[i]
    for i in range(len(s)):
        if s[i] == "?":
            s[i] = "a"
        result += s[i]
    print(result)
else:
    print("UNRESTORABLE")
