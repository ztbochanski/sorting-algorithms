def selection_sort(lst):
    for i in range(len(lst)-1):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index is not i:
            # swap
            temp = lst[i]
            lst[i] = lst[min_index]
            lst[min_index] = temp


lst = [5, 2, 4, 6, 1, 3]
selection_sort(lst)
