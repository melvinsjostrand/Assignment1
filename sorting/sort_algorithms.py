import sys
import time

sys.path.append(".")
sys.path.append("util/")
sys.path.append("util/sort/")
sys.path.append("util/graphs/")

from random_size import random_func  # noqa: E402
from bucket_sort import bucket_sort  # noqa: E402
from insertion_sort import insertion_sort  # noqa: E402
from radix_sort import radix_sort  # noqa: E402
from selection_sort import selection_sort  # noqa: E402
from bubble_sort import bubble_sort  # noqa: E402
from quick_sort import quick_sort_slow  # noqa: E402
from merge_sort import merge_sort_slow  # noqa: E402
from graph_avg import graph_fit  # noqa: E402
from graph import graph  # noqa: E402
from quick_sort_improved import quick_sort_improved  # noqa : E402
 

def main():
    sorters = [
        ("bubbel sort", bubble_sort),
        ("merge sort", merge_sort_slow),
        ("quick sort", quick_sort_slow),
        ("bucket sort", bucket_sort),
        ("insertion sort", insertion_sort),
        ("radix sort", radix_sort),
        ("selection sort", selection_sort),
        ("quick_sort_improved", quick_sort_improved)
    ]
    results = []
    repeat = 5
    size = range(500, 9000, 500)
    for name, sort_function in sorters:
        for run in range(1, repeat + 1):
            for i in size:
                # print(i)
                lst = random_func(i)
                data = lst.copy()
                before = time.time()
                sort_function(data)
                mes_time = time.time() - before
                results.append((name, i, mes_time, run))
    graph("Sorteringsalgoritmer", results)
    graph_fit("sorteringsalgoritmer", results, size)


main()

