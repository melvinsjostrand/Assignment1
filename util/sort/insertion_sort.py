def insertion_sort(lst):
    sorted_lst = lst.copy()

    if len(sorted_lst) <= 1:
        return sorted_lst
    for i in range(1, len(sorted_lst)):
        item = sorted_lst[i]
        j = i - 1
        while j >= 0 and item < sorted_lst[j]:
            sorted_lst[j+1] = sorted_lst[j]
            j -= 1
            
        sorted_lst[j+1] = item
    return sorted_lst