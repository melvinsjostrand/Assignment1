def average(lst, run):
    avg_res = []
    runs = {}

    for result in lst:
        alg, size, mes_time = result[:3]
        if alg not in runs:
            runs[alg] = {}
        if size not in runs[alg]:
            runs[alg][size] = []
        runs[alg][size].append(mes_time)

    for alg, sizes in runs.items():
        for size, times in sizes.items():
            avg = sum(times) / len(times)
            avg_res.append((alg, size, avg))

    return avg_res