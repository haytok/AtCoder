# s = input()
# if s.replace("eraser","").replace("erase","").replace("dreamer","").replace("dream","") == "":
#     print("YES")
# else:
#     print("NO")

S = input()[::-1]

while len(S) > 0:
    if S[:5] == 'maerd':
        S = S[5:]
    elif S[:5] == 'esare':
        S = S[5:]
    elif S[:6] == 'resare':
        S = S[6:]
    elif S[:7] == 'remaerd':
        S = S[7:]
    else:
        print('NO')
        break

if len(S) == 0:
    print('YES')
