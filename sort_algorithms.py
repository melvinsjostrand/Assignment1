def main():
    result = []
    size = range(100, 850, 50)
    for j in range(3):
        for i in (size):
            lst = random_func(i, 10)
            before = time.time()
            selection_sort(lst)
            mes_time = time.time() - before
            result.append((j, i, mes_time,))

    graph(result)
    graph_fit(result, size)


main()