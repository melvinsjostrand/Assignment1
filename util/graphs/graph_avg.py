from util.avg_sort import average
import math
from util.lin_reg import lin_reg
import matplotlib.pyplot as plt 


def graph_fit(name, lst, size):

    # Räknar ut genomsnittlig exekveringstid för varje liststorlek
    avg_lst = average(lst, size)
    runs = {}

    # Grupperar medelvärdena efter algoritm
    for algorithm, s, t in avg_lst:
        if algorithm not in runs:
            runs[algorithm] = []
        runs[algorithm].append((s, t))

    # Skapar två diagram bredvid varandra
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle(name)

    # Går igenom varje algoritm
    for algorithm, results in runs.items():
        results.sort()
        sizes = []
        for s, _ in results:
            sizes.append(s)
        times = []
        for _, t in results:
            times.append(t)
            
        ax1.plot(sizes, times, marker="*", linestyle="-", label=algorithm)

        log_x = [math.log(s) for s in sizes]
        log_y = [math.log(t) for t in times]

        # Beräknar en linjär regression på de logaritmerade värdena
        m, k = lin_reg(log_x, log_y)

        # Räknar ut trendlinjens y-värden
        line_y = [m + k * x for x in log_x]
        ax2.plot(
            log_x,
            log_y,
            marker="*",
            linestyle="None",
            label=f"{algorithm} (k={k:.3f})",
        )
        ax2.plot(log_x, line_y, color="red")

    ax1.set_xlabel("Listans storlek")
    ax1.set_ylabel("Genomsnittlig tid (sekunder)")
    ax1.set_title("Genomsnitt")
    ax1.legend()
    ax1.grid()
    ax2.set_xlabel("Logaritmen av listans storlek")
    ax2.set_ylabel("Logaritmen av tiden")
    ax2.set_title("log vs log")
    ax2.legend()
    ax2.grid()

    plt.tight_layout()
    plt.show()
