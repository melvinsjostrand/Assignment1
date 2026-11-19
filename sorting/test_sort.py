import random
import sys

sys.path.append(".")
sys.path.append("util/")
sys.path.append("util/sort/")
sys.path.append("util/graphs/")
from bucket_sort import bucket_sort  # noqa: E402
from insertion_sort import insertion_sort  # noqa: E402
from radix_sort import radix_sort  # noqa: E402
from selection_sort import selection_sort  # noqa: E402
from bubble_sort import bubble_sort  # noqa: E402
from quick_sort import quick_sort_slow  # noqa: E402
from merge_sort import merge_sort_slow  # noqa: E402


def test():
    for run in range(1, 4):
        randoms = []
        for i in range(15):
            r = random.randint(-10 * run, 10 * run)
            randoms.append(r)

        bucket = bucket_sort(randoms)
        insertion = insertion_sort(randoms)
        radix = radix_sort(randoms)
        selection = selection_sort(randoms)
        bubble = bubble_sort(randoms)
        quick = quick_sort_slow(randoms)
        merge = merge_sort_slow(randoms)

        print("runs", run)
        print("Random list with numbers", randoms)
        print("Bucket sort", bucket)
        print("Insertion sort", insertion)
        print("Radix sort", radix)
        print("Selection sort", selection)
        print("Bubble sort", bubble)
        print("Quick sort", quick)
        print("Merge sort", merge)
        print()
        if (
            bucket
            == insertion
            == radix
            == selection
            == bubble
            == quick
            == merge
        ):
            print("All tests passed!")
        else:
            print("Something went wrong")


def main():
    test()


main()