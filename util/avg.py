def average(lst, run):
    avg_res = []
    print(lst)
    for size in (run):
        total = 0
        count = 0

        for run, s, time in lst:
            if s == size:
                total += time
                count += 1
        print(total)
        print(count)
        avg = total / count
        avg_res.append((size, avg))
    return avg_res
        