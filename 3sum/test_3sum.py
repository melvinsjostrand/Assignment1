import random
from brute import threesum_brute
from cache import threesum_cache
from pointer import threesum_pointer


def test():
    n = 15
    for run in range(1, 4):
        randoms = []
        for i in range(n):
            r = random.randint(-10 * n, 10 * n)
            randoms.append(r)
        brute = threesum_brute(randoms)
        cache = threesum_cache(randoms)
        pointer = threesum_pointer(randoms)
        print(randoms)
        print("runs", run)
        print(brute, "BRUTE 3 SUM")
        print(cache, "CACHE 3 SUM")
        print(pointer, "POINTER 3 SUM")

        assert set(brute) == set(cache) == set(pointer)

        print("All tests passed!")
        print(f"Brute: {len(brute)} triplets")
        print(f"Cache: {len(cache)} triplets")
        print(f"Pointer: {len(pointer)} triplets")


def main():
    test()


main()