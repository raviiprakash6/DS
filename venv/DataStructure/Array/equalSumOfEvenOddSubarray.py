def countSubarraySum(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        sumEven = 0
        sumOdd = 0
        for j in range(i, n):
            if (j % 2 == 0):
                sumEven += arr[j]
            else:
                sumOdd += arr[j]
            if (sumEven == sumOdd):
                count += 1

    return count


arr = [1, 2, 3, 4, 1]
print(countSubarraySum(arr))