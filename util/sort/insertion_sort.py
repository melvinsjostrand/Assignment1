def insertion_sort(lst):
    n = len(lst)
    if n <= 1:
        return
    for i in range(1, n):
        item = lst[i]
        j = i - 1
        print(lst)
        while j >= 0 and item < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
            
        lst[j+1] = item


arr = [12, 11, 13, 5, -1]
insertion_sort(arr)
print(arr)