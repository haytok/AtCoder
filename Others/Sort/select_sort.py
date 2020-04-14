# 選択ソート
# 昇順にソート

# 配列の中から最小値とその値のインデックスを取る関数
def get_min(array):
    min_index, min_value = 0, 1e10
    for index, value in enumerate(array):
        if min_value > array[index]:
            min_index, min_value = index, array[index]
    return min_index, min_value
            

def select_sort(array):
    for index in range(len(array)):
        min_index, min_value = get_min(array[index+1:])
        target_index = min_index + index + 1
        if target_index > len(array):
            return array
        if array[index] > min_value:
            array[index], array[target_index] = array[target_index], array[index]
    return array

if __name__ == '__main__':
    array = [4, 1, 2, 9, 5, 3, 8, -1]
    print(array)
    # print(get_min(array))
    sorted_array = select_sort(array)
    print(sorted_array)

"""
いきなり問題を解決しようとする傾向にある。
大きな問題を小さな問題に分割して考える癖を付ける。
"""