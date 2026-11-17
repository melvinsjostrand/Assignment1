import time
from util.random_size import random_func
from util.graphs.graph import graph
from util.graphs.graph_fit import graph_fit


def selection_sort(lst):
    new_lst = list(lst)
    for i in range(len(new_lst)):
        min_index = i
        for j in range(i + 1, len(new_lst)):
            if new_lst[j] < new_lst[min_index]:
                min_index = j
        new_lst[i], new_lst[min_index] = new_lst[min_index], new_lst[i]
    return new_lst