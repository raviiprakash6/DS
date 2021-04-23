def sortedRotatedArray(arr, n, elem):
    high = n-1
    low = 0

    while (high >= low):
        mid = int((high + low) / 2)
        if (arr[mid] == elem):
            return mid
        elif (arr[mid] > arr[low]):
            if (arr[mid] > elem >= arr[low]):
                high = mid - 1
            else:
                low = mid + 1
        else:
            if (arr[mid] < elem <= arr[high]):
                low = mid + 1
            else:
                high = mid - 1

    return -1
