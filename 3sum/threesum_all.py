from brute import threesum_brute
from pointer import threesum_pointer
from cache import threesum_cache
from test_3sum import test
import sys

sys.path.append(".")
sys.path.append("util/")
sys.path.append("util/graphs/")
from random_size import random_func  # noqa: E402


def main():
    repeat = 5
    size = range(100, 1500, 100)
    for i in range(repeat):
        for j in size:
            lst = random_func(i, 10)
            threesum_brute(lst)
            threesum_pointer(lst)
            threesum_cache(lst)
    test()