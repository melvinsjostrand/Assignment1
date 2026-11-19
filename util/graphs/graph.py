import matplotlib.pyplot as plt 


def graph(name, lst):
    runs = {}

    for algorithm, size, mes_time in lst:
        if algorithm not in runs:
            runs[algorithm] = []

        runs[algorithm].append((size, mes_time))
    print(runs)
    for algorithm, results in runs.items():
        results.sort()

        sizes = []
        times = []

        for size, mes_time in results:
            sizes.append(size)
            times.append(mes_time)
        plt.plot(sizes, times, marker="*", linestyle="None", label=algorithm)

    plt.title(f"{name} alla körningar")
    plt.xlabel("Listans storlek")
    plt.ylabel("Exekveringstid (sekunder)")
    plt.legend()
    plt.grid()
    plt.show()