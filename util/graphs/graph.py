import matplotlib.pyplot as plt 


def graph(name, lst):
    runs = {}

    for result in lst:
        if len(result) == 4:
            algorithm, size, mes_time, run = result
            key = (algorithm, run)
        else:
            algorithm, size, mes_time = result
            key = (algorithm, None)

        if key not in runs:
            runs[key] = []

        runs[key].append((size, mes_time))

    for (algorithm, run), results in runs.items():
        results.sort()

        sizes = []
        times = []

        for size, mes_time in results:
            sizes.append(size)
            times.append(mes_time)
        label = algorithm if run is None else f"{algorithm} - körning {run}"
        plt.plot(sizes, times, marker="*", linestyle="None", label=label)

    plt.title(f"{name} alla körningar")
    plt.xlabel("Listans storlek")
    plt.ylabel("Exekveringstid (sekunder)")
    plt.legend()
    plt.grid()
    plt.show()