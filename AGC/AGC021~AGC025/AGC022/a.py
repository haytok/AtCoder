S = input()

ans = ''

if len(S) != 26:
    a_z = [chr(i) for i in range(97, 123)]
    for s in S:
        a_z.remove(s)
    ans = S + a_z[0]
    print(ans)
else:
    if S == 'zyxwvutsrqponmlkjihgfedcba':
        ans = -1
        print(ans)
    else:
        a_z = [int(i) for i in range(97, 123)]
        inputs = list(map(ord, list(S)))
        buf = [inputs[-1]]
        for i in range(1, len(S)):
            if inputs[25-i] > inputs[25-(i-1)]:
                buf.append(inputs[25-i])
            else:
                buf.sort()
                for item in buf:
                    if inputs[25-i] < item:
                        print(''.join(list(map(chr, inputs[:25-i]+[item]))))
                        exit()
