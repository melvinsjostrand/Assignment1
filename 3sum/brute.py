import sys
import time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from util.random_size import random_func
from util.graph_fit import graph_fit
from util.graph import graph


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


def main():
    size = range(100, 200, 50)
    print("code is running...")
    result = []
    for j in range(3):
        for i in (size):
            lst = random_func(i, 10)
            before = time.time()
            threesum_brute(lst)
            mes_time = time.time() - before
            result.append((j, i, mes_time,))
    graph("Brute", result)
    graph_fit("Brute", result, size)


main()