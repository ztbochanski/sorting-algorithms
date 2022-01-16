def shellsort(lst):
    # similar to an interval in music, we need a beginning and end value to compare
    # this interval will continue to shrink until we get to the same "note"
    interval = len(lst) // 2  # the range where initial values will be compared

    while interval > 0:  # each iteration will reduce by n/2, n/4, n/8 ... remaining work to 1
        # for every interval in the array (like playing all of the same intervals in a scale, i.e. 3rds up/down the keyboard)
        for index in range(interval, len(lst)):
            # save the current value being compared (root note of interval)
            temp = lst[index]
            j = index
            # swap the elements at this interval if they are not in order already
            while j >= interval and lst[j-interval] > temp:
                lst[j] = lst[j-interval]  # swap
                # decrement j (going backwards from the top of the interval)
                j -= interval

            # set temp to the location of j
            lst[j] = temp
        # reduction of work (shrinking the interval, i.e. 5ths now become 4ths)
        interval //= 2
    return lst


lst = [502, 2, 402, 6, 1, 308, 47]
print(shellsort(lst))
