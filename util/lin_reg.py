def lin_reg(x, y):
    # Hämtar antalet mätpunkter
    n = len(x)

    # Beräknar summorna som behövs för linjär regression
    sx = sum(x)
    sy = sum(y)
    sxx = sum(i * i for i in x)
    sxy = sum(x[i]*y[i] for i in range(n))

    # Beräknar nämnaren i formlerna för lutning och skärningspunkt
    denominator = n * sxx - sx ** 2

    # Beräknar linjens skärningspunkt med y-axeln
    m = (sxx * sy - sx * sxy) / denominator

    # Beräknar linjens lutning
    k = (n * sxy - sx * sy) / denominator
    return m, k