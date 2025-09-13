def main():
    X, Y = input().split('.')
    number_Y = int(Y)

    last_str = ''
    if number_Y >= 0 and number_Y <= 2:
        last_str = '-'
    elif number_Y >= 7 and number_Y <= 9:
        last_str = '+'

    print(X + last_str)

if __name__ == '__main__':
    main()
