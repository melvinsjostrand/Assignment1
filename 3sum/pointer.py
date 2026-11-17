import sys
import time

sys.path.append(".")
sys.path.append("util/")
sys.path.append("util/graphs/")

from random_size import random_func  # noqa: E402
from graph_fit import graph_fit  # noqa: E402
from graph import graph  # noqa: E402


def threesum_pointer(lst, sum=0):
    unique_sum = set()
    new_lst = sorted(lst)
    for i in range(len(new_lst)-2):
        n1 = new_lst[i]
        fp = i+1
        lp = len(new_lst) - 1
        while fp < lp:
            p = new_lst[fp] + new_lst[lp] + n1
            if p == sum:
                unique_sum.add((n1, new_lst[fp], new_lst[lp]))
                fp += 1
            elif p < sum:
                fp += 1
            else:
                lp -= 1

    return list(unique_sum)


def main():
    size = range(100, 850, 50)
    print("code is running...")
    result = []
    for j in range(3):
        for i in (size):
            lst = random_func(i, 10)
            before = time.time()
            threesum_pointer(lst)
            mes_time = time.time() - before
            result.append((j, i, mes_time,))
    graph("Pointer", result)
    graph_fit("Pointer", result, size)


main()