from brute import threesum_brute
from pointer import threesum_pointer
from cache import threesum_cache
from test_3sum import test
import sys
import time

# Lägger till sökvägar så att Python hittar modulerna
sys.path.append(".")
sys.path.append("util/")
sys.path.append("util/graphs/")
from random_size import random_func  # noqa: E402
from graph import graph  # noqa: E402
from graph_avg import graph_fit  # noqa: E402


def main():
    # Kör testerna för att kontrollera att algoritmerna fungerar
    test()

    # Samlar algoritmerna i en lista för att kunna köra dem på samma sätt    
    threesum = [
        ("Brute", threesum_brute),
        ("Pointer", threesum_pointer),
        ("Cache", threesum_cache),
    ]
    repeat = 5
    results = []
    size = range(2500, 10000, 500)
    brute_size = range(100, 900, 50)
    for name, threesums in threesum:
        # Väljer liststorlekar beroende på vilken algoritm som körs 
        sizes = brute_size if name == "Brute" else size
        for run in range(1, repeat + 1):
            for j in sizes:
                lst = random_func(j)
                data = lst.copy()
                before = time.time()
                threesums(data)
                measure_time = time.time() - before
                results.append((name, j, measure_time, run))
    graph("Three sum", results)
    graph_fit("three sum", results, size)


main()