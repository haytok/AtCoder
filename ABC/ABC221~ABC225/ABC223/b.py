def left_shift(s):
    return s[1:] + s[:1] 

def main():
    S = input()
    res = []
    for _ in range(len(S)):
        S = left_shift(S)
        res.append(S)
    
    res.sort()

    print(res[0])
    print(res[-1])

if __name__ == '__main__':
    main()
