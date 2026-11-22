def quick_sort_improved(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivo, left, right = partition_slow(lst)
        sorted_left = quick_sort_improved(left)
        sorted_right = quick_sort_improved(right)
        return sorted_left + [pivo] + sorted_right


def partition_slow(lst):
    first = lst[0]
    mid = lst[len(lst) // 2]
    last = lst[-1]

    if (first <= mid <= last) or (last <= mid <= first):
        pivo = mid
    elif (mid <= first <= last) or (last <= first <= mid):
        pivo = first
    else:
        pivo = last

    left, right = [], []

    for i in range(len(lst)):
        if lst[i] == pivo:
            pivo_index = 1
            break
    for i in range(len(lst)):
        if i == pivo_index:
            continue
        val = lst[i]

        if val <= pivo:
            left += [val]
        else:
            right += [val]

    return pivo, left, right