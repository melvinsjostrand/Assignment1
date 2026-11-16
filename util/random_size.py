import random


def random_func(size, width):
    lst = []
    n = size * width
    for i in range(size):
        r = random.randint(-10 * n, 10 * n)
        lst.append(r)
    return lst