def quick_sort_slow(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivo, left, right = partition_slow(lst)
        sorted_left = quick_sort_slow(left)
        sorted_right = quick_sort_slow(right)
        return sorted_left + [pivo] + sorted_right


def partition_slow(lst):
    pivo = lst[0]
    left, right = [], []

    for i in range(1, len(lst)):
        val = lst[i]
        if val <= pivo:
            left += [val]
        else:
            right += [val]
    return pivo, left, right