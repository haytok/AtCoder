N = int(input())
input_list = [int(input()) for i in range(N)]

pointer = input_list[0]
count = 1
index = 0

while True:
    if pointer == 2:
        print(count)
        break
    if index == 10**5 + 1:
        print(-1)
        break
    pointer = input_list[pointer-1]
    count += 1
    index += 1