def countOnes(arr, n,elem=1,low=0):
    high=n-1
    while (low <= high):
        mid = int((low + high) / 2)
        if ((arr[mid] == elem and mid == 0) or (arr[mid] == elem and arr[mid] != arr[mid - 1])):
                return n-mid
        elif (arr[mid] < elem):
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [0,0,1,1,1]
print(countOnes(arr,5))
