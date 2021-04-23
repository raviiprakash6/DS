def peakElem(arr,n):
    low=0
    high=n-1
    while(low<=high):
        mid=int((low+high)/2)
        if( low==n-1 or high==0 or arr[mid-1]<=arr[mid]>=arr[mid+1]):
            return arr[mid]
        elif(arr[mid-1]>=arr[mid]):
            high=mid-1
        else:
            low=mid+1
    return -1

arr=[2,3,5,4,1]
print(peakElem(arr,n))