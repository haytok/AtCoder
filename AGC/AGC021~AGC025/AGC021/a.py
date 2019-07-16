N = str(input())

for item in N[1:]:
    if item != '9':
        print(int(N[0]) - 1 + 9 * (len(N) - 1))
        break
else:
    print(int(N[0]) + 9 * len(N[1:]))
