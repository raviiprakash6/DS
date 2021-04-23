def indexOfFirstOccurence(arr, elem, high, low=0):
    while (low <= high):
        mid = int((low + high) / 2)
        if ((arr[mid] == elem and mid == 0) or (arr[mid] == elem and arr[mid] != arr[mid - 1])):
                return mid
        elif (arr[mid] < elem):
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [1, 10, 10, 10, 20, 20,20, 40]
indexOfFirstOccurence(arr, 20, 7)


#---------------------------------------Recursion-----------------------------------------
def indexOfFirstOccurence(arr, elem, high, low=0):
    if (low<=high):
        mid = int((low + high) / 2)
        if ((mid==0 and elem == arr[mid]) or (arr[mid]!=arr[mid-1] and elem == arr[mid])):
            return mid
        elif (elem > arr[mid]):
            return indexOfFirstOccurence (arr,elem,high,mid+1)
        else:
            return indexOfFirstOccurence(arr,elem,mid-1,low)
    else:
        return -1

