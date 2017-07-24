def solved_selection_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i, len(ls)):
            if ls[lowest] > ls[j]:
                lowest = j
        temp = ls[lowest]
        del ls[lowest]
        ls.insert(i, temp)
    return ls