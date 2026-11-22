def threesum_pointer(lst, sum=0):
    unique_sum = set()
    new_lst = sorted(lst)
    for i in range(len(new_lst)-2):
        n1 = new_lst[i]
        fp = i+1
        lp = len(new_lst) - 1
        while fp < lp:
            p = new_lst[fp] + new_lst[lp] + n1
            if p == sum:
                unique_sum.add((n1, new_lst[fp], new_lst[lp]))
                fp += 1
            elif p < sum:
                fp += 1
            else:
                lp -= 1

    return list(unique_sum)
