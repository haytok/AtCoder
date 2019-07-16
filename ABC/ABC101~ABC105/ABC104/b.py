S = input()

if S[0] == "A":
    if S[2:-1].count("C") == 1:
        index = S.index("C")
        S = S[1:index] + S[index+1:]
        if S.islower():
            print("AC")
        else:
            print("WA")
    else:
        print("WA")
else:
    print("WA")