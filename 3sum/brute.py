def threesum_brute(lst, sum=0):
    unique_sum = set()
    lst = sorted(lst)
    for i in range(len(lst)-2):
        ni = lst[i]
        for j in range(i+1, len(lst)-1):
            nj = lst[j]
            for x in range(j+1, len(lst)):
                nk = lst[x]
                if ni + nj + nk == sum:
                    p = tuple(sorted((ni, nj, nk)))
                    unique_sum.add(p)
    return list(unique_sum)


