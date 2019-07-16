N, M = map(int, input().split())
input_list = [[int(i) for i in input().split()] for i in range(M)]

first_element = set()
second_element = set()

for element in input_list:
    if element[0] == 1:
        first_element.add(element[1])
    elif element[1] == N:
        second_element.add(element[0])

if first_element & second_element:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

# 以下のように書けていたら、わざわざ無駄に配列に値を入れたりして、余分なメモリ使わんで済んだ
# N, M = map(int, (input().split()))
# for _ in range(M):
#     f, t = map(int, (input().split()))
#     if f == 1:
#         to_middle.add(t)
#     elif t == N:
#         from_middle.add(f)
