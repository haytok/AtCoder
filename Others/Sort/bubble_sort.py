# バブルソート
# 昇順にソート
def bubble_sort(array):
    length = len(array)
    for index in range(length - 1):
        if index + 1 > length:
            continue
        else:
            if array[index] > array[index+1]:
                array[index], array[index+1] = array[index+1], array[index]
    return array

if __name__ == '__main__':
    array = [4, 1, 2, 9, 5, 7, 8]
    print(array)
    sorted_array = bubble_sort(array)
    print(sorted_array)