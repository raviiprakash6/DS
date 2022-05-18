def leftRoatateByD(arr, d):
    res = []
    n = len(arr)
    c = 0
    d = d % n
    for i in range(n):
        if (i + d < n):
            res.append(arr[d + i])
        else:
            res.append(arr[c])
            c = c + 1
    return res


# arr = [0, 1, 2, 3, 4]
# d = 2
#
# leftRoatateByD(arr, d)


def swap(arr, low, high):
    while (high > low):
        arr[low], arr[high] = arr[high], arr[low]
        high -= 1
        low += 1


def leftRoatateByD_1(arr, d, n):
    swap(arr, 0, d-1)
    swap(arr, d, n-1)
    swap(arr, 0, n-1)
    return arr


arr = [20, 30, 10, 15, 24, 21]
print(leftRoatateByD_1(arr, 2, 6))
