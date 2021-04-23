def binarySearch(arr, elem, high, low=0):
    if (low<=high):
        mid = int((low + high) / 2)
        if (elem == arr[mid]):
            return mid
        elif (elem > arr[mid]):
            return binarySearch (arr,elem,high,mid+1)
        elif (elem < arr[mid]):
            return binarySearch(arr,elem,mid-1,low)
    else:
        return -1



#------------------------------------iterative search---------------------------------
def binarySearch(arr,elem,n,low=0):
    high=n-1
    while(low<=high):
        mid=int((low+(high))/2)
        if(arr[mid]==elem):
            return mid
        elif(elem>arr[mid]):
            low=mid+1
        elif(elem<arr[mid]):
            high=mid-1
    return -1

arr=[1,2,6,7,8]
print(binarySearch(arr,3,5))