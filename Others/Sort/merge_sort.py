# マージソート
def divide(array):
    # 終了条件
    if len(array) == 1:
        return array
    # それ以外
    length = len(array) // 2
    former, latter = array[:length], array[length:]
    former, latter = divide(former), divide(latter)
    return merge(former, latter)

def merge(former, latter):
    res = []
    f_index, l_index = 0, 0
    for _ in range(len(former + latter)):
        if len(former) > 0 and len(latter) > 0:
            if former[0] > latter[0]:
                res.append(former[0])
                former.pop(0)
            elif former[0] < latter[0]:
                res.append(latter[0])
                latter.pop(0)
            else:
                res.append(former[0])
                former.pop(0)
                res.append(latter[0])
                latter.pop(0)
        elif len(former) > 0:
            return res + former
        elif len(latter) > 0:
            return res + latter
        else:
            return res
# def merge_sort(array):
#     former, latter = divide(array)
#     if len(former) != 1:
#         former1, latter1 = divide(former)

if __name__ == "__main__":
    array = [3, 4, 2, 1, 5 , 9, 2]
    ans = divide(array)
    print(ans)

"""
[2,4,1,3]    
[[2,4], [1,3]]
[[[2], [4]], [[1], [3]]] # 分割終わり
[[4,2], [3,1]]
[4,3,2,1]
# 分割
[] -> [], []
# 結合
[], [] ->[]
"""