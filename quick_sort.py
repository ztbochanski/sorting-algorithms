def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        # 1. choose a pivot
        pivot = lst[0]

        # 2.1 partition smaller
        smaller_subarray = []
        for i in lst[1:]:
            if i <= pivot:
                smaller_subarray.append(i)

        # 2.2 partition larger
        larger_subarray = []
        for i in lst[1:]:
            if i >= pivot:
                larger_subarray.append(i)

        # 3 recursively swap
        sorted_lower_than_pivot = quicksort(smaller_subarray)
        sorted_larger_than_pivot = quicksort(larger_subarray)

        # 4 add together the partitions
        return sorted_lower_than_pivot + [pivot] + sorted_larger_than_pivot


lst = [5, 2, 4, 6, 1, 3]
print(quicksort(lst))
