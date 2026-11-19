from brute import threesum_brute
from pointer import threesum_pointer
from cache import threesum_cache
from test_3sum import test
import sys
import time
sys.path.append(".")
sys.path.append("util/")
sys.path.append("util/graphs/")
from random_size import random_func  # noqa: E402
from graph import graph  # noqa: E402
from graph_avg import graph_fit  # noqa: E402


def main():
    test()
    threesum = [
        ("Brute", threesum_brute),
        ("Pointer", threesum_pointer),
        ("Cache", threesum_cache)

    ]
    repeat = 3
    results = []
    size = range(500, 8000, 500)
    brute_size = range(100, 850, 50)
    for name, threesums in threesum:
        sizes = brute_size if name == "Brute" else size
        for i in range(repeat):
            for j in sizes:
                lst = random_func(j, 10)
                data = lst.copy()
                before = time.time()
                threesums(data)
                mes_time = time.time() - before
                results.append((name, j, mes_time))
    graph("Three sum", results)
    graph_fit("three sum", results, size)


main()