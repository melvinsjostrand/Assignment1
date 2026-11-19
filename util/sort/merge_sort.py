def merge_sort_slow(lst):
    if len(lst) > 1:
        first, last = 0, len(lst)
        mid = (first + last) // 2
        left = lst[first:mid]
        right = lst[mid:last]

        sorted_left = merge_sort_slow(left)
        sorted_right = merge_sort_slow(right)

        sorted = merge_slow(sorted_left, sorted_right)

        return sorted
    else:
        return lst


def merge_slow(left, right):
    sorted = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted += [left[i]]
            i += 1
        else:
            sorted += [right[j]]
            j += 1
    while i < len(left):
        sorted += [left[i]]
        i += 1

    while j < len(right):
        sorted += [right[j]]
        j += 1
    return sorted


lst = [6, -7, 9, -12, 1, 52, 531, 21, 55, -62]

print(merge_sort_slow(lst))