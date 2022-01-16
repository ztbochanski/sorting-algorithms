def insertion_sort(lst):
    for parent_index in range(1, len(lst)):
        child_index = parent_index
        while child_index > 0 and lst[child_index-1] > lst[child_index]:
            # swap
            temp = lst[child_index-1]
            lst[child_index-1] = lst[child_index]
            lst[child_index] = temp
            child_index = child_index - 1


lst = [5, 2, 4, 6, 1, 3]
insertion_sort(lst)
