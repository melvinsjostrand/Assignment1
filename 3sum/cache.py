import sys
import time

sys.path.append(".")
sys.path.append("util/")
sys.path.append("util/graphs/")

from random_size import random_func  # noqa: E402
from graph_fit import graph_fit  # noqa: E402
from graph import graph  # noqa: E402


def threesum_cache(lst, sum=0):
    unique_sum = set()
    lst = sorted(lst)
    for i in range(len(lst)-2):
        n1 = lst[i]
        cache = set()
        for j in range(i+1, len(lst)):
            n2 = lst[j]
            n3 = sum - (n1 + n2)
            if n3 in cache:
                if n3 < n2:
                    n2, n3 = n3, n2
                unique_sum.add((n1, n2, n3))
            else:
                cache.add(n2)

    return list(unique_sum)


def main():
    size = range(1000, 2000, 200)
    print("code is running...")
    result = []
    for j in range(3):
        for i in (size):
            lst = random_func(i, 10)
            before = time.time()
            threesum_cache(lst)
            mes_time = time.time() - before
            print(mes_time)
            result.append((j, i, mes_time,))
    graph("Cache", result)
    graph_fit("Cache", result, size)


main()