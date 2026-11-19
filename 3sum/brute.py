def threesum_brute(lst, sum=0):
    unique_sum = set()
    lst = sorted(lst)
    for i in range(len(lst)-2):
        n1 = lst[i]
        for j in range(i+1, len(lst)-1):
            n2 = lst[j]
            for x in range(j+1, len(lst)):
                n3 = lst[x]
                if n1 + n2 + n3 == sum:
                    p = tuple(sorted((n1, n2, n3)))
                    unique_sum.add(p)
    return list(unique_sum)
