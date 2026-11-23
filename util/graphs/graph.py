import matplotlib.pyplot as plt 


def graph(name, lst):
    runs = {}

    # Grupperar resultaten efter algoritm och körningsnummer
    for result in lst:

        # Om resultatet innehåller fyra värden finns även körningsnumret
        if len(result) == 4:
            algorithm, size, mes_time, run = result
            key = (algorithm, run)
        else:
            algorithm, size, mes_time = result
            key = (algorithm, None)

        # Skapar en tom lista om gruppen inte redan finns
        if key not in runs:
            runs[key] = []

        # Lägger till liststorleken och exekveringstiden
        runs[key].append((size, mes_time))

    # Skapar en separat kurva för varje algoritm och körning
    for (algorithm, run), results in runs.items():
        results.sort()

        sizes = []
        times = []

        # Delar upp resultaten i liststorlekar och tider
        for size, mes_time in results:
            sizes.append(size)
            times.append(mes_time)

        # Skapar en etikett för diagrammets förklaring
        label = algorithm if run is None else f"{algorithm} - körning {run}"
        plt.plot(sizes, times, marker="*", linestyle="None", label=label)

    plt.title(f"{name} alla körningar")
    plt.xlabel("Listans storlek")
    plt.ylabel("Exekveringstid (sekunder)")
    plt.legend()
    plt.grid()
    plt.show()