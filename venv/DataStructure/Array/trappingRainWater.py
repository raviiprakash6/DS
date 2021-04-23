def trappingRainWater(arr, c=1):
    n=len(arr):
    sum=0
    for i in arr:
        min()










    n = len(arr)
    a = b = 0
    totalwater = 0
    if (c <= n - 1):
        for i in range(c, n):
            if (arr[i - 1] > arr[i] and a == 0):
                a = arr[i - 1]
            if (arr[i] < a):
                totalwater += a - arr[i]
                b += 1
            if (arr[i] < a and i == n - 1 and arr[i - 1] < arr[i]):
                totalwater = totalwater - (a - arr[i]) * b
            if (arr[i] < a and i == n - 1 and arr[i - 1] > arr[i]):
                totalwater = 0
            if (arr[i] >= a or i == n - 1):
                c = i + 1
                break
    else:
        return 0
    return totalwater + trappingRainWater(arr, c)

arr=[2]
print(trappingRainWater(arr))