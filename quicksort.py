def quicksort2(arr, low, high):
    if low < high:
        pi = partition2(arr, low, high)

        quicksort2(arr, low, pi - 1)
        quicksort2(arr, pi + 1, high)

        return  # arr is sorted in place


def partition2(arr, low, high, tmp_pivot_index=None):
    if tmp_pivot_index is not None:
        tmp_pivot_index = (low + high) // 2
    else:
        tmp_pivot_index = high
    pivot = arr[tmp_pivot_index]

    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[high], arr[i + 1] = arr[i + 1], arr[high]

    return i + 1  # real index of the pivot


# 示例使用
arr = [10, 7, 8, 9, 1, 5]
quicksort2(arr, 0, len(arr) - 1)
print("Sorted array is:", arr)
