def bubble_sort(lst):
    new_lst = lst.copy()
    n = len(new_lst)

    for i in range(n-1):
        for j in range(n-i-1):
            if new_lst[j] > new_lst[j+1]:
                new_lst[j], new_lst[j+1] = new_lst[j+1], new_lst[j]

    return new_lst