def main():
    N = int(input())
    inputs = []
    times = []
    for i in range(N):
        A, B = map(lambda s: int(s), input().split(' '))
        times.append(A / B)
        inputs.append([A, B])

    res = 0
    half_time = sum(times) / 2.0
    for i, t in enumerate(times):
        if half_time > t:
            half_time -= t
            res += inputs[i][0]
        else:
            res += half_time * inputs[i][1]
            break
    print(res)

if __name__ == '__main__':
    main()
