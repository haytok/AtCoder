# アルゴリズムは完璧なはずなのに、Pythonの仕様のせいか上手く行かなかった

N = int(input())
inputs = [int(input()) for _ in range(N)]

input_count_dict = {key: value for value, key in enumerate(sorted(list(set(inputs))))}

for input in inputs:
    print(input_count_dict[input])