"""基数排序（Radix Sort）是一种非比较型整数排序算法，其基本思想是将整数按位数切割成不同的数字，然后按每个位数分别比较。由于整数也可以表示字符串（如姓名或日期）和特定格式的浮点数，所以基数排序也不仅限于整数。

基数排序通常使用两种方法：LSD（Least Significant Digit，最低位优先）和MSD（Most Significant Digit，最高位优先）。这里，我将提供一个 LSD 基数排序的 Python 实现，并在代码中详细注释每一步的意义。"""


def radix_sort(arr):
    max_digits = max([len(str(i)) for i in arr])
    buckets = 10
    # print(f"""arr={arr}""")
    for digit in range(max_digits):
        bucket_arr = [[] for _ in range(buckets)]
        # print(f"""bucket_arr={bucket_arr}""")
        for i in arr:
            bucket_index = (
                i // 10**digit
            ) % 10  # %10 is for the situation that i_digits - digit > 1
            # print(f"""i={i}, bucket_index={bucket_index}""")
            bucket_arr[bucket_index].append(i)
            # print(f"""bucket_arr={bucket_arr}""")
        arr = sum(bucket_arr, [])
        # print(f"""arr={arr}""")
    return arr


# 示例使用
arr = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_arr = radix_sort(arr)
print("Sorted array is:", sorted_arr)
