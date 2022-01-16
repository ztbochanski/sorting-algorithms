def countingsort(lst, exp1):

    n = len(lst)

    output = [0] * (n)

    count = [0] * (10)

    for i in range(0, n):
        index = lst[i] // exp1
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = lst[i] // exp1
        output[count[index % 10] - 1] = lst[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(lst)):
        lst[i] = output[i]


def radixsort(lst):

    max1 = max(lst)

    exp = 1
    while max1 / exp > 1:
        countingsort(lst, exp)
        exp *= 10
    return lst


lst = [5, 2, 4, 6, 1, 3]
print(radixsort(lst))
