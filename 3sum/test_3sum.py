import random
from brute import threesum_brute
from cache import threesum_cache
from pointer import threesum_pointer


def test():
    randoms = []

    for run in range(1, 4):
        for i in range(4):
            r = random.randint(-15, 15)
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