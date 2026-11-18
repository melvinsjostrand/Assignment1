import sys
import time

sys.path.append(".")
sys.path.append("util/")
sys.path.append("util/sort/")
sys.path.append("util/graphs/")

from random_size import random_func  # noqa: E402
from bucket_sort import bucket_sort  # noqa: E402
from insertion_sort import insertion_sort  # noqa: E402
from radix_sort import radix  # noqa: E402
from selection_sort import selection_sort  # noqa: E402
from sort_graph import sort_graph  # noqa: E402
# from graph_avg_sort import graph_fit  # noqa: E402
from util.avg_sort import average  # noqa: E402
 

def main():
    sorters = [
        ("bucket sort", bucket_sort),
        ("insertion sort", insertion_sort),
        ("radix sort", radix),
        ("selection sort", selection_sort),
    ]
    results = []
    repeat = 3
    size = range(1000, 2000, 100)
    for name, sort_function in sorters:
        for j in range(repeat):
            for i in size:
                #print(i)
                lst = random_func(i, 10)
                data = lst.copy()
                before = time.time()
                sort_function(data)
                mes_time = time.time() - before
                results.append((name, i, mes_time))
    avg = average(results, size)
    print(avg)
    sort_graph("Sorteringsalgoritmer – medelvärden", avg)
    sort_graph("sorteringsalgoritmer", results)


main()

