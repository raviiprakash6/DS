def leftRoatateByD(arr,d):
    res = []
    n = len(arr)
    c = 0
    d=d%n
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
