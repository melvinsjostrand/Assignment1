import sys
import time

sys.path.append(".")
sys.path.append("util/")
sys.path.append("util/graphs/")

from random_size import random_func  # noqa: E402
from graph_fit import graph_fit  # noqa: E402
from graph import graph  # noqa: E402


def threesum_brute(lst, sum=0):
    unique_sum = set()
    lst = sorted(lst)
    for i in range(len(lst)-2):
        n1 = lst[i]
        for j in range(i+1, len(lst)-1):
            n2 = lst[j]
            for x in range(j+1, len(lst)):
                n3 = lst[x]
                if n1 + n2 + n3 == sum:
                    p = tuple(sorted((n1, n2, n3)))
                    unique_sum.add(p)
    return list(unique_sum)