def indexOfLastOccurence(arr, elem, high, low=0):
    if (low<=high):
        mid = int((low + high) / 2)
        if ((mid==high and elem == arr[mid]) or (elem == arr[mid] and arr[mid]!=arr[mid+1])):
            return mid
        elif(elem < arr[mid]):
            return indexOfLastOccurence(arr,elem,mid-1,low)
        else:
            return indexOfLastOccurence(arr,elem,high,mid+1)
    else:
        return -1

#---------------------------------------Itrative way------------------------------------------------------------

def indexOfLastOccurence(arr, elem, high, low=0):
    while (low <= high):
        mid = int((low + high) / 2)
        if ((arr[mid] == elem and mid == high) or (arr[mid] == elem and arr[mid] != arr[mid + 1])):
                return mid
        elif (elem < arr[mid]):
            high = mid - 1
        else:
            low = mid + 1
    return -1


