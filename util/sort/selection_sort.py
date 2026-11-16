def selection_sort(lst):
    new_lst = lst
    for i in range(len(new_lst)):
        min_idx = i
        for j in range(i + 1, len(new_lst)):
            if new_lst[j] < new_lst[min_idx]:
                min_idx = j
        new_lst[i], new_lst[min_idx] = new_lst[min_idx], new_lst[i]
    return new_lst


lst = [6, 5, 9, -12, -2, -7]
print(selection_sort(lst))

