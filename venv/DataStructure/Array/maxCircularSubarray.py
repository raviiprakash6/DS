def maxCircularSubarray(arr):
    n = len(arr)
    maxsum = 0

    for i in range(n):
        sum = 0
        for j in range(n):
            index = (i + j) % n
            sum = sum + arr[index]
            if (sum > maxsum):
                maxsum = sum

    return maxsum


print(maxCircularSubarray([1, 6, -6, 3, 4,-4, 1]))