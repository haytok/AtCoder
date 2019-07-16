result = input()
N = int(input())

for i in range(N):
    start, end = map(int, input().split())
    sliced = result[start-1:end]
    if start == 1:
        result = sliced[::-1] + result[end:]
    elif end == len(result):
        result = result[:start-1] + sliced[::-1]
    else:
        result = result[:start-1] + sliced[::-1] + result[end:]

print(result)

# for i in range(N):
#     start, end = map(int, input().split())
#     result = result[:start-1] + result[start-1:end][::-1] + result[end:]
