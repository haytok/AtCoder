def main():
    length = len(set(list(input())))

    if length == 2:
        ans = 3
    elif length == 3:
        ans = 6
    else:
        ans = 1
    
    print(ans)

if __name__ == '__main__':
    main()
