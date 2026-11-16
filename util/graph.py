import matplotlib.pyplot as plt 


def graph(lst):
    # Graf 1: Alla tre körningar
    for j in range(3):
        x = []
        y = []

        for run, size, mes_time in lst:
            if run == j:
                x.append(size)
                y.append(mes_time)

        plt.plot(x, y, marker="*", linestyle="-", label=f"Körning {j+1}")

    plt.xlabel("Listans storlek")
    plt.ylabel("Exekveringstid (sekunder)")
    plt.title("Alla körningar")
    plt.legend()
    plt.grid()

