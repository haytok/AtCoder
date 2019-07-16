N, K = map(int, input().split())

inputs = []
for _ in range(N):
    key, value = map(int, input().split())
    inputs.append((value, key))

inputs.sort(reverse=True) # valueで降順のソートをかけてる

priority_queue = [] # 値が大きくてまだ種類に加わってない寿司
queue = [] # まだ種類に加わっていない寿司 or 種類に加わっているが値の小さい寿司
sets = set()
for i in range(K):
    value, key = inputs[i]
    if key in sets:
        queue.append(value)
    else:
        priority_queue.append(value)
        sets.add(key)

sum_priority_queue = sum(priority_queue)
sum_queue = sum(queue)
kinds = len(sets)
ans = sum_priority_queue + sum_queue + kinds ** 2
for i in range(K, N):
    if not queue: # 引き換えにされるべき優先度の低いqueue
        break
    value, key = inputs[i]
    if key in sets: # 種類に加わっているが値の小さい寿司は無視
        continue
    sets.add(key)
    sum_queue -= queue.pop()
    sum_priority_queue += value
    kinds += 1
    ans = max(ans, sum_priority_queue + sum_queue + kinds ** 2)

print(ans)
