from util.avg import average
import math
from util.lin_reg import lin_reg
import matplotlib.pyplot as plt 


def graph_fit(name, lst, size):
    avg_lst = average(lst, size)
    
    sizes = []
    for s, t in avg_lst:
        sizes.append(s)
    times = []
    for s, t in avg_lst:
        times.append(t)
    log_x = []
    for s in sizes:
        s = math.log(s)
        log_x.append(s)
    log_y = []
    for t in times:
        t = math.log(t)
        log_y.append(t)
    m, k = lin_reg(log_x, log_y)
    line_y = []
    for x in log_x:
        line_y.append(m + k * x)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle(name)
    ax1.plot(sizes, times, marker="*", linestyle="None")
    ax1.set_xlabel("Listans storlek")
    ax1.set_ylabel("Genomsnittlig tid (sekunder)")
    ax1.set_title("Genomsnitt")
    ax1.grid()

    ax2.plot(log_x, log_y, marker="*", linestyle="None", label="Mätpunkter")
    ax2.plot(log_x, line_y, color="red", label=f"Linje med k = {k:.3f}")
    ax2.set_xlabel("Logaritmen av listans storlek")
    ax2.set_ylabel("Logaritmen av tiden")
    ax2.set_title(f"log vs log, k = {k:.3f}")
    ax2.legend()
    ax2.grid()

    plt.tight_layout()
    plt.show()
