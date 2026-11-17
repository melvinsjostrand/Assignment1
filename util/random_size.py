import random


def random_func(size, width):
    lst = []
    n = size * width
    for i in range(size):
        r = random.randint(-1 * n, 1 * n)
        lst.append(r)
    return lst