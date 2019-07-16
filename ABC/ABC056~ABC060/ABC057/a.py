A, B = map(int, input().split())
time = A + B
print(time if time < 24 else time-24)

# print((A+B) % 24)
# print(sum(map(int,input().split()))%24)

# 自分の書き方やと汎用性が低い。時計的に考えることが汎用性が高い
# 入力を足し算するか、mapオブジェクトをsum関数に書けるかの二択になりそう









