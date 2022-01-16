def mergesort(lst):
    # 1. base case array divided to size 1, T(n) = 1
    if len(lst) < 2:
        return lst
    else:
        # 2. reduce the work n/2 (split array)
        left_half = mergesort(lst[:len(lst)//2])
        right_half = mergesort(lst[len(lst)//2:])
        # 3. base work O(n): comparing the elements and sorting
        sorted = []
        while 0 < len(left_half) and 0 < len(right_half):
            if left_half[0] <= right_half[0]:
                sorted.append(left_half.pop(0))
            else:
                sorted.append(right_half.pop(0))
        # 4. combine sorted subarray and return
        return sorted + left_half + right_half


lst = [5, 2, 4, 6, 1, 3]
print(mergesort(lst))
