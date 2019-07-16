X = input()

componets = ['o', 'k', 'u']

index = 0

while True:
    if index == len(X)-1:
        print('YES')
        break
    try:
        if X[index] == 'c':
            try:
                if X[index+1] == 'h':
                    index += 2
                else:
                    print('NO')
                    break
            except:
                print('NO')
                break
        elif X[index] in componets:
            index += 1
        else:
            prin('NO')
            break
    except:
        print('NO')
        break

# print('NO'if set(input().replace('ch',''))-set('oku')else'YES')