import time
from util.random_size import random_func
from util.graph import graph
from util.graph_fit import graph_fit


def selection_sort(lst):
    new_lst = list(lst)
    for i in range(len(new_lst)):
        min_index = i
        for j in range(i + 1, len(new_lst)):
            if new_lst[j] < new_lst[min_index]:
                min_index = j
        new_lst[i], new_lst[min_index] = new_lst[min_index], new_lst[i]
    return new_lst


def main():
    result = []
    size = range(100, 850, 50)
    for j in range(3):
        for i in (size):
            lst = random_func(i, 10)
            before = time.time()
            selection_sort(lst)
            mes_time = time.time() - before
            result.append((j, i, mes_time,))

    graph(result)
    graph_fit(result, size)


main()