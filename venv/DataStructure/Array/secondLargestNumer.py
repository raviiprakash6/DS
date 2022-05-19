def secondLargestNumber(arr):
    n = len(arr)
    large = arr[0]
    secondLarge = -1
    for i in range(1, n):
        if arr[i] > large:
            secondLarge = large
            large = arr[i]
        elif arr[i] < large and arr[i] > secondLarge:
            secondLarge = arr[i]
    return secondLarge


arr = [12, 35, 1, 10, 34, 1]
print(secondLargestNumber(arr))
