N = int(input())
S = input()

def cal(data, r, c):
    for i in range(1,N):
        if data[i-1] == "W" and data[i] == "W":
            c += 1
        elif data[i-1] == "E" and data[i] == "E":
            c -= 1
            if r > c:
                r = c
    return r

if S[0] == "E":
    count = S.count("E") -1
    result = count
    result = cal(S, result, count)
else:
    count = S.count("E")
    result = count
    result =  cal(S, result, count)


print(result)