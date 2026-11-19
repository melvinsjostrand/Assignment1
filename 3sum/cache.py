def threesum_cache(lst, sum=0):
    unique_sum = set()
    lst = sorted(lst)
    for i in range(len(lst)-2):
        n1 = lst[i]
        cache = set()
        for j in range(i+1, len(lst)):
            n2 = lst[j]
            n3 = sum - (n1 + n2)
            if n3 in cache:
                if n3 < n2:
                    n2, n3 = n3, n2
                unique_sum.add((n1, n2, n3))
            else:
                cache.add(n2)

    return list(unique_sum)

